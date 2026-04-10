from example.data_io import get_example_data_file_path, load_data
import pandas as pd

def test_data_io():
    '''
    Test that example data loads correctly
    '''
    data = load_data(get_example_data_file_path('example_data.txt'))
    assert data.x[0] == 1
