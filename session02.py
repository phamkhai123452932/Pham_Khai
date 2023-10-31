import numpy as np
import math
import matplotlib.pyplot as plt
a1=int(input("nhập a1"))
b1=int(input("nhập b1"))
c1=int(input("nhập c1"))
a2=int(input("nhập a2"))
b2=int(input("nhập b2"))
c2=int(input("nhập c2"))
# Tạo mảng giá trị x từ -10 đến 10
x = np.linspace(-10, 10, 100)

# Tính giá trị y tương ứng cho đường thẳng 1
y1 = (c1 - a1*x) / b1

# Tính giá trị y tương ứng cho đường thẳng 2
y2 = (c2 - a2*x) / b2

# Vẽ đường thẳng 1
plt.plot(x, y1, label='a1x + b1y = c1')

# Vẽ đường thẳng 2
plt.plot(x, y2, label='a2x + b2y = c2')

# Đặt tiêu đề và chú thích cho biểu đồ
plt.title('Biểu đồ hai đường thẳng')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Hiển thị biểu đồ
plt.show()