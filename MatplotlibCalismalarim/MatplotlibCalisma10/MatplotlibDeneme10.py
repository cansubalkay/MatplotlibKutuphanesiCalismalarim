#PART10-SUBPLOTS-10.VİDEO subplots=alt olay örgüsü
#BU kodla bir pencerede birden fazla grafik oluşturulabilir.
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']
#fig satırlarını aşağıdaki gibi ayrıyazarsak run edildiğinde 2 pencere açılır, 
#tek satırda yazarsak bir pencerede iki grafik açılır
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444',
          linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')



ax1.legend()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
#aşağıdaki iki satırla grafikleri kaydedebiliriz.
fig1.savefig('fig1.png')
fig2.savefig('fig2.png')