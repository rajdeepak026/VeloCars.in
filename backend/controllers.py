from flask import Flask, render_template, redirect, request, session
from flask import current_app as app 
from .models import *

@app.route("/")
def index():
    return render_template("landing-page.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            if user.password == password:
                if user.type == "admin":
                    return redirect("/admin")
                else:
                    return redirect(f"/user/{user.id}")
            else:
                return render_template("login.html", error="Invalid password")
        else:
            return render_template("login.html", error="User not found")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        mobile_no = request.form.get("mobile_no")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match")

        this_user = User.query.filter_by(email=email).first()
        if this_user:
            return render_template("signup.html", error="User already exists")

        new_user = User(fullname=fullname, email=email, password=password, mobile_no=mobile_no)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")

    return render_template("signup.html")


@app.route("/landing")
def landing():
    return render_template("landing-page.html")

@app.route("/admin")
def admin():
    admin_user = User.query.filter_by(type="admin").first()
    return render_template("admin-dash.html", admin_user=admin_user)

@app.route("/user/<int:user_id>")
def user_dash(user_id):
    user = User.query.get(user_id)
    return render_template("user-dash.html", user=user)
