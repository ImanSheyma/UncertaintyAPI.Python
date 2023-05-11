from uncertainty import models, db

def summary_index():
    areas = db.session.query(models.Economic_area)
    for area in areas:
        area_index(area)


def area_index_by_area_name(area_name):
    area = db.session.query(models.Economic_area)\
        .where(models.Economic_area.area_name == area_name).first()
    return area_index(area)

def area_index(area):
    questions = db.session.query(models.Question).where(models.Question.area_id == area.id).all()
    area_indexes = dict()
    for q in questions:
        question_indexes = get_uncertainty_index_by_question(q)
        for index in question_indexes:
            val = area_indexes.get(index.date)
            if val == None:
                val = 0
            area_indexes.update({index.date : val + index.value})
    return area_indexes

def summary_index_by_date_range(date_start, date_end):
    pass

def area_index_by_date_range(area, date_start, date_end):
    pass

def get_uncertainty_index_by_question(question):
    return db.session.query(models.Uncertainty_index)\
        .where(models.Uncertainty_index.question_id == question.id).all()