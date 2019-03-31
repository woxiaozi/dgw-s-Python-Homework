# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:45:38 2019

@author: 邓淦文
"""

class ArRport(object):
    def __init__(self,situation1):
        self.situation1=situation1     
    def airRport(self,situation1):
        y=[]
        y.append(situation1['citynow']['AQI'])
        y.append(situation1['citynow']['quality'])
        return(y)
        
        
        
        