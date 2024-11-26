import math

def print_circle(radius, center_x, center_y):
    for y in range(10):
        row = ""
        for x in range(10):
            # 计算(x, y)是否在圆形内
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            if abs(distance - radius) < 0.5:  # 设置一个容忍度
                row += "*"
            else:
                row += " "
        print(row)

# 设置圆心和半径
center_x, center_y = 5, 5
radius = 4
print_circle(radius, center_x, center_y)


