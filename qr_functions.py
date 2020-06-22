from pyqrcode import QRCode
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd




#bibliotecas instaladas -> pyqrcode, pypng, pandas, Pillow e matplotlib
#deletar a imagem depois de visualizada set -> delete_file = True

#delete_temp_files = True;


def adhesive_tag_75x25(data, file_name, data_pd, data_model, data_item, data_pn, delete_temp_files):
    qrcode = QRCode(data_pn);
    qrcode.png('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode.png', scale=6);

    qrcode_img = Image.open('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode.png');
    qrcode_img.thumbnail((222,222));
    qrcode_img.save('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode_resized.png');
    qrcode_img_resized = Image.open('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode_resized.png');

    eld_logo = Image.open('images/base_imgs_75x25/logo_eldorado_597x160.png');
    eld_logo.thumbnail((250, 250));
    eld_logo.save('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');

    background_75x25 = Image.open('images/base_imgs_75x25/75x25_background.png');
    img_mounting = background_75x25.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (60) , (30) );
    qrcode_img_pos = ( (int(background_75x25.width) - int(qrcode_img_resized.width) - 15) , ( int(background_75x25.height/2) - int(qrcode_img_resized.height/2) ));
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);
    


    img_mounting.save('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 22);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 20);
    t1.text( (5,90), data_pd, font = textFont, fill=(0,0,0));
    t1.text( (5,120), 'P/M: ' + data_model, font = textFont, fill=(0,0,0));
    t1.text( (5,150), data_pn, font = text2Font, fill=(0,0,0));

    qr_img.save('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_75x25/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags_75x25/' + file_name + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode_resized.png');
        os.remove('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
        os.remove('images/base_imgs_75x25/temp_imgs/'+data_item+'_qrcode.png');

    else:
        pass;




def adhesive_tag_75x25_anyText(file_name, text1, text2, text3, f1, f2, f3, delete_temp_files):
        
    eld_logo = Image.open('images/base_imgs_75x25/logo_eldorado_597x160.png');
    eld_logo.thumbnail((250, 250));
    eld_logo.save('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');

    background_75x25 = Image.open('images/base_imgs_75x25/75x25_background.png');
    img_mounting = background_75x25.copy();

    #eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2) - 40) , (15) );
    eld_logo_pos = ( (60) , (30) );
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    
    img_mounting.save('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');

    qr_img = Image.open('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
    qr_img.thumbnail((595, 595));
    
    t1 = ImageDraw.Draw(qr_img);
    textFont = ImageFont.truetype('fonts/ARIALNB.TTF', 22);
    text2Font = ImageFont.truetype('fonts/ARIALNB.TTF', 20);
    t1.text( (50,90), text1, font = textFont, fill=(0,0,0));
    t1.text( (50,120), text2, font = textFont, fill=(0,0,0));
    t1.text( (50,150), text3, font = textFont, fill=(0,0,0));

    qr_img.save('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
    qr_img = Image.open('images/base_imgs_75x25/temp_imgs/' + file_name + '.png').convert('LA');
    qr_img.save('images/gen_tags_75x25/' + file_name + '.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/base_imgs_75x25/temp_imgs/eld_logo_resized.png');
        os.remove('images/base_imgs_75x25/temp_imgs/' + file_name + '.png');
        

    else:
        pass;
