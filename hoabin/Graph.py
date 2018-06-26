# -*- coding: UTF-8 -*-

import sys
import os
import pylab as plt

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

     #꺾은선 그래프 그리기
    plt.plot(Graph_list_body[y_axis])
    plt.title(Graph_list_subject[y_axis])
    plt.show()

filename = "../data_txt/ALL_DATA/Aqi_Beijing_monthly.txt"

scattergram(filename,2,2)

line_graph(filename,4)