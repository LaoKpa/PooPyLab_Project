# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 08:58:29 2018

@author: Ars
"""

import Flows, Clarifiers

inf= Flows.influent(BOD5=200, TSS=100, VSS=10, TKN=20, NH3=10, NO=5, TP=5, ALK=400, DO=0, design_flow=300)
params= inf.get_inf_parameters()
primary_clarifier= Clarifiers.PrimaryClarifier(Shape='circular', Volume= 20, Depth= 3)
post_clarifier= primary_clarifier.apply(all_params=params)
print(post_clarifier)
