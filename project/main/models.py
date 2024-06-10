from ..extensions import db

class Contact(db.Model):
    ''' Create an Order table'''
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60))
    mobile = db.Column(db.Integer)
    note = db.Column(db.String(120))

    def __repr__(self):
        return '<Order By: {}, Email: {}, Mobile: {}>'.format(self.full_name, self.email, self.mobile)

