import pandas as pd
import os
import numpy as np
from openpyxl import load_workbook

#optional dependecy of pandas installed > pip install xlrd

excel_file = 'input_data/Eldorado_Inventory.xlsx';


data_inventory = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
data_withdrawal = pd.read_excel(excel_file, sheet_name='withdrawal_form', skiprows=6);

col_inventory = data_inventory.columns.values.tolist();
print(col_inventory)
col_withdrawal = data_withdrawal.columns.values.tolist();

'''-----------------------'''
inv_item = [];
inventory_Item = data_inventory[col_inventory[1]].values;
inventory_PN = data_inventory[col_inventory[5]].values;
withdrawal_PN = data_withdrawal[col_withdrawal[0]].values;

print(inventory_Item)
for item in inventory_Item:
    if(str(data_inventory.loc[item, 'Product Description']) != 'nan'):
        inv_item.append(inventory_Item[item]);

inventory_Item = inv_item;
'''-----------------------'''

sum_descr = ['']*len(inventory_Item);
sum_pn = ['']*len(inventory_Item);
sum_unit = ['']*len(inventory_Item);
sum_tqty = np.zeros(len(inventory_Item));
sum_fqty = np.zeros(len(inventory_Item));
sum_flag_gen = np.zeros(len(inventory_Item));
sum_flag_pj1 = np.zeros(len(inventory_Item));
sum_flag_pj2 = np.zeros(len(inventory_Item));
sum_flag_pj3 = np.zeros(len(inventory_Item));
sum_flag_pj4 = np.zeros(len(inventory_Item));

qty_generalUse = [];
qty_project1 = [];
qty_project2 = [];
qty_project3 = [];
qty_project4 = [];
qty_var = [];

for item in inventory_Item:
    sum_descr[item] = data_inventory.loc[item, 'Product Description'];
    sum_pn[item] = data_inventory.loc[item, 'P/N'];
    sum_unit[item] = data_inventory.loc[item, 'Unit Type'];
    sum_tqty[item] = data_inventory.loc[item, 'Qty'];

    i = 0;
    for with_item_PN in withdrawal_PN:
        
        
        if ( with_item_PN == sum_pn[item] ):
            try:                
                sum_flag_gen[item] += int(data_withdrawal.loc[i, 'General Use']);
            except:
                sum_flag_gen[item] += 0;
            try:                
                sum_flag_pj1[item] += int(data_withdrawal.loc[i, 'Project_1']);
            except:
                sum_flag_pj1[item] += 0;
            try:                
                sum_flag_pj2[item] += int(data_withdrawal.loc[i, 'Project_2']);
            except:
                sum_flag_pj2[item] += 0;
            try:                
                sum_flag_pj3[item] += int(data_withdrawal.loc[i, 'Project_3']);
            except:
                sum_flag_pj3[item] += 0;
            try:                
                sum_flag_pj4[item] += int(data_withdrawal.loc[i, 'Project_4']);
            except:
                sum_flag_pj4[item] += 0;                                 

            qty_var = sum_flag_gen[item] + sum_flag_pj1[item] + sum_flag_pj2[item] + sum_flag_pj3[item] + sum_flag_pj4[item];
            sum_fqty[item] =  int(data_inventory.loc[item, 'Qty']) - qty_var;
            #sum_flag_gen.append(data_withdrawal.loc[i, 'General Use']);
            #sum_flag_pj1.append(data_withdrawal.loc[i, 'Project_1']);
            #sum_flag_pj2.append(data_withdrawal.loc[i, 'Project_2']);
            #sum_flag_pj3.append(data_withdrawal.loc[i, 'Project_3']);
            #sum_flag_pj4.append(data_withdrawal.loc[i, 'Project_4']);
            
            #qty_generalUse = 0;
            #qty_project1 = 0;
            #qty_project2 = 0;
            #qty_project3 = 0;
            #qty_project4 = 0;
            qty_var = 0;
            i+=1;

        else:
            sum_flag_gen[item] = 0;
            sum_flag_pj1[item] = 0;
            sum_flag_pj2[item] = 0;
            sum_flag_pj3[item] = 0;
            sum_flag_pj4[item] = 0;
            sum_fqty[item] = data_inventory.loc[item, 'Qty'];

i = 0;
for item in inventory_Item:
    print(sum_descr[item], sum_pn[item], sum_unit[item], sum_tqty[item], sum_fqty[item], sum_flag_gen[item], sum_flag_pj1[item], sum_flag_pj2[item], sum_flag_pj3[item], sum_flag_pj4[item]);
    i+=1;
    
book = load_workbook(excel_file);

writer = pd.ExcelWriter(excel_file, mode='a');
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)


df = pd.DataFrame({
    'Description': sum_descr,
    'P/N': sum_pn,
    'Unit': sum_unit,
    'Total Qty': sum_tqty,
    'Free Qty': sum_fqty,    
    'General Use (Qty)': sum_flag_gen,
    'Project_1 (Qty)': sum_flag_pj1,
    'Project_2 (Qty)': sum_flag_pj2,
    'Project_3 (Qty)': sum_flag_pj3,
    'Project_4 (Qty)': sum_flag_pj4,            
});



df.to_excel(writer, sheet_name = 'summary_form', index = False, header=False, startrow=7);
writer.save();

