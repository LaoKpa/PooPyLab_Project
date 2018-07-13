# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 08:59:44 2018

@author: Ars
"""
import numpy as np
import math
import pandas as pd

class PrimaryClarifier ():
    
    def __init__(self, Shape, Volume, Depth, width_length_ratio= 0.6):
        '''
        Shape: shape of the clarifier which can be 'rectangular' or 'circular'
        Volume: volume of the clarifier
        width_length_ratio: for rectanular clarifiers,it is possible to 
        specify the width/length
        '''
        
        self.shape= Shape
        self.volume= Volume
        self.depth= Depth
        self.surface= self.volume/self.depth
        self.width_length_ratio= width_length_ratio
        
        if self.shape == 'rectangular':
            self.length= np.sqrt(self.surface / self.width_length_ratio)
            self.width= self.length * self.width_length_ratio
        if self.shape == 'circular':
            self.radius= np.sqrt(self.surface / math.pi)
            self.diameter= self.radius * 2
            
    def apply(self, all_params):
        '''
        all_params: it is all the parameters of the influent
        '''
        self.parameters= all_params.to_dict()
        self.residence_time= self.volume / self.parameters['design_flow']
        
        if self.residence_time < 4.0:
            self.parameters['TSS']= self.parameters['TSS'] * (1-self.residence_time * 0.1)
            self.parameters['CODb']= self.parameters['CODb'] * (1-self.residence_time * 0.05)
            self.parameters['CODb']= self.parameters['CODb'] * (1-self.residence_time * 0.08)
            self.parameters['BOD5']= self.parameters['BOD5'] * (1-self.residence_time * 0.02)
            
        else:
            self.parameters['TSS']= self.parameters['TSS'] * 0.4
            self.parameters['CODb']= self.parameters['CODb'] * 0.6
            self.parameters['CODb']= self.parameters['CODb'] * 0.5
            self.parameters['BOD5']= self.parameters['BOD5'] * 0.8
            
        return (pd.Series(self.parameters))
            
        
            
        
        
            
        
        