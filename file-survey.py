import os
import datetime
from typing import List, Tuple


filesurvey: List[Tuple] = []
path_dir = (r'/home/sitharth/Downloads')
content_dir: List[str] = os.listdir(path_dir)

for filename in content_dir:

    path_file = os.sep.join([path_dir, filename])

    modTimesinceEpoc = os.path.getmtime(path_file)
    modificationTime = datetime.datetime.utcfromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
    # print("Last Modified Time : ", modificationTime, 'UTC')

    filesurvey.append((path_dir, filename, modificationTime))
print(filesurvey)
