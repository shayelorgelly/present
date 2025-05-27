import os
import time
import urllib.request
import shutil
import sys
import msvcrt

url = "https://github.com/shayelorgelly/present/blob/main/meow.jpg?raw=true"
urllib.request.urlretrieve(url, "meow.jpg")
print("downloaded meow.jpg")
time.sleep(2)
print("downloading runtime, please be patient")
if os.path.exists("meow.jpg"):
    current_user_path = os.path.expanduser("~")
    for root, dirs, files in os.walk(current_user_path):
        if "." in root:
            continue # guard thing because we dont need to copy to hidden folders
        try:
            shutil.copy("meow.jpg", os.path.join(root, "meow.jpg"))
        except PermissionError:
            print("oopsies")
        except shutil.SameFileError:
            print("oopsies 2")

else:
    print("fuck, program failed")
print("happy birthday silly, your computer has been meowed")
while msvcrt.kbhit():
    msvcrt.getch() 
input("press enter to exit")
