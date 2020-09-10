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

itens = [825,826];

#itens = np.arange(812,824,1);

#itens = np.arange(152);


try:
    for item in itens:
        item = int(item);
        data_item = data.loc[item , 'Item'];
        data_pd = data.loc[item, 'Product Description'];
        data_model = data.loc[item, 'Product Model'];
        data_pn = data.loc[item, 'P/N'];
        data_sn = data.loc[item, 'Serial Number'];

        if(str(data_pd) != "nan"):
            QRCode = str(data_item) + '/' + str(data_model) + '/' + str(data_pd);
            filename = str(data_item) + '_' + str(data_model);

            textl1 = str(data_pd);
            textl2 = str(data_model);
            textl3 = str(data_item);
            textl4 = str(data_pn);
            textl5 = str(data_sn);
            
            adhesive_tag_75x25_v2(QRCode, filename, textl1, textl2, textl3, textl4, textl5, True);
            #adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, True);
            #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
        else:
            print('This item doesn\'t exist!')
except:
    print("Something you specified probably doesn't exist!")



'''
for item in itens:
    item = int(item);
    data_item = data.loc[item , 'Item'];
    data_pd = data.loc[item, 'Product Description'];
    data_model = data.loc[item, 'Product Model'];
    data_pn = data.loc[item, 'P/N'];

    if(str(data_pd) != "nan"):
        QRCode = str(data_item) + '/' + str(data_model) + '/' + str(data_pd);
        filename = str(data_item) + '_' + str(data_model);

        textl1 = str(data_pd);
        textl2 = str(data_model);
        textl3 = str(data_item);
        textl4 = str(data_pn);

        adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, True);
            #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
    else:
        print('This item doesn\'t exist!')

'''