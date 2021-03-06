# -*- coding: UTF-8 -*-

import sys
import os
import pylab as plt
import numpy as np

sys.path.append("../func")

from d0_makelist_column import MakeList_column

# scattergram은 산포도 그래프를 그리는 함수입니다. scattergram(파일이름)
def scattergram (filename,x_axis,y_axis):
    filename = filename
    Raw_list = MakeList_column(filename)
    Graph_list_subject = []
    Graph_list_body = []
    x_axis = 0
    y_axis = 0
    # 데이터를 이름과 값의 리스트로 분리합니다. 이름: Graph_list_subject, 값: Graph_list_value
    for i in range(len(Raw_list)):
        Temp_list_subject = []
        Temp_list_body = []
        for k in range(len(Raw_list[i])):
            if k == 0:
                Temp_list_subject.append(Raw_list[i][k])
            else:
                Temp_list_body.append(float(Raw_list[i][k]))

        # 그래프용 리스트 완성
        Graph_list_subject.append(Temp_list_subject)
        Graph_list_body.append(Temp_list_body)

# 보고 싶은 x축, y축 데이터를 선택합니다.
    for n in range(len(Graph_list_subject)):
        print(n, ':', Graph_list_subject[n][0])
    x_axis=int(input("x축에 해당하는 번호를 입력하세요:"))
    y_axis=int(input("y축에 해당하는 번호를 입력하세요:"))

    # 산포도 그래프 그리기
    x_label = Graph_list_subject[x_axis][0]
    y_label = Graph_list_subject[y_axis][0]

    plt.plot(Graph_list_body[x_axis],Graph_list_body[y_axis],'o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(x_label+ '-'+y_label)
    plt.show()

def line_graph (filename,y_axis):
    filename = filename
    Raw_list = MakeList_column(filename)
    Graph_list_subject = []
    Graph_list_body = []
    # 데이터를 이름과 값의 리스트로 분리합니다. 이름: Graph_list_subject, 값: Graph_list_value
    for i in range(len(Raw_list)):
        Temp_list_subject = []
        Temp_list_body = []
        Temp_list = []
        if i == 0:
            for k in range(len(Raw_list[i])):
                if k == 0:
                    Temp_list_subject.append(Raw_list[i][k])
                else:
                    Temp_list.append(Raw_list[i][k])

            for j in range(len(Temp_list)):
                YYYY = Temp_list[j][0:4]
                MM = Temp_list[j][4:6]
                DD = Temp_list[j][6:8]
                Temp_list_body.append(YYYY + '-' + MM + '-' + DD)
        else:
            for k in range(len(Raw_list[i])):
                if k == 0:
                    Temp_list_subject.append(Raw_list[i][k])
                else:
                    Temp_list_body.append(float(Raw_list[i][k]))

        # 그래프용 리스트 완성
        Graph_list_subject.append(Temp_list_subject)
        Graph_list_body.append(Temp_list_body)

    # x축에 날짜 간격 리스트 만들기
    def format_date(x):
        format_date_list = []
        for i in range(len(x)):
            if x[i][5:7] == '01' and x[i][8:10] == '01':
                k = x[i]
                format_date_list.append(k)
            #if x[i][5:7] == '06' and x[i][8:10] == '01':
            #    k = x[i]
            #    format_date_list.append(k)
            #if x[i][5:7] == '09' and x[i][8:10] == '01':
            #    k = x[i]
            #    format_date_list.append(k)
            #if x[i][5:7] == '12' and x[i][8:10] == '01':
            #    k = x[i]
            #    format_date_list.append(k)
            else:
                k = ""
                format_date_list.append(k)
        return format_date_list

    N = len(Graph_list_body[0])
    ind = np.arange(N)

    x_label = Graph_list_subject[0][0]
    y_label = Graph_list_subject[y_axis][0]

    plt.plot(ind, Graph_list_body[y_axis], '-')
    plt.xticks(ind, format_date((Graph_list_body[0])))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(y_label)

    plt.show()

def box_plot(filename):
    filename = filename
    Raw_list = MakeList_column(filename)
    Graph_list_subject = []
    Graph_list_body = []
    x_axis = 0
    y_axis = 0
    # 데이터를 이름과 값의 리스트로 분리합니다. 이름: Graph_list_subject, 값: Graph_list_value
    for i in range(len(Raw_list)):
        Temp_list_subject = []
        Temp_list_body = []
        for k in range(len(Raw_list[i])):
            if k == 0:
                Temp_list_subject.append(Raw_list[i][k])
            else:
                Temp_list_body.append(float(Raw_list[i][k]))

        # 그래프용 리스트 완성
        Graph_list_subject.append(Temp_list_subject)
        Graph_list_body.append(Temp_list_body)

    labels = [Graph_list_subject[i+1][0] for i in range(len(Graph_list_subject[1:]))]

    fig1, ax = plt.subplots()
    ax.set_title(filename)
    ax.boxplot(Graph_list_body[1:], vert=True, labels=labels, showmeans = True, meanline = True, whis = [0, 100])
    ax.xaxis.set_tick_params(rotation=30, labelsize=10)
    ax.yaxis.grid(True)

    plt.show()

filename = "../data_txt/ALL_DATA/Aqi_Beijing_WIND.txt"

#scattergram(filename,2,2)

#line_graph(filename,4)

#box_plot(filename)