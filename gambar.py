"""Gambar.

Usage:
  gambar <url>
  gambar <url> [-slcw]
  gambar <url> [-slgw]
  gambar -f <filename> [-slgw]
  gambar --version
  gambar (-h | --help)

Options:
  -f --file         Scrape from local file.
  -s --keep         Save text to file (.txt). [Default: False]
  -w --msword       Save text to document (.docx). [Default: False]
  -l --line         Force Paragraph to Line.
  -c --clipboard    Copy to Clipboard.
  -g --noprint      Don't print output, just copy to Clipboard.
  -h --help         Show this screen.
  --version         Show version.
"""
from docopt import docopt

def processCommand(arg):
    import pytesseract as pys
    import pyperclip
    url = arg['<url>']
    filename = arg['<filename>']
    save = arg['--keep']
    line = arg['--line']
    clip = arg['--clipboard']
    pr = arg['--noprint']
    msword = arg['--msword']
    if pr == True:
        clip == True
    if filename == None:
        import wget
        print('\n')
        images = wget.download(url)
    else:
        images = filename
    import os
    results = pys.image_to_string(str(images))
    fname = os.path.splitext(os.path.basename(images))[0]
    # Print Results
    if pr == False:
        print('\n')
        if line == False:
            print(results)
        else:
            print(results.replace('\n',''))
        print('\n')
    # Save to TXT
    if save == False:
        if filename == None:
            os.remove(images)
            print('- Image is removed')
    else:
        print('- Image File: '+ images +'')
        with open(fname + ".txt", "w") as text_file:
            if line == False:
                text_file.write(results)
            else:
                array_results = results.split('\n')
                for result in array_results:
                    text_file.write(result)
            text_file.close()
        print('- Text File: '+ fname +'.txt')
    # Save to Docx
    if msword == True:
        from docx import Document
        document = Document()
        array_results = results.split('\n')
        for result in array_results:
            document.add_paragraph(result)
        document.save(fname + '.docx')
        print('- Doc file: '+ fname +'.docx')
    # Copy to Clipboard
    if clip == True:
        pyperclip.copy(results)
        print('- Copied to Clipboard!')
    # Print Source Image
    if filename == None:
        print('- Source Image: '+url)
    else:
        print('- Source Image: '+images)
    return True

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Gambar v1.0')
    processCommand(arguments)
    print('\n')
