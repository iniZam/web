from datetime import datetime
from sim import db,login_manager
from flask_login import UserMixin

#from sim import db
# from sim.models import Tadmin
# db.create_all()

@login_manager.user_loader
def load_user(id):
    return Tadmin.query.get(int(id))

# class Tuser(db.Model,UserMixin): #tambahkan
#     id = db.Column(db.Integer, primary_key=True)
#     npm = db.Column(db.String(15), unique=True, nullable=False)
#     nama = db.Column(db.String(20) , nullable=False)
#     email = db.Column(db.String(20),unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     alamat = db.Column(db.String(100), nullable=False)
#     foto = db.Column(db.String(20), nullable=False, default='default.jpg')
#     pengaduans = db.relationship('Tpengaduan', backref='mahasiswa')#backref itu relasi/hubungan antar ttabel

#     def __repr__(self):
#         return f"Tuser('{self.npm}', '{self.nama}', '{self.email}', '{self.password}', '{self.kelas}', '{self.alamat}','{self.foto}')"

class Tadmin(db.Model,UserMixin): #tambahkan
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(20) , nullable=False)
    email = db.Column(db.String(20),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # id_tulis = db.relationship('ttulisan', backref='tulisan')#backref itu relasi/hubungan antar ttabel

    def __repr__(self):
        return f"Tadmin('{self.nama}',  '{self.email}', '{self.password}')"
        
class Ttulisan(db.Model,UserMixin):
    id_tulisan= db.Column(db.Integer, primary_key=True)
    judul= db.Column(db.String(100),nullable=False)
    kategori =db.Column(db.String(100), nullable=False)
    isi =db.Column(db.String(10000), nullable=False)
    tgl_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # mahasiswa_id = db.Column (db.Integer, db.ForeignKey('tmahasiswa.id'), nullable=False)

    def __repr__(self):
        return f"Ttulisan('{self.judul}','{self.kategori}', {self.isi}', '{self.tgl_post}')"

