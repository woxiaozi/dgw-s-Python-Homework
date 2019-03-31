# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:09:42 2019

@author: 邓淦文
"""

class WthRport(object):
    def __init__(self,situation2):
        self.situation2=situation2
    def today_wther(self,situation2):
        return(situation2['today'])
    
    def future_wther(self,situation2):
        return(situation2['future'])
    