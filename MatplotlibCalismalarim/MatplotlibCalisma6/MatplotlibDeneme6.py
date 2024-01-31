#PART6-HISTOGRAMS- 6.VİDEO Histogram= gruplandırılmış bir veri dağılımının sütun grafiğiyle gösterimidir.
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55] bu satırı denemek için başta çalıştırdım.
bins = [10,20,30,40,50,60,70,80,90,100] #bu satırla belirtilen değerler arasına çizgi konur
#bins= kutular, bins ile sütun kutusu sayısı ayarlanır.bins ayrı olarak değişken olarak da tanımlanabilir, parantez içinde bins=sayı olark da
#plt.hist ile histogram grafiği oluşturulur.
#log=True ile y eksenindekilerin logaritmasını aldı 
plt.hist(ages, bins=bins, edgecolor='black',log=True) 


median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median')
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()

