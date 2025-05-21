# Object Downloader

A script that downloads all files from a specified S3 bucket.

## Installation & setup

1. Create a new virtual environment
2. Install all packages (`pip install -r requirements.txt`)
3. Make sure there is a `data` folder
4. Create a `.env` file with the following structure

```sh
AWS_ACCESS_KEY_ID=XXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXX
S3_BUCKET_NAME=XXXXXXXXXX
```

## Usage

Use `python3 main.py` to run the code and download all files.
