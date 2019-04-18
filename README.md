
# Gambar

An Image Scrapper Tools written in Python.
[![asciicast](https://asciinema.org/a/cNjFBVESnukxOhC1c2X1WkltY.svg)](https://asciinema.org/a/cNjFBVESnukxOhC1c2X1WkltY)

## Requirements

- Python 3.6 or above.

## Installation
```bash
$ git clone https://github.com/dedenbangkit/gambar ~/.gambar
$ cd ~/.gambar
$ pip install -r requirements.txt
$ chmod +x gambar
$ mv gambar usr/local/bin/gambar
```

## Usage

```
$ gambar <url>
$ gambar -f <filename>

Usage:
  gambar <url>
  gambar <url> [-slcw]
  gambar <url> [-slgw]
  gambar -f <filename> [-lgw]
  gambar --version
  gambar (-h | --help)

Options:
  -f --file         Scrape from local file.
  -s --keep         Save text to file (.txt). [Default: False]
  -o --output       Output file (without extension) 
  -w --msword       Save text to document (.docx). [Default: False]
  -l --line         Force Paragraph to Line.
  -c --clipboard    Copy to Clipboard.
  -g --noprint      Don't print output, just copy to Clipboard.
  -h --help         Show this screen.
  --version         Show version.
```
