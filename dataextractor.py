######################################################
# Code Name: Vision Sim Data Parser                  #
# Rev: 1 PROD STABLE                                 #
# Author: Aniket Yashwant Nawle, 12127118            #
# NMDS Yield, ww05'25                                #
######################################################
import os
import fnmatch
from ast import Index
import os
import numpy as np
import pandas as pd
import re

def TheActualExtractor(inputfile):
#    file  = open('20250105211401799_IOM_Q422E75A1_119325_618T03_I_L01_Summary.xml',"r")
    file = open(inputfile,"r")
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
        prod = detail[i][41:46]
        lane = detail[i][65:68]
        test_session = detail[i][71:84]
        Lot = detail[i][89:98]
        tray = detail[i][106:112]
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

    #---- creating dict for pandas DB ----
    data = {"Product": product, "Lot_id": Lot_id,
        "PWID": PWID, "test_session": session_date,
        "Direction": direction, 'Unit_X_Y': unit_x_y,
        'Outer_corner_X': outer_corner_X,
        'Outer_corner_Y': outer_corner_Y}
    new_df = pd.DataFrame(data)
    afilename = 'SIMOutput.csv'
    try:
        existing_DF = pd.read_csv(afilename)
        combined_df = pd.concat([existing_DF,new_df],ignore_index=True)
    except FileNotFoundError:
        print("Concat Failed this attempt")
        combined_df = new_df

    combined_df.to_csv(afilename,index=False)

    return()

def find_summary_xml_files_with_folders(root_dir):
    summary_xml_files_with_folders = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, '*summary.xml'):
            file_path = os.path.join(dirpath, filename)
            summary_xml_files_with_folders.append((dirpath, file_path))
    return summary_xml_files_with_folders

def main():
    root_dir = input("Enter the root directory to search: ")
    if not os.path.isdir(root_dir):
        print(f"The directory {root_dir} does not exist.")
        return

    summary_xml_files_with_folders = find_summary_xml_files_with_folders(root_dir)
    if summary_xml_files_with_folders:
        print("Found the following summary.xml files with their folders:")
        for folder, file in summary_xml_files_with_folders:
            print(f"File:{file}")
            TheActualExtractor(file)
    else:
        print("No summary.xml files found.")



if __name__ == "__main__":
    main()