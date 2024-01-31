#PART5- FILLING AREA ON LINE PLOTS- 5.VİDEO
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

#overall_median ile ortalamanın altında kalan değerler ters döner 
overall_median = 57287
#aşağıdaki fill_between ile iki plot arası doldurulur.alphanın karşısına yazılan 0-1 arası değerler ile fill rengi koyulaşabilir.
#where ile parantez içindeki şartı sağlamayan veriler grafikte gösterilmez.
#interpolate ile ara değer hesaplanır veya hesaplanmaz aradaki farkı görmek için true ve false olarak ayrı çalıştır.
plt.fill_between(ages,py_salaries,overall_median,
                 where=(py_salaries >overall_median),
                 interpolate=False,  alpha=0.35)
#label ların calışması için aşağıdaki legend satırı eklenmelidir.
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()