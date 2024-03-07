import pandas as pd
import pytest
from data_processing import is_numeric, is_float, is_bool, is_category, is_datetime, is_timedelta, is_complex, infer_col_type, clean_column

# Sample data for testing
data = {
    'col1': pd.Series([1, 2, 3, 4]),
    'col2': pd.Series([1.1, 2.2, 3.3, 4.4]),
    'col3': pd.Series([True, False, True, False]),
    'col4': pd.Series(['a', 'b', 'c', 'd']),
    'col5': pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']),
    'col6': pd.Series([pd.Timedelta(days=1), pd.Timedelta(days=2), pd.Timedelta(days=3), pd.Timedelta(days=4)]),
    'col7': pd.Series([1+2j, 2+3j, 3+4j, 4+5j]),
}

def test_is_numeric():
    # Numeric series
    assert is_numeric(pd.Series([1, 2, 3, 4])) == True
    assert is_numeric(pd.Series([1.1, 2.2, 3.3, 4.4])) == True
    
    # Non-numeric series
    assert is_numeric(pd.Series(['a', 'b', 'c', 'd'])) == False
    assert is_numeric(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'])) == False

# Test for is_float
def test_is_float():
    # Float series
    assert is_float(pd.Series([1.1, 2.2, 3.3, 4.4])) == True
    
    # Non-float series

    assert is_float(pd.Series(['a', 'b', 'c', 'd'])) == False

# Tests for is_bool
def test_is_bool():
    assert is_bool(data['col1']) == False
    assert is_bool(data['col2']) == False
    assert is_bool(data['col3']) == True
    assert is_bool(data['col4']) == False
    assert is_bool(data['col5']) == False
    assert is_bool(data['col6']) == False
    assert is_bool(data['col7']) == False

def test_is_category():
    # Non-category series
    assert is_category(pd.Series([1, 2, 3, 4])) == False
    assert is_category(pd.Series([1.1, 2.2, 3.3, 4.4])) == False
    assert is_category(pd.Series(['a', 'b', 'c', 'd'])) == False
    assert is_category(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'])) == False

# Test for is_datetime
def test_is_datetime():
    # Non-datetime series
    assert is_category(pd.Series([1, 2, 3, 4])) == False
    
    # Datetime series
    assert is_datetime(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'])) == True
    assert is_datetime(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']).apply(pd.to_datetime)) == True
    assert is_datetime(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']).apply(pd.to_datetime, errors='coerce')) == True
    assert is_datetime(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']).apply(pd.to_datetime, errors='ignore')) == True


# Tests for is_complex
def test_is_complex():
    assert is_complex(data['col1']) == False
    assert is_complex(data['col2']) == False
    assert is_complex(data['col3']) == False
    assert is_complex(data['col4']) == False
    assert is_complex(data['col5']) == False
    assert is_complex(data['col6']) == False
    assert is_complex(data['col7']) == True


# Tests for clean_column
def test_clean_column():
    assert clean_column(data['col1']).equals(pd.Series([1, 2, 3, 4]))
    assert clean_column(data['col2']).equals(pd.Series([1.1, 2.2, 3.3, 4.4]))
    assert clean_column(data['col3']).equals(pd.Series([True, False]))
    assert clean_column(data['col4']).equals(pd.Series(['a', 'b', 'c', 'd']))
    assert clean_column(data['col5']).equals(pd.Series(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']))
    assert clean_column(data['col6']).equals(pd.Series([pd.Timedelta(days=1), pd.Timedelta(days=2), pd.Timedelta(days=3), pd.Timedelta(days=4)]))
    assert clean_column(data['col7']).equals(pd.Series([1+2j, 2+3j, 3+4j, 4+5j]))
