import matplotlib.pyplot as plt


years = [2010, 2012, 2014, 2016, 2018, 2020]

programmers_count = [12, 14, 16, 18, 20, 22]


plt.plot(years, programmers_count, marker='o', linestyle='-')


plt.title('Количество программистов по годам')
plt.xlabel('Год')
plt.ylabel('Количество программистов (млн)')


plt.grid(True)
plt.show()

