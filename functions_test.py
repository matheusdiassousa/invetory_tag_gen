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