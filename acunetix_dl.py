#!/usr/bin/env python3

# this script will get the download link for the latest version of Acunetix
# for the given platform and download it to the current directory
# it requires the Acunetix license key as an argument

# Author: @linuxkd

import requests
import json
import argparse
import rich

# parse the command line arguments
parser = argparse.ArgumentParser(description="Download the latest version of Acunetix")
parser.add_argument("-k", "--key", help="Acunetix license key", required=True)
parser.add_argument(
    "-p", "--platform", help="Platform type (Linux|Windows), Linux is default", required=False, default="Linux"
)
args = parser.parse_args()

# the base URL of the Acunetix download page
url = "https://updates.acunetix.com/"

# if args.platform is Windows, then we need to add the Windows path
if args.platform == "Windows":
    url += "w14"

# if args.platform is Linux, then we need to add the Linux path
# this is the default
else:
    url += "l14"

# the POST data
data = {
    "license_key": args.key,
    "name": "John Doe",
    "company": "Acme Inc.",
    "email": "jdoe@example.com",
    "phone": "555-555-5555",
    "country": "US",
}

# the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Origin": "https://www.acunetix.com",
}

# send the POST request
try:
    rich.print("[bold green]Sending POST request to Acunetix download page...[/bold green]")
    r = requests.post(url, data=data, headers=headers)
except Exception as e:
    rich.print(f"[bold red]Error: {e}[/bold red]")
    exit()

# get the download link and filename
download_link = json.loads(r.text)["link"]
filename = json.loads(r.text)["file_name"]

try:
    # download the file
    rich.print(f"[bold green]Downloading {filename}...[/bold green]")
    r = requests.get(download_link)
except Exception as e:
    rich.print(f"[bold red]Error: {e}[/bold red]")
    exit()

# save the file
with open(filename, "wb") as f:
    f.write(r.content)
