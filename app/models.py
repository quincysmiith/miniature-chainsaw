from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    client = db.Column(db.String(120))


class LineItem(db.model):
    id = db.Column(db.Integer, primary_key=True)
    stage = db.Column(db.String(20))
    description = db.Column(db.String(500))
    reason = db.Column(db.String(120))
    estimate = db.Column(db.Integer)
    comments = db.Column(db.String(120))
    rate = db.Column(db.Integer)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def line_total(self):
        return self.estimate * self.rate
