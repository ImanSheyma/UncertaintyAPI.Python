import statsmodels.api as sm

def seasonal_adjustment(timeseries):
    return sm.tsa.seasonal_decompose(timeseries, model='additive', period=12)

def get_trend(timeseries, lambda_value):
    pass

def get_cycle(timeseries, lambda_value):
    pass