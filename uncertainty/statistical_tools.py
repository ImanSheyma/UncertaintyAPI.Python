import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

def seasonal_adjustment(timeseries):
    res = seasonal_decompose(x=timeseries, period=12, extrapolate_trend='freq')
    return res.trend

def get_trend(timeseries, lambda_value):
    pass

def get_cycle(timeseries, lambda_value):
    pass