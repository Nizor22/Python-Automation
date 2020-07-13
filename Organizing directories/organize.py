import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


# Goes over the dictionary, SUBDIRECTORIES, and compares the given suffix with one's in the dictionary
# If a match is found the category is returned, otherwise MISC directory will be returned.
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


''' organizeDirectory():
	1) Scans the OrganizeMe directory.
    2) For every file in the working directory calls pickDirectory(file's extension).
    3) If the directory returned by the pickDirectory doesn't exist, a new one is created.
    4) The file is then assigned a proper directory.
'''


def organizeDirectory(directory):
    for item in os.scandir(directory):
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type = file_path.suffix.lower()
        directory = pickDirectory(file_type)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path))


organizeDirectory('OrganizeMe')
