from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.filters.hp_filter import hpfilter

def seasonal_adjustment(timeseries):
    res = seasonal_decompose(x=timeseries, period=12, extrapolate_trend='freq')
    return res.trend

def get_trend(timeseries, lambda_value):
    hpfilter(timeseries, lambda_value)

def get_cycle(timeseries):
    cycle_yearly , trend_yearly = hpfilter(timeseries, 100)
    cycle, trend = hpfilter(trend_yearly, 14.400)
    return cycle