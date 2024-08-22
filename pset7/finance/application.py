# Pset 7
# Implementaciones: register, quote, buy, index, sell, history
# 16/11/2021
# Debido a que tuve problemas con la primera version del codigo y debido a los comentarios de un STAFF sobre la forma en que estaba escrito preferia inciar de cero
import os
import datetime
import time
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask import Flask
from flask import request
from flask import Flask, request
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Mostrar cartera de acciones
    cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    stocks = db.execute("SELECT stock, shares, total, price FROM portfolio WHERE id=:id", id=session["user_id"])

    if not stocks:
        return render_template("index1.html", cash=usd(cash[0]['cash']))
    else:
        prices = db.execute("SELECT stock, shares, total, price FROM portfolio WHERE id=:id", id=session["user_id"])
        for price in prices:
            symbol = prices[0]['stock']
            price = lookup(symbol)['price']
            shares = prices[0]['shares']
            total = price * shares
            db.execute("Update portfolio set price=:price, total=:total WHERE id=:id AND stock=:symbol",
                        price=price, total=total, id=session["user_id"], symbol=symbol)

        sumnums = db.execute("SELECT SUM(total) AS \"sumnums\" FROM portfolio WHERE id=:id", id=session["user_id"])

        if sumnums:
            grand_total = sumnums[0]['sumnums']+(cash[0]['cash'])

        else:
            grand_total = cash[0]['cash']

        return render_template("index.html", cash=usd(cash[0]['cash']), grand_total=usd(grand_total), stocks=stocks)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # Comprar acciones
    if request.method == "POST":
        # Mensaje para que el usuario introduzca el simbolo
        if not request.form.get("symbol"):
            return apology("debe proporcionar el simbolo", 400)
        # Mensaje para que el usuario sepa que introdujo un numero invalido
        if not request.form.get("shares") or not request.form.get("shares").isdigit() or float(request.form.get("shares")) % 1 != 0 or int(request.form.get("shares")) <= 0:
            return apology("Numero invalido", 400)
        # Busca el simbolo de accion
        lookedup = lookup(request.form.get("symbol"))
        # En el caso que no encuentre el simbolo envia un mensaje de simbolo invalido
        if not lookedup:
            return apology("simbolo invalido", 400)
        # Buscamos el dinero que tienen el usuario en la base de batos
        cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        # Revisamos el costo de la aacion
        value = lookedup["price"] * int(request.form.get("shares"))

        if value > cash[0]['cash']:
            # Enviamos mensaje porque no tiene dinero suficiente para comprar la accion
            return apology("Te hace falta dinero", 400)

        # Actualizamos la tabla de transacciones
        transaction = db.execute("INSERT INTO transactions (id, worth, shares, symbol, purchase, price) VALUES (:id, :worth, :shares,:symbol, :purchase, :price)",
                                id=session["user_id"], worth=value, shares=int(request.form.get("shares")), symbol=lookedup["symbol"], price=lookedup["price"], purchase="purchase")
        # Actualizamos el portfolio
        update = db.execute("SELECT shares FROM portfolio WHERE id=:id AND stock=:symbol",
                            id=session["user_id"], symbol=lookedup["symbol"])

        if not update:
            db.execute("INSERT INTO portfolio (id, stock, shares, price, total) VALUES(:id, :symbol, :shares, :total, :price)",
                        id=session["user_id"], symbol=lookedup["symbol"], shares=int(request.form.get("shares")), total=value, price=lookedup['price'])

        else:
            new_shares = update[0]['shares'] + int(request.form.get("shares"))
            new_total = new_shares*lookedup['price']
            db.execute("UPDATE portfolio SET shares =: shares. total=:total, price =: price WHERE id =: id and stock =: symbol",
                        shares=new_shares, total=new_total, id=session["user_id"], symbol=lookedup["symbol"], price=loockedup['price'])

        # Actualizamos el saldo del usuario
        new_cash = cash[0]['cash'] - value
        update = db.execute("UPDATE users SET cash = :value WHERE id = :id", value=new_cash, id=session["user_id"])
        return render_template("bought.html", cash=usd(new_cash), price=usd(lookedup['price']), total=usd(value), shares=request.form.get("shares"), symbol=request.form.get("symbol"))
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Mostrar historial de transacciones
    transactions = db.execute("SELECT symbol, shares, price, time, purchase FROM transactions WHERE id=:id", id=session["user_id"])
    return render_template("history.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/changepassword", methods=["GET", "POST"])
