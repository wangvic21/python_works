import pygal
bar_chart = pygal.Bar()
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.render_to_file('bar_chart.svg')
#) 生成 png 格式图表
bar_chart.render_to_png(filename='bar_chart.png')