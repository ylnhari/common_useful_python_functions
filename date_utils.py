"""Date Utility Functions."""


def get_time_difference_from_a_start_date(pandas_series, start_date):
    """
    Parameters
    ----------
        pandas_series (pandas.series object) : each value is pd.datetime dtype
        start_date (pd.datetime dtype) : start datetime from which difference should be calculated
    return
    ------
        (pandas_series) difference from start date in minutes
    """
    return (pandas_series - start_date).apply(lambda x: int(x.total_seconds() / 60))
    
