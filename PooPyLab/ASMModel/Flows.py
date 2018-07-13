# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:15:59 2018

@author: Ars
"""

import pandas as pd

class influent():
    
    def __init__(self, BOD5, TSS, VSS, TKN, NH3, NO, TP, ALK, design_flow, DO=0.0, 
                 CODb_BOD5_ratio=1.71, CODt_BOD5_ratio= 2.04, soluble_innert_CODt=0.13,
                 particulate_biodeg_COD=1.6, X_BH=0.0, X_BA=0.0, X_D = 0.0,
                 nonbiodegradable_TKN_ratio= 0.03):
        '''
        Please enter the design_flow in m3/h
        CODb: influent biodegradable COD, BOD/COD = 1.71 for typ. muni.WW
        CODt: influent total COD, COD/BOD5 = 2.04 per BioWin
        CODi: influent total innert COD
        S_I: influent soluble innert COD (soluble_innert_CODt)
        X_I: influent particulate innert COD 
        X_S: influent particulate biodegradable COD (multiplied by particulate_biodeg_COD)
        S_S: influent soluble biodegradable COD
        X_BH: influent Heterotrophs (mgCOD/L)
        X_BA: influent Autotrophs (mgCOD/L)
        X_D: influent Biomass Debris (mgCOD/L)
        nb_TKN: nonbiodegradable TKN 
        S_NS: soluble biodegrable TKN
        X_NS: particulate biodegradable TKN
        
        '''
        self.BOD5= BOD5
        self.TSS= TSS
        self.VSS= VSS
        self.TKN= TKN
        self.NH3= NH3
        self.NO= NO
        self.TP= TP
        self.ALK= ALK
        self.DO= DO
        self.design_flow= design_flow
        self.CODb_BOD5_ratio= CODb_BOD5_ratio
        self.CODt_BOD5_ratio= CODt_BOD5_ratio
        self.soluble_innert_CODt= soluble_innert_CODt
        self.particulate_biodeg_COD= particulate_biodeg_COD
        self.X_BH = X_BH 
        self.X_BA= X_BA
        self.X_D = X_D
        self.nonbiodegradable_TKN_ratio= nonbiodegradable_TKN_ratio
        
        self.CODb= self.BOD5 * self.CODb_BOD5_ratio
        self.CODt= self.BOD5 * self.CODt_BOD5_ratio
        self.CODi= self.CODt - self.CODb
        self.S_I= self.soluble_innert_CODt * self.CODt
        self.X_I= self.CODi - self.S_I
        self.X_S= self.particulate_biodeg_COD * self.VSS - self.X_I
        self.S_S = self.CODb - self.X_S
        self.nb_TKN= self.TKN * self.nonbiodegradable_TKN_ratio
        self.soluble_biodegradable_OrgN_ratio = self.S_S / (self.S_S + self.X_S)
        self.S_NS = (self.TKN - self.NH3 - self.nb_TKN)\
                    * self.soluble_biodegradable_OrgN_ratio
        self.X_NS = (self.TKN - self.NH3 - self.nb_TKN)\
                    * (1.0 - self.soluble_biodegradable_OrgN_ratio)
         
        
        self.input_dict={}
        
        
    def get_inputs(self):
        '''
        To check the user inputs
        '''
        self.input_dict['BOD5']= self.BOD5
        self.input_dict['TSS']= self.TSS
        self.input_dict['VSS']= self.VSS
        self.input_dict['TKN']= self.TKN
        self.input_dict['NH3']= self.NH3
        self.input_dict['NO']= self.NO
        self.input_dict['TP']= self.TP
        self.input_dict['ALK']= self.ALK
        self.input_dict['DO']= self.DO
        self.input_dict['design_flow']= self.design_flow
        return (pd.Series(self.input_dict))
        #print('Inputs: {}'.format(self.inf_dict))
        
    def get_inf_parameters(self):
        '''
        To see all the parameters including the 
        ones calculated by the program
        '''
        self.all_params= self.get_inputs().to_dict()
        self.all_params['CODb']= self.CODb
        self.all_params['CODt']= self.CODt
        self.all_params['CODi']= self.CODi
        self.all_params['S_I']= self.S_I
        self.all_params['X_I']= self.X_I
        self.all_params['X_S']= self.X_S
        self.all_params['S_S']= self.S_S
        self.all_params['X_BH']= self.X_BH
        self.all_params['X_BA']= self.X_BA
        self.all_params['X_D']= self.X_D
        self.all_params['nb_TKN']= self.nb_TKN
        self.all_params['S_NS']= self.S_NS
        self.all_params['X_NS']= self.X_NS
        return (pd.Series(self.all_params))
        

      