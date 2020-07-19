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

def ext_mapping(list_of_files):
    return set( file_object.get('ext').lower() for file_object in list_of_files)

if __name__ == "__main__":
    filepaths = glob.glob(DOWNLOAD_FOLDER_PATH + '*')
    filepaths.sort(key=os.path.getmtime) # sort by time modified, unix time, asc (last is newest)

    files = map(extract_file_data, filepaths)
    extension = ext_mapping(tuple(files))
    
    pp.pprint(extension)
