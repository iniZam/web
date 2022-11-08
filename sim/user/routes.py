# from flask import Flask, render_template, redirect, request, url_for, Blueprint, flash
# from sim.admin.forms import login_admin
# from sim.mahasiswa.forms import Orang,login_org,Edit_org,pengaduan,edit_pengaduan,agenda_info
# from sim.models import Tadmin
# from sim import db, bcrypt,app
# from flask_login import login_user,current_user,logout_user,login_required


# radmin=Blueprint('radmin', __name__)

# @radmin.route("/")
# def rumah():
#     return render_template("rumah.html")

# @radmin.route("/tentang")
# def tentang():
#     return render_template("tentang.html")

# @radmin.route("/daftar", methods=['GET', 'POST'])
# def daftar():
#     form=Orang()
#     if (form.validate_on_submit()):
#         pas_hash = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')# ini adalah variabel yang akan mengamankan pasword yang dimasukan dan nanti pasword yang sudah di amankan akan di panggil di line selanjutnya
#         add_mahasiswa=Tadmin(npm=form.npm.data, nama=form.nama.data, email=form.email.data, password=pas_hash, kelas=form.kelas.data, alamat=form.alamat.data)
#         db.session.add(add_mahasiswa)
#         db.session.commit()
#         flash(f'Akun- {form.npm.data} berhasil daftar', 'primary')
      
#         return redirect(url_for('radmin.login'))
#     return render_template("daftar.html", form=form)

# @radmin.route("/akunadmin")
# @login_required # ini akan membuat halamanya hanya bisa dibuka saat user sudah login
# def akunadmin():
#     return render_template('akunadmin.html')