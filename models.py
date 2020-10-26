from app import db

class Particles(db.Model):
    __tablename__ = 'particles'

    id = db.Column(db.Integer, primary_key=True)
    TimeStamp = db.Column(db.DateTime())
    pm1_0cf1 = db.Column(db.Numeric())
    pm2_5cf1 = db.Column(db.Numeric())
    pm10cf1 = db.Column(db.Numeric())
    pm1_0 = db.Column(db.Numeric())
    pm2_5 = db.Column(db.Numeric())
    pm10 = db.Column(db.Numeric())
    n0_3 = db.Column(db.Numeric())
    n0_5 = db.Column(db.Numeric())
    n1_0 = db.Column(db.Numeric())
    n2_5 = db.Column(db.Numeric())
    n5_0 = db.Column(db.Numeric())
    n10 = db.Column(db.Numeric())


    def __init__(self, pm1_0cf1, pm2_5cf1, pm10cf1, pm1_0, pm2_5, pm10, n0_3, n0_5, n1_0, n2_5, n5_0, n10, TimeStamp):
        self.pm1_0cf1 = pm1_0cf1
        self.pm2_5cf1 = pm2_5cf1
        self.pm10cf1 = pm10cf1
        self.pm1_0 = pm1_0
        self.pm2_5 = pm2_5
        self.pm10 = pm10
        self.n0_3 = n0_3
        self.n0_5 = n0_5
        self.n1_0 = n1_0
        self.n2_5 = n2_5
        self.n5_0 = n5_0
        self.n10 = n10
        self.TimeStamp = TimeStamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id,
            'TimeStamp': self.TimeStamp,
            'pm1_0cf1': self.pm1_0cf1,
            'pm2_5cf1': self.pm2_5cf1,
            'pm10cf1': self.pm10cf1,
            'pm1_0': self.pm1_0,
            'pm2_5': self.pm2_5,
            'pm10': self.pm10,
            'n0_3': self.n0_3,
            'n0_5': self.n0_5,
            'n1_0': self.n1_0,
            'n2_5': self.n2_5,
            'n5_0': self.n5_0,
            'n10': self.n10
        }