import matplotlib.pyplot as plt


# 解决中文乱码
plt.rcParams['font.sans-serif'] = 'SimHei'

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.figure(figsize=(10, 6))
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题， 并给坐标轴加上标签
plt.title("平方数", fontsize=24)
plt.xlabel("数值", fontsize=14)
plt.ylabel("数值的平方", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
