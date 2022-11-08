from flask import Flask, render_template, redirect, request, url_for, Blueprint, flash
from sim.admin.forms import Admin,Tulisan,login_admin,Edit_org, editTulisan
from sim.models import Tadmin, Ttulisan
from sim import db, bcrypt,app,ALLOWED_EXTENSIONS
from flask_login import login_user,current_user,logout_user,login_required
import os
from werkzeug.utils import secure_filename
import secrets
from PIL import Image



radmin=Blueprint('radmin', __name__)

@radmin.route("/")
def rumah():
    tampilan = Ttulisan.query.all()
    return render_template("rumah.html",info=tampilan)
@radmin.route("/tentang")
def tentang():
    return render_template("tentang.html")
@radmin.route("/prolog")
def prolog():
    return render_template("prolog.html")
@radmin.route("/visimisi")
def visimisi():
    return render_template("visi-misi.html")
@radmin.route("/tujuan")
def tujuan():
    return render_template("tujuan.html")
@radmin.route("/sejarah")
def sejarah():
    return render_template("sejarah.html")

@radmin.route("/berita")
def berita():
    tampilan = Ttulisan.query.all()
    return render_template("berita.html",info = tampilan)

@radmin.route("/opini")
def opini():
    tampilan = Ttulisan.query.all()
    return render_template("opini.html",info = tampilan)
@radmin.route("/sastra")
def sastra():
    tampilan = Ttulisan.query.all()
    return render_template("sastra.html",info = tampilan)

@radmin.route("/essay")
def essay():
    # fil = "Essay"
    tampilan = Ttulisan.query.all()
    return render_template("essay.html",info=tampilan)

@radmin.route("/esay/<int:ed_id>/detail", methods=['GET','POST'])
def detil(ed_id):
    dt_tulisan=Ttulisan.query.get_or_404(ed_id)
    return render_template('detail_laporan.html',dt_tulisan=dt_tulisan)



@radmin.route("/daftar", methods=['GET', 'POST'])
def daftar():
    form=Admin()
    if (form.validate_on_submit()):
        pas_hash = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')# ini adalah variabel yang akan mengamankan pasword yang dimasukan dan nanti pasword yang sudah di amankan akan di panggil di line selanjutnya
        add_mahasiswa=Tadmin(nama=form.nama.data, email=form.email.data, password=pas_hash)
        db.session.add(add_mahasiswa)
        db.session.commit()
        flash(f'Akun- {form.nama.data} berhasil daftar', 'primary')
      
        return redirect(url_for('radmin.login'))
    return render_template("daftar.html", form=form)

@radmin.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('radmin.rumah'))
    form=login_admin()
    if form.validate_on_submit():
        cek= Tadmin.query.filter_by(email=form.email.data).first()
        if cek and bcrypt.check_password_hash(cek.password, form.password.data):
            login_user(cek)
            flash('Selamat Datang Kembali', 'warning')
            return redirect(url_for('radmin.rumah'))
         
       
        else:
            flash('Login Gagal, Periksa email dan Password kembali', 'danger')
            return redirect(url_for('radmin.login'))
    
    
    return render_template ("login.html",form=form)


@radmin.route("/akun")
@login_required # ini akan membuat halamanya hanya bisa dibuka saat user sudah login
def akun():
    return render_template('akun.html')

@radmin.route("/keluar")
def keluar():
    logout_user()
    return redirect(url_for('radmin.login'))

@radmin.route("/editprofil", methods=['GET','POST'])
@login_required
def editpfofil():
    form = Edit_org()
    if form.validate_on_submit():# ini adalah sintak untuk mengupdate data yang akan dimasukan ke dalam database
        current_user.nama=form.nama.data
        current_user.email=form.email.data
        sandi = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        current_user.password=sandi
        db.session.commit()
        flash('Data berhasil di rubah ','warning ')
        return redirect(url_for('radmin.editpfofil'))
    elif request.method=="GET":# ini sintak untuk menampilkan data ke dalam database
        form.nama.data=current_user.nama 
        form.email.data=current_user.email
        form.password.data=current_user.password
        
    return render_template ('edit.html',form=form)

#simpan foto 


@radmin.route("/tambah_tulisan", methods=['GET','POST'])
@login_required
def tambah_tulisan():
    
    form = Tulisan()
    # isi = allowed_file(form.isi.data)
    if form.validate_on_submit(): 
        add_laporan = Ttulisan(isi=form.isi.data,judul=form.judul.data,kategori=form.kategori.data)
        db.session.add(add_laporan)
        db.session.commit()
        flash('tulisan telah di post ','warning ')
        return redirect(url_for('radmin.tambah_tulisan'))        
       
    return render_template('tambah_tulisan.html',form=form)

@radmin.route("/edit_tulisan/<int:ed_id>/update", methods=['GET','POST'])
@login_required # ini akan membuat halamanya hanya bisa dibuka saat user sudah login
def edit_tulisan(ed_id):# ed_id adalah id yang ada di database dan data yang di edit akan berdasarkan id nya
    form = editTulisan()
    dt_tulisan=Ttulisan.query.get_or_404(ed_id)
    if request.method=="GET":# ini adalah sytak untuk menampilkan data 
        form.judul.data=dt_tulisan.judul
        form.kategori.data=dt_tulisan.kategori
        form.isi.data=dt_tulisan.isi
    elif form.validate_on_submit():# ini sytak untuk mengubah di dalam database
        dt_tulisan.judul=form.judul.data
        dt_tulisan.kategori=form.kategori.data
        dt_tulisan.isi=form.isi.data
        db.session.commit()
        flash('Tulisan telah direvisi :)','warning')
        return redirect(url_for('radmin.rumah'))
    return render_template('editlapor.html',form=form)

@radmin.route("/hapus/<ed_id>", methods=['GET','POST'])
@login_required # ini akan membuat halamanya hanya bisa dibuka saat user sudah login
def hapus(ed_id):
    hapus =Ttulisan.query.get(ed_id)
    db.session.delete(hapus)
    db.session.commit()
    flash('Sudah di hapus ','warning')
    return redirect(url_for('radmin.essay'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower in ALLOWED_EXTENSIONS

@app.route("/test", methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No File Part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No Selected File')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename = filename))
        
    return render_template('CobaInput.html')



    



# ini kabawa ni UAS punya
# @radmin.route("/posting", methods=['GET','POST'])
# @login_required
# def agenda_inf():
#     form = agenda_info()
#     if form.validate_on_submit(): 
#         add_agenda = Agenda_info(subjek=form.subjek.data,caption=form.caption.data)
#         db.session.add(add_agenda)
#         db.session.commit()
#         flash('Sudah di posting ','warning ')
#         return redirect(url_for('radmin.agenda_inf'))  
#     return render_template('tambahagenda.html',form=form)#, info_agenda=info_agenda)

# @radmin.route("/agenda", methods=['GET','POST'])
# def informasi():
#     info_agenda = Agenda_info.query.all()
    
#     return render_template("agenda_info.html",info=info_agenda)