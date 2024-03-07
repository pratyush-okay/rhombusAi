import pandas as pd

def is_numeric(col: pd.Series):
    series = col.dropna()
    try:
        # Attempt to convert to numeric first
        return not all(pd.isna(pd.to_numeric(series, errors='coerce')))
    except:
        return False

def is_float(col: pd.Series):
    series = col.dropna()
    try:
        # Check if all values are floating-point numbers
        if pd.to_numeric(series, errors='coerce').notnull().all():
            return True
        else:
            return False
    except:
        return False
    

def is_bool(col: pd.Series):
    series = col.dropna()
    if any(isinstance(value, bool) for value in series):
        return True
    
    # Convert strings "True" and "False" to actual boolean values
    series_lower = series.apply(lambda x: x.lower() if isinstance(x, str) else x)

    # Check if all values are boolean after converting string representations
    if any(value in {"true", "false"} for value in series_lower):
        return True
    
    return False

def is_category(col: pd.Series):
    series = col.dropna()
    if len(series.unique()) / len(series) <= 0.5:  # Example threshold for categorization
        return True
    return False

def is_datetime(col: pd.Series):
    series = col.dropna()
    return any(series.apply(lambda x: pd.to_datetime(x, errors='coerce') is not pd.NaT))

def is_timedelta(col: pd.Series):
    series = col.dropna()
    return any(series.apply(lambda x: pd.to_timedelta(x, errors='coerce') is not pd.NaT))

def is_complex(col: pd.Series):
    series = col.dropna()
    return any(series.apply(lambda x: isinstance(x, complex) or isinstance(x, str) and '+' in x and 'j' in x))

def clean_column(col: pd.Series):
    series = col.dropna()
    series = series.drop_duplicates()
    return series

def infer_col_type(col: pd.Series):
    if is_numeric(col):
        if is_float(col=col):
            return "decimal"
        else:
            return "int"
    else:
        if is_bool(col=col):
            return "boolean"
        elif is_category(col=col):
            return "category"
        elif is_datetime(col=col):
            return "datetime"
        elif is_complex(col=col):
            return "complex"
        elif is_timedelta(col=col):
            return "timedelta"
        elif is_datetime(col=col):
            return "datetime"
    
    return "object"
