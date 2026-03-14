from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "admin123"  # VULNERABILITY: hardcoded weak secret

DB = "craftyrafty.db"

def get_db():
    return sqlite3.connect(DB)

@app.route("/")
def index():
    return render_template("index.html")

# VULNERABILITY: SQL Injection
@app.route("/products")
def products():
    search = request.args.get("search", "")
    conn = get_db()
    query = f"SELECT * FROM products WHERE name LIKE '%{search}%'"
    results = conn.execute(query).fetchall()
    conn.close()
    return render_template("products.html", products=results, search=search)

# VULNERABILITY: No rate limiting on login
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        user = conn.execute(
            f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        ).fetchone()
        conn.close()
        if user:
            session["user"] = username
            return redirect("/products")
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)