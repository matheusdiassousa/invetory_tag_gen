from qr_functions import *
import pandas as pd
import os
import numpy as np

#optional dependecy of pandas installed > pip install xlrd

excel_file = 'input_data/Eldorado_Inventory.xlsx';


data = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
col_names = data.columns.values.tolist();
number_of_itens = data[col_names[1]].values;

#print(number_of_itens)



# [1]34x23
# [2]50x30
# [3]75x25 
# [4]100x80

tag = 3; # [1]34x23 [2]50x30 [3]75x25 [4]100x80
itens = [248,249];
#itens = np.arange(536,636,1);

#itens = np.arange(152);

'''
try:
    for item in itens:
        item = int(item);
        data_item = data.loc[item , 'Item'];
        data_pd = data.loc[item, 'Product Description'];
        data_model = data.loc[item, 'Product Model'];
        data_pn = data.loc[item, 'P/N'];
        data_sn = data.loc[item, 'Serial Number'];
        print(item, data_item, data_pd, data_model);
        if(str(data_pd) != "nan"):
            #QRCode = str(data_item) + '/' + str(data_model) + '/' + str(data_pd);
            filename = str(data_item) + '_' + str(data_model);

            textl1 = str(data_pd);
            textl2 = str(data_model);
            textl3 = str(data_item);
            textl4 = str(data_pn);
            textl5 = str(data_sn);
            
            if(tag == 1):
                adhesive_tag_34x23(filename, textl1, textl2, textl3, textl4, textl5, True);
            if(tag == 2):
                adhesive_tag_50x30(filename, textl1, textl2, textl3, textl4, textl5, True);
            if(tag == 3):
                adhesive_tag_75x25(filename, textl1, textl2, textl3, textl4, textl5, True);
            if(tag == 4):
                adhesive_tag_100x80(filename, textl1, textl2, textl3, textl4, textl5, True);                                 

            #adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, textl5, True);
            #adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, True);
            #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
        else:
            print('This item doesn\'t exist!')
except:
    print("Something is not working properly!")

'''
for item in itens:
    item = int(item);
    data_item = data.loc[item , 'Item'];
    data_pd = data.loc[item, 'Product Description'];
    data_model = data.loc[item, 'Product Model'];
    data_pn = data.loc[item, 'P/N'];
    data_sn = data.loc[item, 'Serial Number'];
    print(item, data_item, data_pd, data_model);
    if(str(data_pd) != "nan"):
        #QRCode = str(data_item) + '/' + str(data_model) + '/' + str(data_pd);
        filename = str(data_item) + '_' + str(data_model);

        textl1 = str(data_pd);
        textl2 = str(data_model);
        textl3 = str(data_item);
        textl4 = str(data_pn);
        textl5 = str(data_sn);
            
        if(tag == 1):
            adhesive_tag_34x23(filename, textl1, textl2, textl3, textl4, textl5, True);
        if(tag == 2):
            adhesive_tag_50x30(filename, textl1, textl2, textl3, textl4, textl5, True);
        if(tag == 3):
            adhesive_tag_75x25(filename, textl1, textl2, textl3, textl4, textl5, True);
        if(tag == 4):
            adhesive_tag_100x80(filename, textl1, textl2, textl3, textl4, textl5, True);                                 

        #adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, textl5, True);
        #adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, True);
        #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
    else:
        print('This item doesn\'t exist!')



