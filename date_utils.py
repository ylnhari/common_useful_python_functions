"""Date Utility Functions."""

def get_curr_date_and_time():
    """
        Function to fetch current date and time
        return(str):
            data and time as a string
    """
    from datetime import datetime, date
    return date.today().strftime("%d/%m/%Y") + " " + datetime.now().strftime("%H:%M:%S") # here we fetched date and time seperately
    
    # also we can use the following code to generate date in different formats.
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    
    # dd-mm-YY_H:M:S
    dt_string = now.strftime("%d-%m-%Y_%H:%M:%S")
    print("date and time =", dt_string)


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
    
    
def convert_pandas_col_to_datetime (df, col_name):
    """
    Parameters
        df (pandas.DataFrame object): dataframe with date column in it
        col_name (str): Name of the column.
    return
        df (pandas.DataFrame object)
    """
    df.loc[:,col_name] = pd.to_datetime(df[col_name])
    return df


def add_or_subtract_minutes_days_hours_seconds_to_pandas_col(df, col_name, no_of_min):
    """Add/Subtract minutes/hours/seconds from a datetime column
    Parameters
        df (pandas.DataFrame object): dataframe with date column in it
        col_name (str): Name of the column.
    return
        df (pandas.DataFrame object)
    """
    minutes = pd.Timedelta (no_of_min, unit 'minutes') # similarly we can do it for seconds, hours (subraction). 
    df[col_name] = (df[col_name]) - minutes
    days = timedelta(days = 730)
    df[col_name] = (df[col_name]) - days
    # we can also use pd.DateOffset(days=180)
    return df
