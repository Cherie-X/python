import numpy as np
a=np.arange(12).reshape(3,4)
print(a.shape)
print(a.dtype)
print(a.ndim)
b=a.reshape(4,3)
print(b)#将数组变形为（4，3）
c=b.reshape(-1)#将数组按行展平
print(c)
d=b.reshape(-1,order='F')
print(d)#将数组按列展平

