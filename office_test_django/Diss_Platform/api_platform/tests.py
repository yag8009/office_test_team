

# Create your tests here.
from pyecharts import *
# 数据
from pyecharts.charts import Bar

attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
bar = Bar('柱形图', '库存量')
bar.add('服装', attr, v1,  is_label_show=True)
bar.show_config()
bar.render(path='./data/01-01柱形图.html')

bar2 = Bar("显示标记线和标记点")
bar2.add('商家A', attr, v1, mark_point=['avgrage'])
bar2.add('商家B', attr, v2, mark_point=['min', 'max'])
bar2.show_config()
bar2.render(path='./data/01-02标记点柱形图.html')

bar3 = Bar("水平显示")
bar3.add('商家A', attr, v1)
bar3.add('商家B', attr, v2, is_convert=True)
bar3.show_config()
bar3.render(path='./data/01-03水平柱形图.html')