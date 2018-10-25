from app import db

class Form(db.Model):
    __tablename__ = 'form'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    income = db.Column(db.Float)
    last_visit_date = db.Column(db.Date)
    lat = db.Column(db.Float)

    def __repr__(self):
        return '<id {}>'.format(self.id)