import win32api as w32
import os
import subprocess

file_path = "D:\MDias\inventory\invetory_tag_gen\images\25_B0810-28-14-05.png";

#w32.ShellExecute(0,'ls -l','','','c:',0)

#print('ls -l')
process=subprocess.Popen(["powershell.exe", "Start-Process -FilePath D:\MDias\inventory\invetory_tag_gen\images"+"\\"+"25_B0810-28-14-05.png -Verb Print"], shell=True ,stdout=subprocess.PIPE);

#subprocess.Popen('powershell.exe Start-Process -FilePath' + 'D:\MDias\inventory\invetory_tag_gen\images'+'\\'+ '25_B0810-28-14-05.png'+ '-Verb Print');
result=process.communicate()[0]
print(result)


#Start-Process -FilePath "D:\MDias\inventory\invetory_tag_gen\images\25_B0810-28-14-05.png" -Verb Print
