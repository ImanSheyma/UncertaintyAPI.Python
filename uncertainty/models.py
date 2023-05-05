from uncertainty import db

class Economic_area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(255), nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    questions = db.relationship('Question', backref='economic_area')


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('economic_area.id'), nullable=False)

    indexes = db.relationship('Uncertainty_index', backref='question')


class Uncertainty_index(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    value = db.Column(db.Float, nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)