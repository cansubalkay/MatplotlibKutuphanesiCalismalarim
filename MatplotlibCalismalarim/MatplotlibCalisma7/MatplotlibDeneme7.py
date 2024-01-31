#PART7- SCATTER PLOTS- 7.VİDEO scatter plot= dağılım grafiği
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
#aşağıdaki x ve y başta anlamak için verilen örneklerdi daha sonra gercek datalarla grafik oluşturuldu
#x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
#y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

#colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
#plt.scatter ile dağılım grafiği oluşturulur. s ile noktaların büyüklüğü ayarlanır.c ile rengi ayarlanır. marker ile şekil ayarlanır
#s= sizes yapılırsa bütün noktalar birbirinden farklı boyutta olacaktır.
plt.scatter(view_count, likes, s=100,  marker='X', c=ratio,
            edgecolor='black', cmap='summer',
            linewidth=1, alpha=0.75)
#aşağıdaki iki satır ile yoğunluk gösterici eklenir
#cbar = plt.colorbar()
#cbar.set_label('Satisfaction')
plt.xscale('log')
plt.yscale('log')


# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]



plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()