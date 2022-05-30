from _config import app, db

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    width = db.Column(db.Integer, default=210)
    height = db.Column(db.Integer, default=210)
    materials = db.Column(db.String(200))
    about = db.Column(db.String(100))
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    images = db.relationship('Image', backref='item')



class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    is_title = db.Column(db.String(100), default=False)
    link = db.Column(db.String(100), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
