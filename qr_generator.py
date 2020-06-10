import pyqrcode
from pyqrcode import QRCode
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
import os
from PIL import Image

#bibliotecas instaladas -> pyqrcode, pypng, pandas, Pillow e matplotlib
#deletar a imagem depois de visualizada set -> delete_file = True

delete_temp_files = True;

qrcode = QRCode('arroz com feijão #12115132523523523526299@@..//');
qrcode.png('images/qrcode_file.png', scale=6);


#img = pltimg.imread('images/qrcode_file.png');
#img_plot = plt.imshow(img, cmap='gray');
#plt.show()

def adhesive_tag_75x25():
    qrcode_img = Image.open('images/qrcode_file.png');
    qrcode_img.thumbnail((222,222));
    qrcode_img.save('images/qrcode_file_resized.png');
    qrcode_img_resized = Image.open('images/qrcode_file_resized.png');

    eld_logo = Image.open('images/logo_eldorado_597x160.png');
    eld_logo.thumbnail((190, 190));
    eld_logo.save('images/eld_logo_resized.png');
    eld_logo_resized = Image.open('images/eld_logo_resized.png');

    background_75x25 = Image.open('images/75x25_background.png');
    img_mounting = background_75x25.copy();

    eld_logo_pos = ( (int(background_75x25.width/2) - int(eld_logo_resized.width/2)) , (0) );
    qrcode_img_pos = ( (int(background_75x25.width) - int(qrcode_img_resized.width) - 25) , ( int(background_75x25.height/2) - int(qrcode_img_resized.height/2) ));
    img_mounting.paste(eld_logo_resized, eld_logo_pos, eld_logo_resized);
    img_mounting.paste(qrcode_img_resized, qrcode_img_pos);


    img_mounting.save('images/mounted_img_75x25.png');




    #imgpil.show()
    if(delete_temp_files == True):
        os.remove('images/eld_logo_resized.png');
        os.remove('images/qrcode_file_resized.png');


adhesive_tag_75x25();


'''PILLOW - Changing Image Type
image = Image.open('unsplash_01.jpg')
image.save('new_image.png')

PILLOW - Resizing an Image

image = Image.open('unsplash_01.jpg')
new_image = image.resize((400, 400))
new_image.save('image_400.jpg')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)

Resizing an Image and keeping the aspect ratio

image = Image.open('unsplash_01.jpg')
image.thumbnail((400, 400))
image.save('image_thumbnail.jpg')

'''