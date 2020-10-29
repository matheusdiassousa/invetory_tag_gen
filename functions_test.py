from qr_functions import *
import pandas as pd
import os
import numpy as np

excel_file = 'input_data/Eldorado_Inventory.xlsx';

item_dataframe(excel_file);





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
