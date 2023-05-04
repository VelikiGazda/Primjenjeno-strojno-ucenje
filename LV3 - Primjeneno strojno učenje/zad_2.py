import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Učitavanje podataka
mtcars = pd.read_csv('mtcars.csv')

#1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara!
mpg_by_cyl = mtcars.groupby('cyl')['mpg'].mean().reset_index()
sns.barplot(x='cyl', y='mpg', data=mpg_by_cyl)
plt.title('Prosječna potrošnja po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('MPG')


#2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila sa 4, 6 i 8 cilindara!
plt.figure()
sns.boxplot(x='cyl', y='wt', data=mtcars)
plt.title('Distribucija težine po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina(wt)')


#3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s rućnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem!
plt.figure()
mpg_by_trans = mtcars[['mpg', 'am']].copy()
mpg_by_trans['am'] = mpg_by_trans['am'].replace({0: 'Automatic', 1: 'Manual'})
sns.boxplot(x='am', y='mpg', data=mpg_by_trans)
plt.title('Odnos potrošnje')
plt.xlabel('Mjenjač')
plt.ylabel('Potrošnja(MPG)')

#4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatksim mjenjačem!
hp_wt_am = mtcars[['hp', 'wt', 'am']].copy()
hp_wt_am['am'] = hp_wt_am['am'].replace({0: 'Automatic', 1: 'Manual'})
sns.lmplot(x='hp', y='wt', hue='am', data=hp_wt_am, fit_reg=False)
plt.title('Odnos ubrzanja i snage')
plt.xlabel('Konjske snage')
plt.ylabel('Q/sec')




# Prikaz grafa
plt.show() 