# import this
from dateutil import parser

date_str = "2023-09-25 12:07:00"  # 请设置需要开抢的演唱会时间
dt = parser.parse(date_str)
timestamp = dt.timestamp()
fixtime = str(timestamp).split('.')[0]
starttime = int(fixtime)
print("时间：", fixtime)
print("时间戳：", starttime)
