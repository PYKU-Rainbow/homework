import sys
import os
import pylab as plt

sys.path.append("C:/Users/USER/PycharmProjects/Project-pre/func")

from d0_makelist_column import MakeList_column

filename = "C:/Users/USER/PycharmProjects/Project-pre/data_txt/ALL_DATA/Aqi_Beijing_WIND.txt"


def line_graph (filename,y_axis):
    Raw_list = MakeList_column(filename)
    Graph_list_subject = []
    Graph_list_body = []
    for i in range(len(Raw_list)):
        Temp_list_subject = []
        Temp_list_body = []
        for k in range(len(Raw_list[i])):
            if k == 0:
                Temp_list_subject.append(Raw_list[i][k])
            else:
                Temp_list_body.append(float(Raw_list[i][k]))

        Graph_list_subject.append(Temp_list_subject)
        Graph_list_body.append(Temp_list_body)

    plt.plot(Graph_list_body[y_axis])
    plt.title(Graph_list_subject[y_axis])
    plt.show()

line_graph(filename,3)





