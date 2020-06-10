from qr_functions import *
import pandas as pd

#optional dependecy of pandas installed > pip install xlrd

data = pd.read_excel('input_data/Eldorado_Inventory_09062020.xlsm', skiprows=6);
col_names = data.columns.values.tolist();
noclass_values = data[col_names[1]].values;
#print(noclass_values);
#print(col_names[1]);

#print(data.loc[ 8 ,['Item', 'Product Description']]);

numb_item = 25;

data_item = data.loc[numb_item , 'Item'];
data_pd = data.loc[numb_item, 'Product Description'];
data_model = data.loc[numb_item, 'Product Model'];

filename = str(data_item) + '_' + data_model;

#adhesive_tag_75x25(str(data_item) + '/' + data_model + '/' + data_pd, filename, True, str(data_pd), str(data_model), str(data_item));
adhesive_tag_75x25(str('19801ade-3f7e-4195-9e25-9b112021eacd'), filename, True, str(data_pd), str(data_model), str(data_item));