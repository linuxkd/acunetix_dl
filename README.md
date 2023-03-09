# acunetix_dl

Automatically download the latest version of the Acunetix web scanner

## Description

This tool will help automate the download of the latest version of the Acunetix web scanner. You will need to provide your Acunetix license key in order to download the latest version.

The tool will default to downloading the Linux version, but you can specify Windows if you need to as a command line argument.

## Requirements

- Python 3 (tested on 3.11.2)

## Installation

```bash
❯ python3 -m pip install -r requirements.txt
```

## Usage

```bash
❯ python3 acunetix_dl.py -h
usage: acunetix_dl.py [-h] -k KEY [-p PLATFORM]

Download the latest version of Acunetix

options:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     Acunetix license key
  -p PLATFORM, --platform PLATFORM
                        Platform type (Linux|Windows), Linux is default
```
