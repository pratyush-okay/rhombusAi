import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    # Your view logic here
    return render(request, 'index.html')  

def data_types(df):
    for col in df.columns:
        # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            df[col] = df_converted
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass
        

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])
    
    return df

## helper functions
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
        if (pd.to_numeric(series, errors='coerce') % 1 == 0).all():
            return True
    except:
        return False

def is_bool(col: pd.Series):
    series = col.dropna()
    if any(isinstance(value, bool) for value in series):
        return True
    
    # Convert strings "True" and "False" to actual boolean values
    series_lower = series.apply(lambda x: x.lower() if isinstance(x, str) else x)

    # Check if all values are boolean after converting string representations
    if any(value in {"true", "False"} for value in series_lower):
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

 # Function to check if a value is null or NaN
def is_null_or_nan(value):
    return pd.isnull(value) or pd.isna(value)

def clean_column(col: pd.Series):
    series = col.dropna()
    series = series.drop_duplicates()
    return series

## infer dtype of a column
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

def get_data_types(df):
    data_types = {}
    for col in df.columns:

        data_types[col] = infer_col_type(df[col])
    return data_types
        

def process_data(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file)
        dtypes_dict = get_data_types(df)
        # dtypes_dict = df.dtypes.apply(lambda x: x.name).to_dict()
        print(dtypes_dict)
        return JsonResponse(dtypes_dict, safe=False)
    # return JsonResponse({'error': 'Invalid request'}, status=400)
    return JsonResponse({'message': 'Request processed succesfully'})




