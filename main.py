import os
import glob
import pprint
from pathlib import Path

# Setup
pp = pprint.PrettyPrinter(indent=4)

# All variable
DOWNLOAD_FOLDER_PATH = os.path.join( # add trailing slash
    os.getenv('DOWNLOAD_FOLDER_PATH', f'{Path.home()}/Downloads/') # get from env
)

def extract_file_data(filepath):
    _, file_extension = os.path.splitext(filepath)
    return {
        'ext': file_extension,
        'last_modified': os.path.getmtime(filepath), 
        'filepath': filepath
    }

if __name__ == "__main__":
    filepaths = glob.glob(DOWNLOAD_FOLDER_PATH + '*')
    files = map(extract_file_data, filepaths)
    pp.pprint(list(files))
