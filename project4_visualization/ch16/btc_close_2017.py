# import requests
import json
import pygal
import math
# json_url1 = 'https://raw.githubusercontent.com/'
# json_url2 = 'muxuezi/btc/master/btc_close_2017.json'
# # 读取数据
# req = requests.get(json_url1 + json_url2)
# # 将数据写入文件
# with open('btc_close_2017.json', 'w') as f:
#     f.write(req.text)
# 加载json格式

file_name = 'btc_close_2017.json'
with open(file_name) as f:
    btc_data = json.load(f)

# # 打印每一天的信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = float(btc_dict['close'])
#     print("{} is month {} week{}, {}, the close price is {} RMB".format(
#         date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
closes = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(float(btc_dict['close']))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = "收盘价(￥)"
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(close) for close in closes]
line_chart.add('log收盘价', close_log)
# line_chart.add('收盘价', closes)
line_chart.render_to_file('收盘价对数变换折线图(￥).svg')
