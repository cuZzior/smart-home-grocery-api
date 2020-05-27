from db import db


class GroceryModel(db.Model):
    __tablename__ = 'groceries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    exp_date = db.Column(db.String(250))

    def __init__(self, name, exp_date):
        self.name = name
        self.exp_date = exp_date

    def json(self):
        return {'id': self.id, 'name': self.name, 'exp_date': self.exp_date}

    @classmethod
    def find_by_id(cls, db_id):
        return cls.query.filter_by(id=db_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
