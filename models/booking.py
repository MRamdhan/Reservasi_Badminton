from database import db


class Booking(db.Model):
    
    __tablename__="booking"
    
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    lapangan_id=db.Column(db.Integer, db.ForeignKey("lapangan.id"))
    tanggal=db.Column(db.Date)
    jam_mulai = db.Column(db.Time)
    jam_selesai = db.Column(db.Time)
    status=db.Column(db.String(20))

    def __init__(
        self,
        user_id,
        lapangan_id,
        tanggal,
        jam_mulai,
        jam_selesai
    ):
        
        self.user_id=user_id
        self.lapangan_id=lapangan_id
        self.tanggal=tanggal
        self.jam_mulai=jam_mulai
        self.jam_selesai=jam_selesai
        self.status="pending"

    def acc(self):
        self.status="approved"

    def mulai_main(self):
        self.status="play"
        
    def selesai(self):
        self.status="selesai"
        
    def batal(self):
        self.status="canceled"
