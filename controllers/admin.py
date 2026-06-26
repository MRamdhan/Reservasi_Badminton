from flask import Blueprint, render_template, redirect, url_for, session, request
from database import db
from models import Booking,User
from werkzeug.utils import secure_filename
from models.lapangan import Lapangan
import os

admin = Blueprint(
    "admin",
    __name__
)

@admin.route("/admin")
def dashboard():
    if session.get("role") != "admin":
        return "Akses Ditolak"
    
    data = Booking.query.join(User).filter(Booking.status.notin_(["finished", "cancelled"])).all()
    return render_template(
        "admin.html",
        booking = data
    )

@admin.route("/admin/acc/<int:id>")
def acc(id):
    booking = Booking.query.get(id)
    
    booking.status = "approved"
    
    db.session.commit()
    
    return redirect(url_for("admin.dashboard"))


@admin.route("/admin/batal/<int:id>")
def batal(id):
    booking = Booking.query.get(id)
    
    booking.status = "cancelled"
    
    db.session.commit()
    
    return redirect(url_for("admin.dashboard"))

@admin.route("/admin/history")
def history():
    if session.get("role") != "admin":
        return "Akses Ditolak"
    
    data = Booking.query.filter(Booking.status.in_(["finished", "cancelled"])).all()
    
    return render_template(
        "history.html",
        booking = data
    )
    
@admin.route("/admin/play/<int:id>")
def play(id):
    booking = Booking.query.get(id)
    booking.status="play"
    db.session.commit()

    return redirect(
        url_for(
            "admin.dashboard"
        )
    )

@admin.route("/admin/selesai/<int:id>")
def selesai(id):
    booking = Booking.query.get(id)
    booking.status="finished"
    db.session.commit()

    return redirect(
        url_for(
            "admin.dashboard"
        )

    )
    
@admin.route("/admin/lapangan")
def lapangan():
    data = Lapangan.query.all()
    
    return render_template("lapang.html", lapangan=data, edit = None)

@admin.route("/admin/lapangan/tambah", methods = ["POST"])
def tambah_lapangan():
    nama = request.form["nama"]
    harga = request.form["harga"]
    deskripsi = request.form["deskripsi"]
    
    data = Lapangan(
        nama = nama,
        harga = harga,
        deskripsi = deskripsi
    )
    
    db.session.add(data)
    db.session.commit()
    
    return redirect(url_for("admin.lapangan"))

@admin.route("/admin/lapangan/edit/<int:id>")
def halaman_edit(id):
    data = Lapangan.query.get(id)
    
    semua = Lapangan.query.all()
    
    return render_template("lapang.html", lapang = semua, edit = data)

@admin.route("/admin/lapangan/edit/<int:id>", methods = ["POST"])
def edit_lapangan(id):
    data = Lapangan.query.get(id)
    
    data.nama = request.form["nama"]
    data.harga = request.form["harga"]
    data.deskripsi = request.form["deskripsi"]
    
    db.session.commit()
    
    return redirect(url_for("admin.lapangan"))

@admin.route("/admin/lapangan/hapus/<int:id>")
def hapus_lapangan(id):
    data = Lapangan.query.get(id)
    
    db.session.delete(data)
    
    db.session.commit()
    
    return redirect(url_for("admin.lapangan"))