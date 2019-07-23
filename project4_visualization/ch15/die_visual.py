import pygal

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die(10)


# 掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "6面的骰子和10面的骰子掷5000次的结果"
# hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [str(pro) for pro in range(2, max_result+1)]
hist.x_title = "结果"
# hist.x_title = "result"
hist.y_title = "频数"
# hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
