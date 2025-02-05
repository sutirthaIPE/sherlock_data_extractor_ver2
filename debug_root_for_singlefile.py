from ast import Index
import os
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import plotly.express as px

file  = open('20250105211401799_IOM_Q422E75A1_119325_618T03_I_L01_Summary.xml',"r")
content = file.readlines()

L_1 = [] # for outer_corner X data
L_2 = [] # for outer_corner Y data
unit_info = [] # collecting unit info
detail = [] # this will have product, lot, tray, lane direction info

for i in range(len(content)):
    if (content[i].__contains__('<MostOuterX>')):
        outer_x = content[i]
        outer_y = content[i+1]
        unit_x_y = content[i-14]
        Product_lot_tray_direction_info = content[i-10]
        L_1.append(outer_x)
        L_2.append(outer_y)
        unit_info.append(unit_x_y)
        detail.append(Product_lot_tray_direction_info)

#=== list of kind of data looking for=====================
outer_corner_X = []
outer_corner_Y = []
Lot_id = []
PWID = []
session_date=[]
direction=[]
product = []
unit_x_y = []

for i in range(len(L_1)):
    new_Lx = L_1[i].replace('<MostOuterX>','').replace('</MostOuterX>','').strip()
    new_Ly = L_2[i].replace('<MostOuterY>','').replace('</MostOuterY>','').strip()
    unit_test = unit_info[i].replace("<Unit",'').replace(">",'').strip()
    unit_test = unit_test.replace('"', '')
    prod = detail[i][41:45]
    lane = detail[i][65:68]
    test_session = detail[i][71:86] 
    Lot = detail[i][91:100] 
    tray = detail[i][108:114] 
    in_or_out = detail[i][115] 
   #------ appending ------------
    outer_corner_X.append(new_Lx)
    outer_corner_Y.append(new_Ly)
    product.append(prod)
    Lot_id.append(Lot)
    PWID.append(tray)
    session_date.append(float(test_session))
    direction.append(in_or_out)
    unit_x_y.append(unit_test)

   
#-- creating dict for pandas DB ------
data = {"Product":product,"Lot_id":Lot_id,
        "PWID":PWID,"test_session":session_date,
        "Direction":direction,'Unit_X_Y':unit_x_y,
        'Outer_corner_X':outer_corner_X,
        'Outer_corner_Y':outer_corner_Y}    
df = pd.DataFrame(data)
df.to_csv('test.csv',index=False)

#---- plotting the data ------------
fig, ax = plt.subplots(2, 1,figsize=(12,4))
ax[0].scatter(df['Unit_X_Y'],df['Outer_corner_X'].astype(float),c='blue',marker='o',s=20,alpha=0.5)
ax[0].axhline(y=450, color='r', linestyle='--', label='UCL')
ax[0].axhline(y=-450, color='r', linestyle='--', label='LCL')
ax[0].set_xlabel('Unit_X_Y')
ax[0].set_ylabel('Outer_corner_X')
ax[0].legend()
ax[0].tick_params(axis='x', labelsize=5, rotation=90) 

ax[1].scatter(df['Unit_X_Y'],df['Outer_corner_Y'].astype(float),c='blue',marker='o',s=20,alpha=0.5)
ax[1].axhline(y=450, color='r', linestyle='--', label='UCL')
ax[1].axhline(y=-450, color='r', linestyle='--', label='LCL')
ax[1].set_xlabel('Unit_X_Y')
ax[1].set_ylabel('Outer_corner_Y')
ax[1].legend()
ax[1].tick_params(axis='x', labelsize=5, rotation=90)
plt.tight_layout()
plt.show()