import csv
import time
import gdown
import os
import urllib.parse

def get_images():
    # Check if directory to save files exists, if not, create it
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    
    file_counter = 1
    
    with open('./urls.csv', "rt", encoding='utf-8') as infile:
        read = csv.reader(infile, delimiter=",")
        for row in read:
            print(row[1])
            if len(row) >= 2:
                words = row[1].split("=")
                if len(words) == 3:
                    print(words[2])
                    # Extract file name from URL
                    file_name = os.path.basename(urllib.parse.unquote(words[2]))
                    # Construct file path with increasing counter
                    file_path = os.path.join("downloads", f"Image-{str(file_counter).zfill(3)}.jpeg")
                    file_counter += 1
                    try:
                        gdown.download(str(row[1]), file_path, quiet=False)
                    except Exception as e:
                        print("Error:", e)
            else:
                print("Nothing")
    print("Done")

get_images()
