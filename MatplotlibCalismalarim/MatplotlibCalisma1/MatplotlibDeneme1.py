#PART1- CREATING AND CUSTOMIZING OUR FIRST PLOTS- İLK VİDEO

import matplotlib.pyplot as plt #pyplot matplotlib in alt modülüdür
#plt.xkcd() BU satırla daha amatörce grafikler çizilebilir.
import numpy as np
# plt show u yorum satırına alıp print(plt.style.available) satırını çalıştırırsak aktif stillerin çıktısını alırız.
# bu stilleri kullanmak için plt.style.use('stilin ismi') şeklinde kullanabiliriz.
#grafiğin olması için x ve ynin eleman sayıları birbirine eşit olmalıdır
x =[0,6,7,8,9,10,15,17]
y = [0,250,300,350,400,450,500,550]
plt.plot(x, y)
#İki adet plt.plot kullanarak aynı pencerede birden fazla eğri çizebilirz. 
#Bir değişkeni birden fazla eğride  kullanabiliriz.
py_y =[0,350,450,550,650,750,850,950]
plt.plot(x,py_y)
#title ve label ile grafiğe ve eksenlere isim verebiliriz.
plt.title("ILK MATPLOTLIB GRAFIGIM")
plt.xlabel("yas")
plt.ylabel("deneyim")
#legend ile grafiğe yazıt eklenebilir.
plt.legend(["Deneme1","Deneme2"])
#bu şekilde yapmak yerine aşağıdaki yorum satırlarındaki gibi de yapılabilir.
#plt.plot(x, y, label="Deneme1")
#plt.plot(x,py_y, label = "Deneme2")
#plt.legend()


# plt.plot parantezine aşağıdaki sırayla renk, şekil ve yazıt eklenebilir.
a= [0,2,4,6]
b=[0,10,20,30]
c=[0,20,40,60]
plt.plot(a,b,'k--', marker= 'o', label= "Şekil deneme")
#plt.plot(a,b, color='k', linestyle='--', label='Şekil deneme') # yukarıdaki satırla aynı çıktıyı verir, daha anlaşılırdır.
plt.plot(a,c, '#5a7d9a',marker='.',linewidth=6, label= "Renk deneme") #linewidth= hat genişliği, eğri kalınlıgı
plt.legend()
plt.grid(True)  #grid ile grafiğe ızgara eklenir.
plt.tight_layout()
plt.savefig('plot.png') #BU satırla grafigi png seklinde kaydedebiliriz.
#show göster, görüntüle demektir.
plt.show()
