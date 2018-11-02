from app import db

class Form(db.Model):
    __tablename__ = 'form'

    key = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    last_visit_date = db.Column(db.Date)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    school_length = db.Column(db.Integer)
    school_name = db.Column(db.String())
    people_in_house = db.Column(db.String())
    why_not_in_school = db.Column(db.String())
    dreams = db.Column(db.String())
    most_loved = db.Column(db.String())
    potential_abuser = db.Column(db.String())
    what_abuse = db.Column(db.String())
    phone = db.Column(db.String())
    address = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
