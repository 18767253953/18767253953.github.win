import numpy as np
import matplotlib.pyplot as plt
import math

x=np.arange(-10,7,1)  
y=[np.sin(math.pi*i/4) for i in x]  
plt.scatter(x,y)  
plt.title('sin函数')
plt.figure()
plt.show()  #绘制图像
