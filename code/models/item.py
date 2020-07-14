from db import db

class ItemModel(db.Model):
    # Creates database name for SQLAlchemy
    __tablename__ = 'items'

    # Creates columns in the SQLAlchemy database
    id = db.Column(db.Integer, primary_key=True) # Unique ID:
    name = db.Column(db.String(80)) # creates name column and limits character to 80
    price = db.Column(db.Float(precision=2)) # creates price column and limits character to 80

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
