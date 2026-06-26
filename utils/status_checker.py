from datetime import datetime,date
from database import db
from models.booking import Booking


def update_booking_status():
    sekarang=datetime.now()
    hari_ini = date.today()
    bookings=Booking.query.all()

    for b in bookings:
        if b.tanggal != hari_ini:
            continue

        if b.status == "approved":
            if (
                b.jam_mulai <= sekarang.time()
                and
                sekarang.time() < b.jam_selesai
            ):
                b.status="play"
        elif b.status == "play":
            if sekarang.time() >= b.jam_selesai:
                b.status="finished"

    db.session.commit()