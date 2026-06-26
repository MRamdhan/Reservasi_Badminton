from database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    password = db.Column(db.String(255), nullable=False)
    telepon = db.Column(db.String(20))
    role = db.Column(db.String(20))
    
    bookings = db.relationship("Booking", backref="user", lazy=True)

    def __init__(self, nama, password, telepon):
        self.nama = nama
        self.password = password
        self.telepon = telepon

    def login(self, password):
        return self.password == password