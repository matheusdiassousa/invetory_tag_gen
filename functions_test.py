from qr_functions import *
import pandas as pd
import os
import numpy as np
from openpyxl import load_workbook

excel_file = 'input_data/Eldorado_Inventory.xlsx';

data = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
data_w = pd.read_excel(excel_file, sheet_name='withdrawal_form', skiprows=6);

book = load_workbook(excel_file);

writer = pd.ExcelWriter(excel_file, mode='a');
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


df = pd.DataFrame({
    'Product Description': data['Product Description'],
    'Item': data['Item'],
    'Product Type': data['Product Type'],
    'Type': data['Type'],
    'Product Model': data['Product Model'],
    'Owner': data['Owner'],
    'P/N': data['P/N'],
    'Unit Type': data['Unit Type'],
    'Qty': data['Qty'],
    'Supplier': data['Supplier'],
    'Manufacturer': data['Manufacturer'],
    'Client P/N': data['Client P/N'],
    'Serial Number': data['Serial Number'],
    'Lote Number': data['Lote Number'],
    'Location': data['Location'],
    'Sector': data['Sector'],
    'Machine': data['Machine'],
    'Manufactured Date': data['Manufactured Date'],
    'Expiration Date': data['Expiration Date'],
    'Rcv. Date': data['Rcv. Date'],
    'Project': data['Project'],
    'Invoice': data['Invoice'],

});

#print(df.loc[0, 'Qty'])
#df.loc[0, 'Qty'] = 55;
#print(df.loc[0, 'Qty'])

w_itens = data_w['Item'];
w_qty = data_w['Qty']
i=0;
for item in w_itens:
    print(str(item)+', '+str(w_qty[i]));
    print(str(df.loc[item,'Item'])+', '+str(df.loc[item,'Qty']))
    df.loc[item,'Qty'] = df.loc[item,'Qty'] - w_qty[i];
    print(str(df.loc[item,'Item'])+', '+str(df.loc[item,'Qty']))
    i=i+1;
    #print(item)


#print(df.loc[0, 'Qty'])



df.to_excel(writer, sheet_name = 'summary_form', index = False, header=False, startrow=7);
writer.save();



#print(item_read(811, excel_file));
#item_dataframe(excel_file);


#arroz...


'''
from qr_functions import *

file_name = "tag_test";
data_pd = "Product Description";
data_model = "Product Model";
data_item = "1000";
data_pn = "Product Part Number";
data_sn = "Product Serial Number";
delete_temp_files = False;

#adhesive_tag_100x80(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files);
#adhesive_tag_50x30(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files);
adhesive_tag_34x23(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files);
'''

#import barcode
##import treepoem #treepoem usa o ghostscript
#import code128

#code128.image("ELD-SMTMAT-CAPILLARY-CAPH85CD115-479").save("Hello World.png")  # with PIL present

##img_barcode = treepoem.generate_barcode('code128','ELD-SMTMAT-CAPILLARY-CAPH85CD115-479');
##img_barcode.convert('1').save('filename.png')
#cd128 = barcode.get_barcode_class('code128');
#codigo = cd128('ELD-SMTMAT-CAPILLARY-CAPH85CD115-479');
#fullname = codigo.save('filename');
