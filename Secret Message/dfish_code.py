import os
import re
def rename_photos():
    photo_list = os.listdir(r"C:\Users\JessW\Desktop\Google Drive\Udacity\Dfish")#replace with actual path of photos
    os.chdir(r"C:\Users\JessW\Desktop\Google Drive\Udacity\Dfish")#replace with actual path of photos
    for photo_name in photo_list:
        new_photo_name = re.sub('[0-9]','',photo_name)
        os.rename(photo_name, new_photo_name)
rename_photos()
