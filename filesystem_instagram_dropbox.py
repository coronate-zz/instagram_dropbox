import dropbox
from os import walk, remove
import datetime
import datetime
import os.path, time
import pdb
import random
from InstagramAPI import InstagramAPI
from PIL import Image
from utils import *

def instargram_rename_upload(selected_folder, selected_photo):
    country = selected_folder.name
    date = selected_photo.client_modified
    date = str(date)
    return country + ". " + date


def random_hashtag_list(all_hashtags, n):
    hashtags_choice =list()
    hashtags = list(set(all_hashtags.copy()))
    while len(hashtags_choice) < n:
        hash=random.choice(hashtags)
        hashtags_choice.append(hash)
        hashtags.remove(hash)
    return  hashtags_choice


def str_hashtag_choice(hashtags_choice):
    str_hash = ""
    for hash in hashtags_choice:
        str_hash += "#" + hash +" "
    return str_hash

#Token inside app management
dbx = dropbox.Dropbox(dropbox_access_token)
dbx.users_get_current_account()

today = datetime.datetime.now()
min_date = today
print("Today's date:", today)
response_foldersinApp = dbx.files_list_folder("")

#CRONOLOGICAL UPLOAD
for folder in response_foldersinApp.entries:
    if folder.name == "Uploaded":
        continue
    response_photosinfolder = dbx.files_list_folder("/"+folder.name)
    for photo in response_photosinfolder.entries:
        date_photo = photo.client_modified
        print("\nFolder: {}\n\tphoto_name: {} photo_date: {} ".format(folder.name, photo.name, photo.client_modified))
        if date_photo < min_date:
            min_date = date_photo
            selected_folder = folder
            selected_photo =  photo
            print("\n\t\t**** Selected_folder: {} \n\t selected_photo: {}  ****\n".format(selected_folder.name, selected_photo.name))


instagram_photo_name = instargram_rename_upload(selected_folder, selected_photo)
photo_to_download_path = "/" + selected_folder.name + "/" + selected_photo.name
instagram_photo_name_path = instagram_photo_name[:-9]+".jpg" #many photos can have the same date
dbx.files_download_to_file(instagram_photo_name_path, photo_to_download_path )


#INSTAGRAM API
api = InstagramAPI(instagram_user, instagram_password)
#api = InstagramAPI("divina__narvaez", "zomondoca")

api.login()  # login
caption = instagram_photo_name

#ADD CAPTION DETAILS LIKE HASHTAGS
random.seed(random.randint(1, 1000))
hashtags_choice = random_hashtag_list(all_hashtags, 5)
hashtags_str = str_hashtag_choice(hashtags_choice)
caption += "\n" + hashtags_str


image = Image.open(instagram_photo_name_path)
image = image.resize((1080,608),Image.ANTIALIAS)
#instagram_photo_lowdetail = instagram_photo_name_path.replace(".jpg", "")+ "_lowdetail.jpg"
image.save("lowdetail.jpeg")

#UPLOAD
api.uploadPhoto("lowdetail.jpeg", caption=caption)



#AFTER USING CHANGE PHOTO LOCATION
with open(instagram_photo_name_path, "rb") as f:
    try:
        dbx.files_upload(f.read(), '/Uploaded/' + selected_folder.name + "/" + instagram_photo_name+".jpg", mute = True)
    except Exception as e:
        print(e)
        dbx.files_create_folder("/Uploaded/" + selected_folder.name)  
        dbx.files_upload(f.read(), '/Uploaded/' + selected_folder.name + "/" + instagram_photo_name+".jpg", mute = True)

#DELETE PHOTO IN DROPBOX ORIGINAL FOLDER
dbx.files_delete(photo_to_download_path)
remove("lowdetail.jpeg")
remove(instagram_photo_name_path)