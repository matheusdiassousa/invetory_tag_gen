# Author: Matheus Dias Sousa
# Instituto de Pesquisas Eldorado
# Algoritmo para balanço de entrada e saída dos materiais

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


w_itens = data_w['Item'];
w_qty = data_w['Qty']
i=0;
for item in w_itens:
    print(str(item)+', '+str(w_qty[i]));
    print(str(df.loc[item,'Item'])+', '+str(df.loc[item,'Qty']))
    df.loc[item,'Qty'] = df.loc[item,'Qty'] - w_qty[i];
    print(str(df.loc[item,'Item'])+', '+str(df.loc[item,'Qty']))
    i=i+1;


df.to_excel(writer, sheet_name = 'summary_form', index = False, header=False, startrow=7);
writer.save();


