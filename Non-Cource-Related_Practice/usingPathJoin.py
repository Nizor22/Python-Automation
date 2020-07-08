import os
from pathlib import Path
searchDir = Path('C:/Users/megan/Desktop')

for entry in os.listdir(searchDir):
    filePath = os.path.join(searchDir, entry)
    fh = open(filePath)