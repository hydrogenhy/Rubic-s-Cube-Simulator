# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

# # 创建一个 3x3 的立方体
# square = np.array([
#     (0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0),
#     (0, 1, 0), (1, 1, 0), (2, 1, 0), (3, 1, 0),
#     (0, 2, 0), (1, 2, 0), (2, 2, 0), (3, 2, 0),
#     (0, 3, 0), (1, 3, 0), (2, 3, 0), (3, 3, 0),

#     (0, 0, 1), (1, 0, 1), (2, 0, 1), (3, 0, 1),
#     (0, 1, 1),                       (3, 1, 1),
#     (0, 2, 1),                       (3, 2, 1),
#     (0, 3, 1), (1, 3, 1), (2, 3, 1), (3, 3, 1),

#     (0, 0, 2), (1, 0, 2), (2, 0, 2), (3, 0, 2),
#     (0, 1, 2),                       (3, 1, 2),
#     (0, 2, 2),                       (3, 2, 2),
#     (0, 3, 2), (1, 3, 2), (2, 3, 2), (3, 3, 2),

#     (0, 0, 3), (1, 0, 3), (2, 0, 3), (3, 0, 3),
#     (0, 1, 3), (1, 1, 3), (2, 1, 3), (3, 1, 3),
#     (0, 2, 3), (1, 2, 3), (2, 2, 3), (3, 2, 3),
#     (0, 3, 3), (1, 3, 3), (2, 3, 3), (3, 3, 3),
# ])
    
# colors = ['w', '#FBFF34', 'r', 'b', 'g', 'orange']

# # 提取顶点坐标
# x = square[:, 0]
# y = square[:, 1]
# z = square[:, 2]

# # 创建绘图对象
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # 绘制立方体的顶点
# ax.scatter(x, y, z, c='b', marker='o')
# for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
#     ax.text(xi, yi, zi, f'{i}')
# # 设置坐标轴刻度
# ax.axis('off')
# ax.set_xlim([0, 3])
# ax.set_ylim([0, 3])
# ax.set_zlim([0, 3])
# ax.set_aspect('equal')

# # 显示图形
# plt.show()

def rotate_180(matrix):
    # 先水平翻转每一行
    horizontal_flip = [row[::-1] for row in matrix]
    # 再垂直翻转整个列表
    vertical_flip = horizontal_flip[::-1]
    return vertical_flip

def rotate_270(matrix):
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    rotated_matrix = transposed_matrix[::-1]
    return rotated_matrix
# 示例二维列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 旋转180度
rotated_matrix = rotate_270(matrix)
print(rotated_matrix)