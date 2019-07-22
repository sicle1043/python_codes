import matplotlib.pyplot as plt


# 解决中文乱码
plt.rcParams['font.sans-serif'] = 'SimHei'

x_values = list(range(1, 1001))
y_values = [i**2 for i in x_values]

plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)

# 设置图表标题， 并给坐标轴加上标签
plt.title("平方数", fontsize=24)
plt.xlabel("数值", fontsize=14)
plt.ylabel("数值的平方", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标的取值范围
plt.axis([0, 1100, 0, 1100000])

# 保存图片而不输出图片
plt.savefig('squares_plot.png', bbox_inches='tight')
