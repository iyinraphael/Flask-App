from db import db

class StoreModel(db.Model):
    # Creates database name for SQLAlchemy
    __tablename__ = 'stores'

    # Creates columns in the SQLAlchemy database
    id = db.Column(db.Integer, primary_key=True) # Unique ID:
    name = db.Column(db.String(80)) # creates name column and limits character to 80

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name, price):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
