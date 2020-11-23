# Author: Matheus Dias Sousa
# Instituto de Pesquisas Eldorado
# Funções para gerar arquivos .png das etiquetas em diferentes dimensões de produtos cadastrados na planilha Eldorado_Inventory.xlsx 


from pyqrcode import QRCode
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import code128
from resizeimage import resizeimage
#from barcode import 128



#bibliotecas instaladas -> pyqrcode, pypng, pandas, Pillow e matplotlib
#deletar a imagem depois de visualizada set -> delete_file = True

#delete_temp_files = True;


def adhesive_tag_75x25(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files):
    size = "75x25";
    qrcode = QRCode(data_pn); #Gera o Qr Code com os dados vindos do campo part number da planilha do inventório
    qrcode.png('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png', scale=6); #Salva o qr code gerado no caminho indicado

    qrcode_img = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');
    qrcode_img.thumbnail((210,210));
    qrcode_img.save('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');
    qrcode_img_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');

    eld_logo = Image.open('images/base_imgs_'+size+'/logo_eldorado_597x160.png');
    eld_logo.thumbnail((250, 250));
    eld_logo.save('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');

    background_75x25 = Image.open('images/base_imgs_'+size+'/75x25_background.png');
    img_mounting = background_75x25.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (60) , (30) );
    qrcode_img_pos = ( (int(background_75x25.width) - int(qrcode_img_resized.width) - 15) , ( int(background_75x25.height/2) - int(qrcode_img_resized.height/2) ));
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);
    


    img_mounting.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 19);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 18);
    t1.text( (5,90), data_pd, font = textFont, fill=(0,0,0));
    t1.text( (5,120), 'P/M: ' + data_model, font = textFont, fill=(0,0,0));
    t1.text( (5,140), data_pn, font = text2Font, fill=(0,0,0));
    t1.text( (5,160), 'S/N: ' + data_sn, font = text2Font, fill=(0,0,0));

    qr_img.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags/' + file_name + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');

    else:
        pass;


def adhesive_tag_100x80(file_name, data_pd, data_model, data_item, data_pn, data_sn, data_qty, data_expdate, delete_temp_files):
    size = "100x80";
    qrcode = QRCode(data_pn+','+data_qty); #Gera o Qr Code com os dados vindos do campo part number da planilha do inventório
    qrcode.png('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png', scale=6); #Salva o qr code gerado no caminho indicado

    qrcode_img = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png'); #abre a img de qrcode gerada e salva
    qrcode_img.thumbnail((210,210)); #redimensiona para 210p por 210p
    qrcode_img.save('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #salva o qrcode redimensionado
    qrcode_img_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #reabre a imagem redimensionada 

    eld_logo = Image.open('images/base_imgs_'+size+'/logo_eldorado_597x160.png'); #
    #eld_logo.thumbnail((250, 250)); 
    #eld_logo.save('images/base_imgs_100x80/temp_imgs/eld_logo_resized.png');
    #eld_logo_resized = Image.open('images/base_imgs_100x80/temp_imgs/eld_logo_resized.png');

    background_100x80 = Image.open('images/base_imgs_'+size+'/100x80_background.png');
    img_mounting = background_100x80.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (200) , (100) );
    qrcode_img_pos = ( (int(background_100x80.width) - int(qrcode_img_resized.width) - 280) , ( int(background_100x80.height/2) - int(qrcode_img_resized.height/2)+270 ));
    img_mounting.paste(eld_logo, eld_logo_pos, eld_logo);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);
    


    img_mounting.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 20);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 24);
    t1.text( (20,220), data_pd, font = textFont, fill=(0,0,0));
    t1.text( (20,250), 'P/M: ' + data_model, font = text2Font, fill=(0,0,0));
    t1.text( (20,280), data_pn, font = text2Font, fill=(0,0,0));
    t1.text( (20,310), 'S/N: ' + data_sn, font = text2Font, fill=(0,0,0));
    t1.text( (20,340), 'Qty: ' + data_qty, font = text2Font, fill=(0,0,0));
    t1.text( (20,370), 'Exp. Date: ' + data_expdate, font = text2Font, fill=(0,0,0));

    qr_img.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags/' + file_name + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        #os.remove('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');

    else:
        pass;


