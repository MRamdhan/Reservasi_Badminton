from flask import Flask, render_template, session, redirect, url_for
from controllers.booking import booking
from controllers.auth import auth
from controllers.admin import admin
from database import db
from utils.status_checker import update_booking_status



from models import (
    User,
    Lapangan,
    Booking
)

from controllers.auth import auth


app=Flask(__name__)

app.secret_key = "badminton_secret"

app.config["SQLALCHEMY_DATABASE_URI"] = \
"mysql+pymysql://root:@localhost/badminton_db"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False



db.init_app(app)

app.register_blueprint(auth)

app.register_blueprint(booking)

app.register_blueprint(admin)

@app.route("/")

def home():
    update_booking_status()
    data=Lapangan.query.all()

    return render_template(
        "index.html",
        lapangan=data
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
            url_for("home")
    )
    

if __name__=="__main__":


    with app.app_context():

        db.create_all()

    app.run(
        debug=True
    )
