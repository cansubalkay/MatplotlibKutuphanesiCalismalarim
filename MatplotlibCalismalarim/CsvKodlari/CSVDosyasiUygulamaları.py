#DATA.CSV DOSYAM OLMADIGI İCİN BURASI HATA VERİYOR
#Bu hatayı eğitimin yüklendiği github hesabındaki data.csv dosyasını manuel açıp içeriği kopyalayark çözdüm.""
#2.videoda yer alan bu bölüm ile  csv dosyasındaki verileri alarak matplotlib ile grafiğe dönüştürdük
import csv 
import numpy as np
import pandas as pd
from collections import Counter 
from  matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids= data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter=Counter()

for response in lang_responses:
        language_counter.update(response.split(';'))
languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
#aşağıdaki reverse ler ile grafik döner ve yüksek olan üste gelir aradki farkı görmek istiyorsan aşağıdaki iki satıra yoruma alarak dene bir de.
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
#plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.show()