def adhesive_tag_50x30(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files):
    size = "50x30";
    qrcode = QRCode(data_pn); #Gera o Qr Code com os dados vindos do campo part number da planilha do inventório
    qrcode.png('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png', scale=6); #Salva o qr code gerado no caminho indicado

    qrcode_img = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png'); #abre a img de qrcode gerada e salva
    qrcode_img.thumbnail((190,190)); #redimensiona para 210p por 210p
    qrcode_img.save('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #salva o qrcode redimensionado
    qrcode_img_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #reabre a imagem redimensionada 

    eld_logo = Image.open('images/base_imgs_'+size+'/logo_eldorado_597x160.png'); #
    eld_logo.thumbnail((250, 250)); 
    eld_logo.save('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');

    background_50x30 = Image.open('images/base_imgs_'+size+'/50x30_background.png');
    img_mounting = background_50x30.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (125) , (25) );
    qrcode_img_pos = ( (int(background_50x30.width) - int(qrcode_img_resized.width)+5) , ( int(background_50x30.height/2) - int(qrcode_img_resized.height/2)+50 ));
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);
    


    img_mounting.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 19);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 19);
    t1.text( (15,140), data_pd, font = textFont, fill=(0,0,0));
    t1.text( (15,165), 'P/M: ' + data_model, font = textFont, fill=(0,0,0));
    t1.text( (15,190), data_pn, font = text2Font, fill=(0,0,0));
    t1.text( (15,215), 'S/N: ' + data_sn, font = text2Font, fill=(0,0,0));

    qr_img.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags/' + file_name + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');

    else:
        pass;


