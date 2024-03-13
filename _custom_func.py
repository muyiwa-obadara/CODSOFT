import zipfile

def extract_data(src: str, dest_path:str="data") -> None:
    """
    Extract the contents of the zipped file `src`
    to the `dest_path`.
    
    Args
    =====
    src: [str] The path to the zipped file.
    dest_path: [str] The destination directory.
    
    Return
    ========
    None
    """
    file = zipfile.ZipFile(src)
    file.extractall(dest_path)