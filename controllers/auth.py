from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from database import db

from models.user import User

auth = Blueprint(
    "auth",
    __name__,
)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nama = request.form.get("nama")
        password = request.form.get("password")
        telepon = request.form.get("telepon")    
        user = User(
            nama=nama,
            password=password,
            telepon=telepon
        )
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(
            url_for("auth.login")
        )
    
    return render_template(
        "register.html"
    )
    
@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        nama = request.form.get("nama")
        password = request.form.get("password")
        
        user = User.query.filter_by(
            nama = nama
        ).first()
        
        if user and user.login(password):
            session["user_id"] = user.id
            session["nama"] = user.nama
            session["role"] = user.role
            if user.role == "admin":
                return redirect(
                    url_for("admin.dashboard")
                )
            else:
                return redirect(
                    url_for("home")
                )
    
    return render_template(
        "login.html"
    )