import zipfile
import pandas as pd

def extract_data(src: str, dest_path: str="data") -> None:
    """
    Extract the contents of the zipped file `src`
    to the `dest_path`.
    
    Args
    =====
    src: (str) The path to the zipped file.
    dest_path: (str) The destination directory.
    
    Return
    ========
    None
    """
    file = zipfile.ZipFile(src)
    file.extractall(dest_path)
    
def load_data(path: str):
    """
    Loads a `csv` file into a Pandas datafame,
    and returns the dataframe.
    
    Args
    =====
    path: (str) The path to the file.
    
    Returns
    ========
    A pandas dataframe.
    """
    try:
        df = pd.read_csv(path)
        print("\nData loaded successfully . . .")
    except Exception as e:
        print("\033[031mError in loading data . . .\033[0m\n", e)
        return
    return df