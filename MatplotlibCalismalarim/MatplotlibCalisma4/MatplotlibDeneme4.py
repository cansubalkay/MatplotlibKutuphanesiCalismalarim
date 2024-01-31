#PART4- STACK PLOTS-4.VİDEO stack plots= yığın grafikleri
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [9, 7, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 1, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
labels= ['player1','player2','player3']
colors= ['#008fd5','#fc4f30','#6d904f']
#stackplot() ile yığın grafiği oluşturulur.
plt.stackplot(minutes, player1, player2, player3, labels= labels, colors=colors)
#yazıtın grafiktekini yerini değiştirmek için legend parantezinin için eistenen yerin adı yazılır. 
#farkı anlamak için aşağıdaki parantezin içini sil. upper left.lower left vs yazılabilir. ya da loc=(0.07,0.05) gibi koordinat yazılabilir.
plt.legend(loc='lower left')

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f