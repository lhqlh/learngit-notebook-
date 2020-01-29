# ctrl+/ 注释
# alt+1 项目视图
# ctrl+d 复制行
# ctrl+y 删除行
# alt+enter 错误修复
# shift+alt+up 代码上移
# shift+alt+down 代码下移
# ctrl+F 文件查找
# ctrl+shift+F 项目查找

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
# y = 2*x + 1
# # 第一个是横坐标的值，第二个是纵坐标的值
# plt.plot(x, y)  
# plt.show()

y1 = 2*x + 1
y2 = 2**x + 1

# 使用figure()函数重新申请一个figure对象
# 注意，每次调用figure的时候都会重新申请一个figure对象
#plt.figure()
# 第一个是横坐标的值，第二个是纵坐标的值
#plt.plot(x, y1)

# 第一个参数表示的是编号，第二个表示的是图表的长宽
plt.figure(num = 2, figsize=(8, 5))
# 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
plt.plot(x, y2)
plt.plot(x, y1, 
         color='green',   # 线颜色
         linewidth=1.0,  # 线宽 
         linestyle='--'  # 线样式
        )
# 设置轴线的lable（标签）
plt.xlabel("I am x")
plt.ylabel("I am y")

plt.show()

# n = 1024
# # 从[0]
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# T = np.arctan2(X, Y)

# plt.scatter(np.arange(5), np.arange(5))

# plt.xticks(())
# plt.yticks(())

# plt.show()