from importlib.machinery import FileFinder
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,EmailField, SelectField #ini akan mengimport tipe data
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from sim.models import Tmahasiswa
from flask_login import current_user
from flask_wtf.file import FileAllowed,FileField




class Admin(FlaskForm):# ini kelas tambahannya
    npm = StringField('NPM', validators=[DataRequired(),Length(min=10,max=15)])#ini untuk deklarasi tipe data dan validasi untuk minta data dimasukan dengan panjang tertentu 
    nama = StringField('Nama', validators=[DataRequired()])#ini adalah variabel dan StringField itu tipe datanya
    email = EmailField('alamat Email', validators=[DataRequired(),Email()])# yang string itu labelnya    
    password = PasswordField('password',validators=[DataRequired(),Length(min=6,max=10)])#ini atribut baru yang akan menampung pasword
    konfir_pass=PasswordField('konfirmasi password',validators=[DataRequired(),EqualTo("password")])# ini untuk konfimasi passwod dan equal
    alamat = TextAreaField('alamat', validators=[DataRequired()])
    submit = SubmitField('tambah') # kalo yang ini itu tombolnya

    #catatan : untuk data yang dimasukan di sini harus sama dengan yang di html kalo jumlahnya tidak sama nanti dia tidak mau keluar 


    #ini akan mengecek npmnya
    def validate_npm(self,npm):
        ceknpm= Tmahasiswa.query.filter_by(npm=npm.data).first()
        if ceknpm:
            raise ValidationError("ganti NPM da yang ini ada yang so pake")
    # cek email
    def validate_email(self,email):
        cekemail= Tmahasiswa.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError("ganti email da yang ini ada yang so pake")

class login_admin(FlaskForm):
    npm = StringField('NPM', validators=[DataRequired()])#ini untuk deklarasi tipe data dan validasi untuk minta data dimasukan dengan panjang tertentu 
    password = PasswordField('pasword',validators=[DataRequired()])
    submit =SubmitField('Login')

class Tulisan (FlaskForm):
    judul = StringField('judul',validators=[DataRequired()])
    isi = StringField('isi',validators=[DataRequired()])
    submit =SubmitField('Login')
    