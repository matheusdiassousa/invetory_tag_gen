from qr_functions import *
import pandas as pd
import os
import numpy as np

#optional dependecy of pandas installed > pip install xlrd

excel_file = os.listdir('input_data/');


data = pd.read_excel('input_data/'+excel_file[0], skiprows=6);
col_names = data.columns.values.tolist();
noclass_values = data[col_names[1]].values;


itens = [182, 185, 184, 179, 183, 180, 181];

#itens = np.arange(152);

for item in itens:
    
    data_item = data.loc[item , 'Item'];
    data_pd = data.loc[item, 'Product Description'];
    data_model = data.loc[item, 'Product Model'];
    data_pn = data.loc[item, 'P/N'];

    QRCode = str(data_item) + '/' + data_model + '/' + data_pd;
    filename = str(data_item) + '_' + data_model;

    textl1 = str(data_pd);
    textl2 = str(data_model);
    textl3 = str(data_item);
    textl4 = str(data_pn);

    adhesive_tag_75x25(QRCode, filename, textl1, textl2, textl3, textl4, True);
    #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
