# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:25:15 2019

@author: 邓淦文
"""
import sys
import requests
import json
from WthRport import *
from ArRport import *
from PyQt5 import QtCore, QtGui,QtWidgets, uic


qtCreatorFile = "PyGui.ui" 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.wthwerbton.clicked.connect(self.temrport)
        self.arplutionbton.clicked.connect(self.arport)
    
    def arport(self):   #查询空气污染
        cityname =self.inputcity.toPlainText()
        r=requests.get('http://web.juhe.cn:8080/environment/air/cityair?city='+cityname+'&key=8818f402264a7a5b67898bfa24962028')
        hjson=json.loads(r.text)
        situation1=hjson['result'][0]
        aplu=ArRport(situation1)
        y=aplu.airRport(situation1)
        result1=cityname+'今日AQI为'+y[0]+',今日空气质量:'+y[1]
        self.textEdit.setText(result1)
    
    def temrport(self):  #天气情况
        cityname=self.inputcity.toPlainText()
        p=requests.get('http://v.juhe.cn/weather/index?format=2&cityname='+cityname+'&key=699b9a952916496fbdf179be0a67c042')
        situation2=json.loads(p.text)['result']
        wrport=WthRport(situation2)
        a=wrport.today_wther(situation2)
        result2=cityname+'今日温度为'+a['temperature']+'天气'+a['weather']+a['dressing_advice']
        self.textEdit.setText(result2)

if  __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())

     