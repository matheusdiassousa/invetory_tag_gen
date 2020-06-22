'''
import win32print as w32
import win32ui as w32ui

#local_printers = w32.EnumPrinters(2);

#print(local_printers);

zebra = w32.OpenPrinter('ZDeisgner zd220-203dpi ZPL');
info = w32.GetPrinter(zebra,1);


file_name = 'images/25_B0810-28-14-05.png';

hDC = w32ui.CreateDC();
hDC.CreatePrinterDC(zebra);
'''

import tempfile
import win32api
import win32print as w32

filename = 'D:/MDias/inventory/invetory_tag_gen/images/25_B0810-28-14-05.png';
zebra = w32.OpenPrinter('ZDesigner zd220-203dpi ZPL');
win32api.ShellExecute (
  0,
  "printto",
  filename,
  #
  # If this is None, the default printer will
  # be used anyway.
  #
  '/d:"%s"' % w32.GetDefaultPrinter (),
  ".",
  0
)

