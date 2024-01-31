#PART3- PIE CHARTS- 3.VİDEO pie charts= dilim grafikler
#Colors:
# Blue = #008fd5 Red= #fc4f30 Yellow= #e5ae37 Green= #6d904f
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices =[60, 30,10]
#Aşağıdaki labels ve colors örneklerindeki gibi değişkenleri baştan atayıp plt. parantezine ekleyebiliriz böylece kod daha anlaşılabilir olur.
labels= ['sixty', 'thirty', 'ten']
# explode= kırmak anlamına gelir belirtilen veriyi pastadan belirtildiği uzaklık kadar uzaklaştırır.
explode = [0,0.15,0]
colors=['blue','red','black']
#plt.pie ile dilimli grafik oluşturulur. edgeprop= kenar destekleri wedgeprops ile dilimler farklı bir renkle bşrbirinden ayrılır.
# shadow=True ile grafik üç boyutlu görünür. startangle ile karşılığında girilen değere en yakın parça ile grafik başlar. 
#autopct ile dilimlerin üzerine yüzdelikleri yazılır.
plt.pie(slices,colors=colors,  labels = labels,explode=explode,shadow= True,startangle=10, wedgeprops={'edgecolor': 'black'}) 
plt.title("My Pie Chart")
plt.tight_layout()
plt.show()