def adhesive_tag_34x23(file_name, data_pd, data_model, data_item, data_pn, data_sn, delete_temp_files):
    size = "34x23";
    code128.image(data_item).save('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');
    #qrcode = QRCode(data_pn); #Gera o Qr Code com os dados vindos do campo part number da planilha do inventório
    #qrcode.png('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png', scale=6); #Salva o qr code gerado no caminho indicado

    qrcode_img = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png'); #abre a img de qrcode gerada e salva
    im_resized = resizeimage.resize_cover(qrcode_img, [210,50], validate=False);
    #im1 = qrcode_img.resize((20,20), resample=3); #redimensiona para 210p por 210p
    im_resized.save('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #salva o qrcode redimensionado
    qrcode_img_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png'); #reabre a imagem redimensionada 

    eld_logo = Image.open('images/base_imgs_'+size+'/logo_eldorado_597x160.png'); #
    eld_logo.thumbnail((220, 220)); 
    eld_logo.save('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');

    background_34x23 = Image.open('images/base_imgs_'+size+'/34x23_background.png');
    img_mounting = background_34x23.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (60) , (12) );
    qrcode_img_pos = ( (int(background_34x23.width) - int(qrcode_img_resized.width)-65) , ( int(background_34x23.height/2) - int(qrcode_img_resized.height/2)-12 ));
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);
    


    img_mounting.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 15);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 17);
    t1.text( (10,130), data_pd, font = textFont, fill=(0,0,0));
    t1.text( (10,150), 'P/M: ' + data_model, font = text2Font, fill=(0,0,0));
    t1.text( (10,170), data_pn, font = text2Font, fill=(0,0,0));
    t1.text( (10,190), 'S/N: ' + data_sn, font = text2Font, fill=(0,0,0));


    qr_img.save('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags/' + data_item + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/base_imgs_'+size+'/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode_resized.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/' + file_name + '.png');
        os.remove('images/base_imgs_'+size+'/temp_imgs/'+data_item+'_qrcode.png');

    else:
        pass;
def adhesive_102x23uniter(item):
    for(i in item):
        lista = len(item)
        if(len(item) = 3):
            
        


def adhesive_tag_composition_102x23(img1, img2, img3):
    size = "34x23";
    background_102x23 = Image.open('images/base_imgs_'+size+'/102x23_background.png');
    img_mounting = background_102x23.copy();

    img1open = Image.open('images/gen_tags/'+str(img1)+'.png');
    img2open = Image.open('images/gen_tags/'+str(img2)+'.png');
    img3open = Image.open('images/gen_tags/'+str(img3)+'.png');

    img1_pos = ( (0) , (1) );
    img2_pos = ( (339) , (1) );
    img3_pos = ( (679) , (1) );

    img_mounting.paste(img1open, img1_pos);
    img_mounting.paste(img2open, img2_pos);
    img_mounting.paste(img3open, img3_pos);

    img_mounting.save('images/gen_tags/'+str(img1)+str(img2)+str(img3)+'.png');


def item_read(item, excel_file):
    
    data = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
    
    pdes = str(data.loc[item, 'Product Description']);
    ptype = str(data.loc[item, 'Product Type']);
    p_type = str(data.loc[item, 'Type']);
    pmodel = str(data.loc[item, 'Product Model']);
    powner = str(data.loc[item, 'Owner']);
    pn = str(data.loc[item, 'P/N']);
    unit = str(data.loc[item, 'Unit Type']);
    qty = str(data.loc[item, 'Qty']);
    supplier = data.loc[item, 'Supplier'];
    manufacturer = data.loc[item, 'Manufacturer'];
    clienpn = data.loc[item, 'Client P/N'];
    serialnumber = data.loc[item, 'Serial Number'];
    location = data.loc[item, 'Location'];
    sector = data.loc[item, 'Sector'];
    machine = data.loc[item, 'Machine'];
    manufdate = data.loc[item, 'Manufactured Date'];
    expdate = data.loc[item, 'Expiration Date'];
    rcvdate = data.loc[item, 'Rcv. Date'];
    project = data.loc[item, 'Project'];
    invoice = data.loc[item, 'Invoice'];

    item_info = [pdes, ptype, p_type, pmodel, powner, pn, unit, qty, supplier, manufacturer, clienpn, serialnumber, location, sector, machine, manufdate, expdate, rcvdate, project, invoice];

    return item_info

def item_dataframe(excel_file):
    data = pd.read_excel(excel_file, sheet_name='inventory_form', skiprows=6);
    col_names = data.columns.values.tolist();

    
    pdes = data['Product Description'];
    item = data['Item'];
    ptype = data['Product Type'];
    p_type = data['Type'];
    pmodel = data['Product Model'];
    powner = data['Owner'];
    pn = data['P/N'];
    unit = data['Unit Type'];
    qty = data['Qty'];
    supplier = data['Supplier'];
    manufacturer = data['Manufacturer'];
    clientpn = data['Client P/N'];
    serialnumber = data['Serial Number'];
    location = data['Location'];
    sector = data['Sector'];
    machine = data['Machine'];
    manufdate = data['Manufactured Date'];
    expdate = data['Expiration Date'];
    rcvdate = data['Rcv. Date'];
    project = data['Project'];
    invoice = data['Invoice'];

    item_info = [pdes, item, ptype, p_type, pmodel, powner, pn, unit, qty, supplier, manufacturer, 
                clientpn, serialnumber, location, sector, machine, manufdate, expdate, rcvdate, project, invoice];

    return 



    


def item_write(item):
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

    df.to_excel(writer, sheet_name = 'summary', index = False, header=False, startrow=7);
    writer.save();



    #print(item, pdes, ptype, p_type, pmodel, powner, pn, unit, qty, supplier, manufacturer, clienpn, serialnumber, location, sector, machine, manufdate, expdate, rcvdate, project, invoice)


    #data_pd = data.loc[item, 'Product Description'];
