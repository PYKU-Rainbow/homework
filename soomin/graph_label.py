import sys
import os
import matplotlib.pyplot as plt
import pylab as plt
import numpy as np
import matplotlib.legend as legend
import math
sys.path.append("../func")
from d0_makelist_column import MakeList_column

filename = ("../data_txt/ALL_DATA/Aqi_Beijing_monthly.txt")
graph_list = MakeList_column(filename)

graph_list_subject= []
graph_list_body = []

for i in range(len(graph_list)):
    Temp_list_subject=[]
    Temp_list_body=[]
    for k in range(len(graph_list[i])):
        if k == 0:
            Temp_list_subject.append(graph_list[i][k])
        else:
            Temp_list_body.append(float(graph_list[i][k]))
#     print(Temp_list_body)
    graph_list_subject.append(Temp_list_subject)
    graph_list_body.append(Temp_list_body)



#print(graph_list_subject);print(graph_list_body)
A_list = graph_list_body[3]; print(A_list);mean_A=sum(A_list)/len(A_list);vsum=0;
for x in A_list:
    vsum = vsum +(x-mean_A)**2
var=vsum/len(A_list)
mean_A=("%.3f"%round(mean_A,3))
var=("%.3f"%round(var,3))
B_list = graph_list_body[2]; print(B_list);mean_B=sum(B_list)/len(B_list)
vsum2=0
for x in B_list:
    vsum2= vsum2 +(x-mean_B)**2
var2=vsum2/len(B_list)
mean_B=("%.3f"%round(mean_B,3))
var2=("%.3f"%round(var2,3))
C_list = graph_list_body[4]; print(C_list)
index = graph_list_body[5]

plt.plot(index,A_list,'g',label='mean = '+(str(mean_A))+'   var='+(str(var)))
plt.plot(index,B_list,'r',label='mean = '+(str(mean_B))+'   var='+(str(var2)))
plt.legend()
plt.grid(True)
plt.show()

