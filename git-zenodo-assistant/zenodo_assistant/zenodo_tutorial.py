import os
import time
from termcolor import cprint, colored

# Libraries to run Zenodo code
import requests
import json

# Library to generate metadata
import pandas as pd

# Libraries to obtain data
import tkinter as tk

from zenodo_assistant.zenodo_tools.zenodo_more import zenodo_review
from zenodo_assistant.zenodo_tools.zenodo_search import filename_input
from zenodo_assistant.zenodo_tools.zenodo_functions import type_title, type_description, creators_dict, author_check
from zenodo_assistant.zenodo_tools.zenodo_date import date_input
from zenodo_assistant.zenodo_tools.zenodo_upload import upload_options
from zenodo_assistant.zenodo_tools.zenodo_images import image_options
from zenodo_assistant.zenodo_tools.zenodo_publication import pub_options
from zenodo_assistant.zenodo_tools.zenodo_metadata import upload_metadata, image_metadata, pub_metadata, generate_md, print_md
from zenodo_assistant.zenodo_tools.zenodo_put import upload_to_zenodo


# Colored messages 
zenodo = colored('Zenodo', 'cyan')
enter = colored('Enter', 'cyan')
select = colored('Select', 'cyan')
submit = colored('Submit', 'cyan')
explore = colored('Explore', 'cyan')
done = colored('Done', 'red')
copy = colored("COPY", "green", attrs=['reverse'])
paste = colored("PASTE", "green", attrs=['reverse'])

# Welcome
welcome_message = f"""
Welcome to your {zenodo} assistant.\n
From here, you can upload a file to your {zenodo} account.
Before starting the tutorial, you should already be a little bit 
familiarized with {zenodo}. If you are not, do not worry. 
We have created a review of some of its important features, 
in case you need it.
"""

print(welcome_message)

# Zenodo review
input(f"Press {enter} to see the review. Click {done} when you finish.")
zenodo_review()
input(f"Excellent!\nLet's start the assistant to upload your file. Press {enter}.")
os.system("clear")


# Submit file
input(f"Press {enter} to open the File Browser to {select} and {submit} the file that you want to upload.\n")

open_browser = True
while open_browser == True:
    try:
        path, filename = filename_input()
        break
    except:
        print(f"You did not {submit} any file. Try again: click {explore}, pick your file and then {done}.\n")
        try:
            path, filename = filename_input()
            break
        except:
            print(f"You did not {submit} any file. Try again: click {explore}, pick your file and then {done}.\n")
            open_browser = True
        

input(f"The file has been stored. Press {enter} to continue.")
os.system("clear")

# Fill metadata
metadata_message = f"""
To upload a file to your {zenodo} account, you will need to provide some basic 
information about the work you will upload to generate the metadata.
Do not worry, you can always change it later in the website.\n
"""
print(metadata_message)

input(f"Press {enter} to start filling the information.\n")
time.sleep(1)

# Title
title = type_title()
os.system("clear")

# Description
description = type_description()
os.system("clear")

# Publication Date
input(f"Press {enter} to open the Calendar to {select} the Publication date.\n")
publication_date = date_input()
input(f"\nThe date has been stored. Press {enter} to continue.\n")
os.system("clear")

# Creators
creators_message = """
Now, you will have to fill the creators information, one by one.
Be careful of the format.
"""
print(creators_message)
input(f"Press {enter} to continue.\n")
creators = creators_dict()
os.system("clear")

# Upload type
input(f"Press {enter} to open the options menu to {select} and {submit} the type of file.\n")
open_type = True
while open_type == True: 
    try:
        upload_input = upload_options()
        break 
    except:
        print(f"You did not {submit} any option. Try again.\n")
        try:
            upload_input = upload_options()
            break
        except:
            print(f"You did not {submit} any option. Try again.\n")
            open_type = True
upload = upload_metadata(upload_input)
input(f"\nThe upload type has been stored. Press {enter} to continue.\n")
os.system("clear")

# Image type
if upload_input == "Image":
    input(f"Press {enter} to open the options menu to {select} and {submit} the type of image.\n")
    open_image = True
    while open_image == True:
        try:
            image_input = image_options()
            break
        except:
            print(f"You did not {submit} any option. Try again.\n")
            try:
                image_input = image_options()
            except:
                print(f"You did not {submit} any option. Try again.\n")
                open_image = True
                
    image = image_metadata(image_input)
    publication = "None"
    input(f"\nThe image type has been stored. Press {enter} to continue.")
    os.system("clear")

# Publication type
elif upload_input == "Publication":
    input(f"Press {enter} to open the options menu to {select} and {submit} the type of publication.\n")
    open_pub = True
    while open_pub == True:
        try:
            pub_input = pub_options()
            break
        except:
            print(f"You did not {submit} any option. Try again.\n")
            try:
                pub_input = pub_options()
                break
            except:
                print(f"You did not {submit} any option. Try again.\n")
                open_pub = True
    publication = pub_metadata(pub_input)
    image = "None"
    input(f"\nThe publication type has been stored. Press {enter} to continue.")
    os.system("clear")

# In case of different type of upload
else:
    publication = "None"
    image = "None"

# Generate metadata and show it to the user
input(f"\nYou have filled all the necessary information. "
      f"Press {enter} to generate the metadata.\n")

data = generate_md(title, description, publication_date, upload, image, publication, creators)
time.sleep(1)
md_message = """
The metadata has been generated.\n
This is the metadata corresponding to the information you just provided.\n
"""
print(md_message)
df = print_md(data)
print(df)

input(f"\nPress {enter} to continue.")
os.system("clear")

# Upload file to Zenodo

token_zenodo = colored('https://zenodo.org/account/settings/applications/tokens/new/', 'cyan')

upload_message = f"""
To upload your file, you need an authentication token. If you do not have one already,
you have to create one by logging in to your {zenodo} account and going into this page:

{token_zenodo}

You will only need a deposit:write token, but you can select all the scopes.
Remember to {copy} the token so you can {paste} it here.

When you are ready, press {enter}.

"""
input(upload_message)
upload_to_zenodo(path, filename, data)

# End message

deposit_zenodo = colored('https://zenodo.org/deposit', 'cyan')
success_message= f"""
Your file and its metadata were successfully uploaded to your {zenodo} account.
You can check it out here: 

{deposit_zenodo}

This program does not support the publication of files. By publishing a file in {zenodo},
it will go straight online and once it is published, you can no longer delete it.
My advice? I would check out my file and its metadata in the {zenodo} website carefully
before publishing.
"""

print(success_message)
input(f"\nPress {enter} to continue.")
