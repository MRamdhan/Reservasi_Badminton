from database import db

class Lapangan(db.Model):
    __tablename__="lapangan"

    id = db.Column(db.Integer, primary_key=True)
    nama=db.Column(db.String(100))
    harga=db.Column( db.Integer)
    deskripsi=db.Column(db.Text)
    status=db.Column(db.String(20))
    bookings = db.relationship("Booking", backref="lapangan", lazy=True)

    def __init__(
        self,
        nama,
        harga,
        deskripsi
    ):

        self.nama=nama
        self.harga=harga
        self.deskripsi=deskripsi
        self.status="tersedia"

    def cek_status(self):

        return self.status
