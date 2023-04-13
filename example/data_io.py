import pandas as pd
from pathlib import Path
import xarray as xr


def get_example_data_file_path(filename, data_dir='example_data'):
    # Path.cwd() returns the location of the source file currently in use (so
    # in this case io.py). We can use it as base path to construct
    # other paths from that should end up correct on other machines or
    # when the package is installed
    current_directory = Path.cwd()
    data_path = Path(current_directory, data_dir, filename)
    return data_path


def load_data(data_file):
    if str(data_file).endswith('.txt'):
        input_file = pd.read_csv(data_file, sep=' ')
        output_data = input_file.to_xarray()
    elif str(data_file).endswith('.nc'):
        output_data = xr.open_dataset(data_file)
    else:
        raise TypeError('file must be a text or NetCDF file')
    return output_data
