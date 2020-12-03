#!/usr/bin/env python3

#system level imports first
import sys
import re
import os
import itertools

#global package imports next
import gzip
import json
import requests

from datetime import datetime
from time import strptime
from datetime import date
import dateutil.parser

# specific dependency modules next
from bs4 import BeautifulSoup
from tqdm import tqdm

from random_useragent.random_useragent import Randomize
r_agent_agent = Randomize()
rm_agent = r_agent_agent.random_agent('desktop','linux')
agent = {"User-Agent":rm_agent}



class AWS:

    def get_all_images(soup):
        # print(soup.prettify())
        meta = soup.find_all('img',attrs={'class':'card-img-top'})
        # print(meta)
        urls = []
        for data in meta:
            Mystr = data["src"]
            Newstr = re.sub(r"_hu.*$", '.jpg', Mystr)
            urls.append(Newstr)
        return urls
        
    def download(url, pathname):

        # if path doesn't exist, make that path dir
        if not os.path.exists("AWSGEEK"):
            os.makedirs("AWSGEEK")
        # download the body of response by chunk, not immediately
        response = requests.get(url, stream=True)

        # get the total file size
        file_size = int(response.headers.get("Content-Length", 0))

        # get the file name
        filename = os.path.join(pathname, url.split("/")[-1])

        # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
        progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for data in progress:
                # write data read to the file
                f.write(data)
                # update the progress bar manually
                progress.update(len(data))

def aws(url):

    req = requests.get(url, agent)
    soup = BeautifulSoup(req.content, 'html.parser')
    path = "/home/sitharth/quarantine/AWSGEEK"
    
    if soup:
        all_urls = AWS.get_all_images(soup)
        # print(all_urls)
        for img in all_urls:
        # for each img, download it
            AWS.download(img, path)
    else:
        print("Soup Not Works Fine")




if __name__ == "__main__":
    

    try:
        url_input = sys.argv[1]
        print("url_input : ", url_input)
        aws(url_input)
    except IndexError:
        print("Given URL after sript")
# <img class="card-img-top" src="https://www.awsgeek.com/Zen-of-Cloud-Optimization/Zen-of-Cloud-Optimization_hu1368e4ffa06e7513186f849074288e92_1165670_320x240_resize_q75_box.jpg"/>
# https://www.awsgeek.com/
# 1
# https://www.awsgeek.com/AWS-Regions/
# https://www.awsgeek.com/AWS-Regions/AWS-Regions.jpg
# 2
# https://www.awsgeek.com/KubeCon-Virtual-2020/
# https://www.awsgeek.com/KubeCon-Virtual-2020/Day-3-Keynote/
# https://www.awsgeek.com/KubeCon-Virtual-2020/Day-3-Keynote/Day-3-Keynote.jpg
# 3
# https://www.awsgeek.com/Amazon-Textract/
# https://www.awsgeek.com/Amazon-Textract/Amazon-Textract.jpg
# 4
# https://www.awsgeek.com/Amazon-S3/
# https://www.awsgeek.com/Amazon-S3/Amazon-S3.jpg

# https://www.awsgeek.com/What-is-Cloud-Computing/What-is-Cloud-Computing.jpg/
# https://www.awsgeek.com/What-is-Cloud-Computing/What-is-Cloud-Computing.jpg
