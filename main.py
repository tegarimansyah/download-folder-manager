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

def file_grouping(list_of_ext, list_of_files):
    ext_counter = {}
    ext_group = {}
    for ext in list_of_ext:
        list_filter = tuple(filter(lambda files: files.get('ext') == ext, list_of_files))

        ext_group[ext] = list_filter
        ext_counter[ext] = len(list_filter)
    
    return ext_counter, ext_group

if __name__ == "__main__":
    filepaths = glob.glob(DOWNLOAD_FOLDER_PATH + '*')
    filepaths.sort(key=os.path.getmtime) # sort by time modified, unix time, asc (last is newest)

    files = tuple(map(extract_file_data, filepaths))
    extensions = ext_mapping(files)
    extension_counter, file_group = file_grouping(extensions, files)
    
    pp.pprint(extension_counter)
    
    # Sample, get all .zip files 
    pp.pprint(file_group.get('.zip'))
