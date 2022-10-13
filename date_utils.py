"""Date Utility Functions."""

def get_curr_date_and_time():
    """
        Function to fetch current date and time
        return(str):
            data and time as a string
    """
    from datetime import datetime, date
    return date.today().strftime("%d/%m/%Y") + " " + datetime.now().strftime("%H:%M:%S")


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


def add_minutes_to_pandas_col(df, col_name, no_of_min):
    """Add/Subtract minutes/hours/seconds from a datetime column
    Parameters
        df (pandas.DataFrame object): dataframe with date column in it
        col_name (str): Name of the column.
    return
        df (pandas.DataFrame object)
    """
    minutes = pd.Timedelta (no_of_min, unit 'minutes') # similarly we can do it for seconds, hours (subraction). 
    df[col_name] = (df[col_name]) - minutes
    return df
