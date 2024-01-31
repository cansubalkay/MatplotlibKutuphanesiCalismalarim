#PART2-BAR CHARTS AND ANALYZING DATA FROM CSVs-2. VİDEO 
#bar charts= çubuk grafikler
import csv 
import numpy as np
from  matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
ages_x= [20,21,22,23,24,25]
x_indexes = np.arange(len(ages_x))
#width ile yanyana çubuk grafikler oluşturulabilir
width =0.25
dev_y= [3000,4000,5000,4500,4200,6000]
py_dev_y =[5000,6000,7000,8000,9000,9500]
plt.bar(x_indexes - width,dev_y,width=width,  color= "#777777", label="All Devs") #plt.plot yerine bar yazarak çubuk grafik oluşturulur
js_dev_y=[2000,3000,4000,5000,5500,7000]
plt.bar(x_indexes + width, js_dev_y, width=width)
#plot ve bar tipi eğriler aynı pencere ve grfaik üzerinde yer alabilir.
plt.bar(x_indexes,py_dev_y, width=width, color='b',label="Python")
plt.legend()
#plt.xticks ile ages_x i indeksler yerine yazdırdık
plt.xticks(ticks=x_indexes, labels=ages_x)
plt.title("Median Salary (TC) by Age")
plt.show()  