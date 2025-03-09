import pandas as pd
import numpy as np
from main import DataProcessor

def test_load_data():
    processor = DataProcessor()
    processor.load_data('test.csv', 'csv')
    assert isinstance(processor.data, pd.DataFrame)

def test_clean_data():
    processor = DataProcessor()
    processor.data = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, 6]})
    processor.clean_data()
    assert not processor.data.isnull().values.any()

def test_normalize_data():
    processor = DataProcessor()
    processor.data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    processor.normalize_data()
    assert processor.data['A'].mean() == 0
    assert processor.data['B'].dtype == 'int64'

def test_identify_inconsistencies():
    processor = DataProcessor()
    processor.data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    processor.identify_inconsistencies()
    assert 'anomaly' in processor.data.columns

def test_export_data():
    processor = DataProcessor()
    processor.data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    processor.export_data('test_output.csv', 'csv')
    assert pd.read_csv('test_output.csv').equals(processor.data)