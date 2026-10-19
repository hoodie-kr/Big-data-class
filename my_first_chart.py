import matplotlib.pyplot as plt
prices = [71000, 70500, 71800, 72400, 71900]
fig, ax = plt.subplots()
ax.plot(prices)
fig.savefig("my_first_chart.png")
plt.show()