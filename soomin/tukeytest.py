import sys
import os
sys.path.append("../func")
from d0_makelist import MakeList
#filename = ("../data_txt/ALL_DATA/Aqi_Beijing_monthly.txt")
filename = ("../data_txt/ALL_DATA/Aqi_Beijing_WIND.txt")
list_A  = MakeList(filename)
import scipy.stats as stats
import pandas as pd
from pandas import Series,DataFrame
from statsmodels.stats.multicomp import pairwise_tukeyhsd

for ii in range(len(list_A)):
    if ii == 0:        
        continue        
    elif float(list_A[ii][0])<20140000:
        continue    
    elif 20140000<float(list_A[ii][0])<20150000:
#        Y2014.append(list_A[ii])
        list_A[ii].append(int(2014))
    elif 20150000<float(list_A[ii][0])<20160000:
#        Y2015.append(list_A[ii])
        list_A[ii].append(int(2015))
    elif 20160000<float(list_A[ii][0])<20170000:
#        Y2016.append(list_A[ii])
        list_A[ii].append(int(2016))
    elif 20170000<float(list_A[ii][0])<20180000:
#        Y2017.append(list_A[ii])
        list_A[ii].append(int(2017))
    elif 20180000<float(list_A[ii][0]):
#        Y2018.append(list_A[ii])
        list_A[ii].append(int(2018))
#print(list_A)
list_B = []
x = list_A.pop(0)
print(list_A)
for aa in range(len(list_A)):
    if aa == 0:
        continue
    else:
        list_B.append(list_A[ii])

#df = DataFrame(list_A,columns=['date','aqi','pm2p5','pm10','so2','co','no2','o3','days','holi','h_temp','wind','year'])
#print(df)
#df=df.reset_index()
#df.head()
#posthoc = pairwise_tukeyhsd(df['aqi'],df['year'],alpha=0.05)
#print(posthoc)

