import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, edgecolors='none', s=1) # s指点的大小
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=1) # s指点的大小
# plt.scatter(x_values, y_values, c=(0.8, 0, 0), edgecolors='none', s=1) # s指点的大小

# 设置颜色映射
# 参见网站 http://matplotlib.org
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=1) # s指点的大小

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 保存图片。第二个实参代表裁剪周围空白区域
plt.savefig('squares_plot.png', bbox_inches='tight')