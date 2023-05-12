from uncertainty import app
from flask import request
from uncertainty import indexes
from uncertainty import statistical_tools as st

@app.route('/uncertainty.api/EUI')
def get_summary_index():
    uncertainty_indexes = indexes.summary_index()
    seasonal_adj = request.args.get("seasonal_adj")
    if seasonal_adj:
        return st.seasonal_adjustment(uncertainty_indexes).to_dict()
    return uncertainty_indexes.to_dict()

@app.route('/uncertainty.api/<area_name>')
def get_area_index(area_name):
    area_indexes = indexes.area_index_by_area_name(area_name)
    seasonal_adj = request.args.get("seasonal_adj")
    if seasonal_adj:
        return st.seasonal_adjustment(area_indexes).to_dict()
    return area_indexes.to_dict()

@app.route('/uncertainty.api/EUI/date-range')
def get_summary_index_by_dateRange():
    pass

@app.route('/uncertainty.api/<area_name>/date-range')
def get_area_index_by_date_range():
    pass

@app.route('/uncertainty.api/EUI/cycle')
def get_EUI_cycle():
    EUI = indexes.summary_index()
    return st.get_cycle(EUI).to_dict()

@app.route('/uncertainty.api/<area_name>/cycle')
def get_area_cycle(area_name):
    UI = indexes.area_index_by_area_name(area_name)
    return st.get_cycle(UI).to_dict()

@app.route('/uncertainty.api/basic')
def get_basic_economic_index():
    pass

@app.route('/uncertainty.api/basic/<area>')
def get_basic_economic_index_by_area():
    pass