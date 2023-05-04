import pandas as pd
import numpy as np

# Učitavanje skupa podataka mtcars
mtcars = pd.read_csv('mtcars.csv')

# 1. Kojih 5 automobila ima najveću potrošnju?
top5_potrosnja = mtcars.sort_values(by=['mpg'], ascending=False).head(5)
print("Top 5 automobila po potrošnji:\n", top5_potrosnja[['car', 'mpg']])


# 2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
cilindri_8 = mtcars[mtcars['cyl']==8]
top3_cilindri_8 = cilindri_8.sort_values(by=['mpg']).head(3)
print("\nTop 3 automobila s 8 cilindara po potrošnji:\n", top3_cilindri_8[['car', 'mpg']])

# 3. Kolika je srednja potrošnja automobila sa 6 cilindara?
potrosnja_cilindri_6 = mtcars[mtcars['cyl']==6]['mpg'].mean()
print("\nSrednja potrošnja automobila s 6 cilindara:", potrosnja_cilindri_6)

# 4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
potrosnja_cilindri_4 = mtcars[(mtcars['cyl']==4) & (mtcars['wt']>=2000) & (mtcars['wt']<=2200)]['mpg'].mean()
print("\nSrednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs:", potrosnja_cilindri_4)

# 5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
broj_rucni = mtcars[mtcars['am']==0]['am'].count()
broj_automatik = mtcars[mtcars['am']==1]['am'].count()
print("\nBroj automobila s ručnim mjenjačem: ", broj_rucni)
print ("\nBroj automobila s automatskim mjenjačem: ", broj_automatik)

# 6.  Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
broj_automatik_snaga_100 = mtcars[(mtcars['am']==0) & (mtcars['hp']>100)]['am'].count()
print("\nBroj automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga:", broj_automatik_snaga_100)

# 7. Kolika je masa svakog automobila u kilogramima?
masa_kilogrami = mtcars['mass_kg'] = mtcars['wt'] * 0.453592
print("\nMasa svakog automobila u kilogramima:",masa_kilogrami)