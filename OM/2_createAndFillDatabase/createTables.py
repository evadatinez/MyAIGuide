# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 18:21:35 2016

@author: Olivier
"""

import defineTables as tabDef
import createDataBase

createDataBase.createTable(tabDef.basisTab)
createDataBase.createTable(tabDef.painTab)
createDataBase.createTable(tabDef.sportTab)
createDataBase.createTable(tabDef.manicTimeTab)
createDataBase.createTable(tabDef.whatPulseTab)
createDataBase.createTable(tabDef.taplogTab)

createDataBase.createTable(tabDef.general)
createDataBase.createTable(tabDef.generalActivities)