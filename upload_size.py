import os
import boto3

BUCKET = "zkloud.zealbots.com"
KEY = "zkloud/Zcusr11111/zkloud/321.png"
FILE = "/home/sitharth/ZEALBOTS/zkloud/321.png"
s3 = boto3.resource('s3')
object = s3.Object(BUCKET,KEY)
MAX_LIMIT = 5242880

# Objects size returns in Bytes
print(object.content_length)
FILE_STAT = os.stat(FILE)
print(FILE_STAT.st_size)

# Objects size returns in Mega Bytes
MB = (1024*1024)
print(FILE_STAT.st_size/MB)


def bytesto(bytes, to, bsize=1024):
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    return bytes / (bsize ** a[to])

print(bytesto(113921,'k',bsize=1024))
print(bytesto(113921,'m',bsize=1024))
print(bytesto(113921,'g',bsize=1024))

# Result
'''
Both remote and local files stats are returned as the same bytes bytes
113921
113921
'''
# TODO:
'''
[ ] Set the size in MB or GB using the st_size property.
'''
