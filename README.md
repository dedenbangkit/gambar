
# Gambar

An Image Scrapper Tools written in Python.

## Requirements

- Python 3.6 or above.

## Installation
```bash
$ git clone https://github.com/dedenbangkit/gambar
$ pip install -r requirements.txt

```

## Usage

```
$ python gambar.py <url>
$ python gambar.py -f <filename>

Usage:
  python gambar.py <url>
  python gambar.py <url> [-slcw]
  python gambar.py <url> [-slgw]
  python gambar.py -f <filename> [-lgw]
  python gambar.py --version
  python gambar.py (-h | --help)

Options:
  -f --file         Scrape from local file.
  -s --keep         Save text to file (.txt). [Default: False]
  -w --msword       Save text to document (.docx). [Default: False]
  -l --line         Force Paragraph to Line.
  -c --clipboard    Copy to Clipboard.
  -g --noprint      Don't print output, just copy to Clipboard.
  -h --help         Show this screen.
  --version         Show version.
```
