import matplotlib.pyplot as plt

# 간단한 데이터
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 40]

# 막대 그래프 그리기
plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('values')
plt.title('Simple Data visualization')
plt.show()

