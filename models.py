from _config import app, db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(20), default='210x210')
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    im1 = db.Column(db.LargeBinary, default='')


class Item2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(20), default='210x210')
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    im1 = db.Column(db.LargeBinary, default=b'')
    im2 = db.Column(db.BLOB, default='')