def changepassword():
    if request.method == "POST":
        if not request.form.get("new_password"):
            return apology("introduzca nueva contrasena", 403)
        if not request.form.get("password"):
            return apology("introduzca vieja contrasena", 403)

        rows = db.execute("SELECT hash FROM users WHERE id = :id_user", id_user=session["user_id"])
        pass2 = request.form.get("password")

        if not check_password_hash(rows[0]['hash'], pass2):
            return apology("contrasena antigua invalida", 403)
        db.execute("UPDATE users SET hash= :hash WHERE id=:id_user", hash=generate_password_hash(
            request.form.get("new_password")), id_user=session["user_id"])
        return redirect("/")
    else:
        return render_template("changepassword.html")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # Obtenga cotización de acciones.
    if request.method == "POST":
        try:
            symbol = request.form.get("symbol")
            accion = lookup(symbol)

            if not accion:
                return apology("NO se encontro el simbolo")

        except TypeError:
            return apology("NO se encontro el simbolo")

        return render_template("quoted.html", accion=accion)

    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Registrar usuario
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Introduce nombre de usuario", 400)

        if not request.form.get("password"):
            return apology("introduce contrasena", 400)

        if not request.form.get("confirmation"):
            return apology("INtroduszca confirmacion", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("password y confirmacion no son iguales", 400)

        a = db.execute("SELECT username FROM users WHERE username = :username", username=request.form.get("username"))
        hash1 = generate_password_hash(request.form.get("password"))
        try:
            db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",
                        username=request.form.get("username"), hash=hash1)
        except:
            return apology("El username ya existe", 400)

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Vender acciones
    if request.method == "POST":
        if not request.form.get("shares") or int(request.form.get("shares")) <= 0:
            return apology("numero invalido", 400)
        if not request.form.get("symbol"):
            return apology("Introduzca la accion", 400)
        num = db.execute("SELECT shares FROM portfolio WHERE id=:id and stock=:stock",
                        id=session["user_id"], stock=request.form.get("symbol"))
        total = db.execute("SELECT total FROM portfolio WHERE id=:id and stock=:stock",
                        id=session["user_id"], stock=request.form.get("symbol"))
        if num[0]["shares"] < int(request.form.get("shares")):
            return apology("No tienes acciones suficientes", 400)
        else:
            lookedup = lookup(request.form.get("symbol"))
            value = lookedup["price"]*int(request.form.get("shares"))
            # Actualizamos las transacciones/ventas
            shares1 = int(request.form.get("shares"))
            transaction = db.execute("INSERT INTO transactions (id, worth, shares, symbol, purchase, price) VALUES(:id, :worth, :shares, :symbol, :purchase, :price)",
                                    id=session["user_id"], worth=value, shares=shares1, symbol=lookedup["symbol"], purchase="sale", price=lookedup['price'])
            # Actualizamos la cartera/ portfolio
            new_shares = num[0]["shares"]-int(request.form.get("shares"))
            new_total = total[0]["total"]-value
            if new_shares == 0:
                db.execute("DELETE FROM portfolio WHERE id=:id and stock=:symbol",
                            id=session["user_id"], symbol=request.form.get("symbol"))
            else:
                db.execute("UPDATE portfolio SET shares=:shares, total=:total WHERE id=:id and stock=:symbol",
                            shares=new_shares, total=new_total, id=session["user_id"], symbol=lookedup["symbol"])
            # Determinamos el nuevo salfo del usuario en la tabla
            cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
            new_cash = cash[0]['cash'] + value
            db.execute("UPDATE users SET cash = :value WHERE id = :id", value=new_cash, id=session["user_id"])
        return render_template("sold.html", cash=usd(new_cash), total=usd(value), shares=shares1, symbol=lookedup["symbol"], price=lookedup['price'])

    else:
        stocks = db.execute("SELECT stock FROM portfolio WHERE id=:id", id=session["user_id"])
        names = []
        for item in stocks:
            names.append(item["stock"])
        return render_template("sell.html", names=names)

def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)

# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
