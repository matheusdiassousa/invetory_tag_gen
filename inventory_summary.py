import pandas as pd
import os
import numpy as np
from openpyxl import load_workbook
import math

#optional dependency of pandas installed > pip install xlrd
#installed dependency -> openpyxl

excel_file = 'input_data/Eldorado_Inventory.xlsx';


data_inventory = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
data_withdrawal = pd.read_excel(excel_file, sheet_name='withdrawal_form', skiprows=6);

col_inventory = data_inventory.columns.values.tolist();
#print(col_inventory);
col_withdrawal = data_withdrawal.columns.values.tolist();
#print(col_withdrawal);

'''-----------------------'''
inv_item = [];
inv_quty = [];
inv_fqty = [];
inv_PN = [];
inv_desc = [];
inv_unit = [];
inv_gu = [];
inv_pj1 = [];
inv_pj2 = [];
inv_pj3 = [];
inv_pj4 = [];

#col_inventory[0] -> Description
#col_inventory[1] -> Item
#col_inventory[5] -> Part Number
#col_inventory[6] -> Unit
#col_inventory[7] -> Qty
inventory_desc = data_inventory[col_inventory[0]].values;
inventory_Item = data_inventory[col_inventory[1]].values;
#print(inventory_Item);
inventory_PN = data_inventory[col_inventory[6]].values;
inventory_unit = data_inventory[col_inventory[7]].values;
inventory_qty = data_inventory[col_inventory[8]].values;

for item in inventory_Item:
    
    #if(str(data_inventory.loc[item, 'Product Description']) != 'nan'):
    if(not math.isnan(item)):
        item = int(item);
        inv_item.append(inventory_Item[item]);
        inv_quty.append(inventory_qty[item]);
        inv_fqty.append(inventory_qty[item]);
        inv_PN.append(inventory_PN[item]);
        inv_desc.append(inventory_desc[item]);
        inv_unit.append(inventory_unit[item]);
        inv_gu.append(0);
        inv_pj1.append(0);
        inv_pj2.append(0);
        inv_pj3.append(0);
        inv_pj4.append(0);


i = 0;
#for item in inv_item:
#    print(inv_item[i], inv_PN[i], inv_quty[i]);
#    i+=1;


w_pn = [];
w_gu = [];
w_pj1 = [];
w_pj2 = [];
w_pj3 = [];
w_pj4 = [];

with_pn = data_withdrawal[col_withdrawal[0]].values;
with_gu = data_withdrawal[col_withdrawal[6]].values;
with_pj1 = data_withdrawal[col_withdrawal[7]].values;
with_pj2 = data_withdrawal[col_withdrawal[8]].values;
with_pj3 = data_withdrawal[col_withdrawal[9]].values;
with_pj4 = data_withdrawal[col_withdrawal[10]].values;



i = 0;
for item in with_pn:
    if( str(with_pn[i]) != 'nan' ):
        w_pn.append(with_pn[i]);
        w_gu.append(with_gu[i]);
        w_pj1.append(with_pj1[i]);
        w_pj2.append(with_pj2[i]);
        w_pj3.append(with_pj3[i]);
        w_pj4.append(with_pj4[i]);
    i+=1;



i = 0;
for item in with_pn:
    if( math.isnan(w_gu[i]) ):
        w_gu[i] = 0;
    if( math.isnan(w_pj1[i]) ):
        w_pj1[i] = 0;
    if( math.isnan(w_pj2[i]) ):
        w_pj2[i] = 0;
    if( math.isnan(w_pj3[i]) ):
        w_pj3[i] = 0;
    if( math.isnan(w_pj4[i]) ):
        w_pj4[i] = 0;

    print(w_pn[i], w_gu[i], w_pj1[i], w_pj2[i], w_pj3[i], w_pj4[i]);
    i+=1;

i = 0;
for item_inv in inv_PN:
    j = 0;
    for item_with in w_pn:
        if( with_pn[j] == item_inv ):
            inv_fqty[i] = inv_fqty[i] - w_gu[j] - w_pj1[j] - w_pj2[j] - w_pj3[j] - w_pj4[j];
            inv_gu[i] = inv_gu[i] + w_gu[j];
            inv_pj1[i] = inv_pj1[i] + w_pj1[j];
            inv_pj2[i] = inv_pj2[i] + w_pj2[j];
            inv_pj3[i] = inv_pj3[i] + w_pj3[j];
            inv_pj4[i] = inv_pj4[i] + w_pj4[j];
        j+=1;
    i+=1;


i=0;
for item in inv_item:
    print(inv_item[i], inv_desc[i], inv_PN[i], inv_unit[i], inv_quty[i], inv_fqty[i], inv_gu[i], inv_pj1[i], inv_pj2[i], inv_pj3[i], inv_pj4[i]);
    i+=1;


book = load_workbook(excel_file);

writer = pd.ExcelWriter(excel_file, mode='a');
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


df = pd.DataFrame({
    'Description': inv_desc,
    'P/N': inv_PN,
    'Unit': inv_unit,
    'Total Qty': inv_quty,
    'Free Qty': inv_fqty,
    'General Use (Qty)': inv_gu,
    'P&D (Qty)': inv_pj1,
    'uMCP (Qty)': inv_pj2,
    'UFS (Qty)': inv_pj3,
    'Project_2 (Qty)': inv_pj4,
});



df.to_excel(writer, sheet_name = 'summary_form', index = False, header=False, startrow=7);
writer.save();
