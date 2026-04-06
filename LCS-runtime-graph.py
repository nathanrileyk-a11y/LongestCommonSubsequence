import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [0.0054,0.0050,0.0065,0.0060,0.0067,0.0034,0.0017,0.0010, 0.0035, 0.1036]
plt.plot(x, y)
plt.xlabel('test file')
plt.ylabel('runtime (s)')
plt.title('Longest Common Subsequence Runtime')
plt.xticks(x)
plt.show()