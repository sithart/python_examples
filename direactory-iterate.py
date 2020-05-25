import os
# import time
import datetime
# import pytz

# from typing import List, Tuple
local_directory_list = []
for subdir, dirs, files in os.walk(r'/home/sitharth/Downloads'):
    local_directory = {}
    for filename in files:
        filepath = subdir + os.sep + filename

        # if filepath.endswith(".jpg") or filepath.endswith(".png"):
            # print(os.stat(filepath))
            # print(time.ctime(os.path.getmtime(filepath)))
        modTimesinceEpoc = os.path.getmtime(filepath)
        modificationTime = datetime.datetime.utcfromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
        # print("File Name : ", filename, "Last Modified Time : ", modificationTime, 'UTC')
        local_directory['File Name'] = filename
        local_directory['modificationTime'] = modificationTime
        local_directory_list.append(local_directory)
print(local_directory_list)
