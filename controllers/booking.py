from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from database import db

from models import (
    Lapangan,
    Booking,
)

from datetime import date, datetime

from utils.status_checker import update_booking_status

booking = Blueprint(
    "booking",
    __name__
)

@booking.route("/detail/<int:id>")
@booking.route("/detail/<int:id>/<tanggal>")
def detail(id, tanggal=None):
    update_booking_status()
    lapangan = Lapangan.query.get(id)
    tanggal = request.args.get("tanggal")

    if tanggal:
        tanggal_pilih = datetime.strptime(tanggal, "%Y-%m-%d").date()
    else:
        tanggal_pilih = date.today()
        
    data_booking = Booking.query.filter_by(
        lapangan_id=id,
        tanggal=tanggal_pilih
    ).all()

    timeline=[]

    for jam in range(8,22):
        waktu = f"{jam:02d}:00"
        status="kosong"

        for b in data_booking:
            mulai = b.jam_mulai.hour
            selesai = b.jam_selesai.hour

            if mulai <= jam < selesai:
                status=b.status

        timeline.append({
            "jam":waktu,
            "status":status
        })

    return render_template(
        "detail_lapangan.html",
        lapangan=lapangan,
        timeline=timeline,
        tanggal = tanggal_pilih
    )
    
@booking.route("/booking/<int:id>", methods=["POST"])
def buat_booking(id):
    if "user_id" not in session:
        return redirect(
            url_for("auth.login")
        )

    mulai = request.form.get("mulai")
    selesai = request.form.get("selesai")
    tanggal = request.form.get("tanggal")

    cek = Booking.query.filter(
        Booking.lapangan_id == id,
        Booking.tanggal == tanggal,
        Booking.status.in_(
            [
                "pending",
                "approved",
                "play"
            ]
        ),

        Booking.jam_mulai < selesai,

        Booking.jam_selesai > mulai
    ).first()

    if cek:
        flash(
            "Jam Tersebut Sudah Dibooking, Silahkan Pilih Jam Lainnya",
            "danger"
        )

        return redirect(
            url_for(
                "booking.detail",
                id=id,
                tanggal=tanggal
            )
        )

    booking = Booking(
        session["user_id"],
        id,
        tanggal,
        mulai,
        selesai
    )

    db.session.add(booking)
    db.session.commit()

    flash(
        "Reservasi berhasil dibuat, menunggu konfirmasi admin.",
        "success"
    )

    return redirect(
        url_for(
            "booking.detail",
            id=id,
            tanggal=tanggal
        )
    )