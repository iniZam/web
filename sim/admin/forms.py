from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,PasswordField,EmailField, SelectField #ini akan mengimport tipe data
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from sim.models import Tadmin,Ttulisan 
from flask_login import current_user
from flask_wtf.file import FileAllowed,FileField


class Admin(FlaskForm):# ini kelas tambahannya
    nama = StringField('Nama', validators=[DataRequired()])#ini adalah variabel dan StringField itu tipe datanya
    email = EmailField('alamat Email', validators=[DataRequired(),Email()])# yang string itu labelnya    
    password = PasswordField('password',validators=[DataRequired(),Length(min=6,max=10)])#ini atribut baru yang akan menampung pasword
    konfir_pass=PasswordField('konfirmasi password',validators=[DataRequired(),EqualTo("password")])# ini untuk konfimasi passwod dan equal
    submit = SubmitField('tambah') # kalo yang ini itu tombolnya

    #catatan : untuk data yang dimasukan di sini harus sama dengan yang di html kalo jumlahnya tidak sama nanti dia tidak mau keluar 



    # cek email
    def validate_email(self,email):
        cekemail= Tadmin.query.filter_by(email=email.data).first()
        if cekemail:
            raise ValidationError("ganti email da yang ini ada yang so pake")

class login_admin(FlaskForm):
    email = StringField('email', validators=[DataRequired()])#ini untuk deklarasi tipe data dan validasi untuk minta data dimasukan dengan panjang tertentu 
    password = PasswordField('pasword',validators=[DataRequired()])
    submit =SubmitField('Login')

class Tulisan(FlaskForm):
    judul = StringField("judul",validators=[DataRequired()])
    kategori = SelectField ( "Kategori Tulisan",choices=[('Essay','Essay'),('Opini','Opini'),('Sastra','Sastra'),('berita','berita')],validators=[DataRequired()])
    isi = TextAreaField("Isi",validators=[DataRequired()])
    submit =SubmitField('posting')

    def validate_email(self,judul):
        cekjudul= Tadmin.query.filter_by(judul=judul.data).first()
        if cekjudul:
            raise ValidationError("ganti judul da yang ini ada yang so pake")
    
class Edit_org(FlaskForm):# ini kelas tambahannya
    
    nama = StringField('Nama', validators=[DataRequired()])#ini adalah variabel dan StringField itu tipe datanya
    email = EmailField('alamat Email', validators=[DataRequired(),Email()])# yang string itu labelnya    
    password = PasswordField('password',validators=[DataRequired(),Length(min=6,max=10)])#ini atribut baru yang akan menampung pasword
    konfir_pass=PasswordField('konfirmasi password',validators=[DataRequired(),EqualTo("password")])# ini untuk konfimasi passwod dan equal
    submit = SubmitField('Ubah ') # kalo yang ini itu tombolnya
    
    #catatan : untuk data yang dimasukan di sini harus sama dengan yang di html kalo jumlahnya tidak sama nanti dia tidak mau keluar 

   
    # cek email
    def validate_email(self,email):
        if email.data != current_user.email:
            cekemail= Tadmin.query.filter_by(email=email.data).first()
            if cekemail:
                raise ValidationError("ganti email da yang ini ada yang so pake")

class editTulisan(FlaskForm):
    judul = StringField("Judul",validators=[DataRequired()])
    kategori = SelectField ( "Kategori Tulisan",choices=[('Essay','Essay'),('Opini','Opini'),('Sastra','Sastra'),('berita','berita')],validators=[DataRequired()])
    isi = TextAreaField("Isi",validators=[DataRequired()])
    submit =SubmitField('Update')

    def validate_email(self,judul):
        cekjudul= Tadmin.query.filter_by(judul=judul.data).first()
        if cekjudul:
            raise ValidationError("ganti judul da yang ini ada yang so pake")