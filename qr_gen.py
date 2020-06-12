from qr_functions import *
import pandas as pd
import os
import numpy as np

#optional dependecy of pandas installed > pip install xlrd



data = pd.read_excel('input_data/text_');
col_names = data.columns.values.tolist();
noclass_values = data[col_names[1]].values;


itens = [25];

#itens = np.arange(152);

for item in itens:
    
    Label = data.loc[item , 'Label'];
    Text1 = data.loc[item, 'Text1'''];
    Text2 = data.loc[item, 'Text2'];
    Text3 = data.loc[item, 'Text3'];

    QRCode = str(data_item) + '/' + data_model + '/' + data_pd;
    filename = str(data_item) + '_' + data_model;

    textl1 = str(data_pd);
    textl2 = str(data_model);
    textl3 = str(data_item);
    textl4 = str(data_pn);

    adhesive_tag_75x25_anyText(QRCode, filename, textl1, textl2, textl3, textl4, True);
    #adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));
adhesive_tag_75x25_anyText(file_name, text1, text2, text3, f1, f2, f3, delete_temp_files):