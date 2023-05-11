from uncertainty import app
from uncertainty import indexes

@app.route('/uncertainty.api/EUI')
def get_summary_index():
    indexes.summary_index()

@app.route('/uncertainty.api/<area_name>')
def get_area_index(area_name):
    res = indexes.area_index_by_area_name(area_name)
    return res

@app.route('/uncertainty.api/EUI/date-range')
def get_summary_index_by_dateRange():
    pass

@app.route('/uncertainty.api/<area_name>/date-range')
def get_area_index_by_date_range():
    pass

@app.route('/uncertainty.api/EUI/cycle')
def get_EUI_cycle():
    pass

@app.route('/uncertainty.api/<area>/cycle')
def get_area_cycle():
    pass

@app.route('/uncertainty.api/basic')
def get_basic_economic_index():
    pass

@app.route('/uncertainty.api/basic/<area>')
def get_basic_economic_index_by_area():
    pass