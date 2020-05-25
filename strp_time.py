import datetime
import maya

date_time_str = '2020-05-21  11:49:50.268380'
# 2020-05-21T11:49:50.268380
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
print(date_time_obj)
#
# import datetime
#
# date_time_str = '2018-06-29 08:15:27.243860'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


dt = maya.parse('2020-05-21T11:49:50.268380').datetime(to_timezone='Europe/London', naive=False)
print(dt.date())
print(dt.time())
print(dt.tzinfo)
