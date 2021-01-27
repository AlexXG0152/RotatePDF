from PyPDF4 import PdfFileReader, PdfFileWriter
from os import listdir, getcwd, makedirs, path
import shutil


def create():
    """
    Create folders "INPUT" & "OUTPUT" in folder with .py file if not exist
    """
    work_dir = getcwd()
    folders = ["INPUT", "OUTPUT"]
    for i in folders:
        try:
            makedirs(path.join(f"{getcwd()}\\{i}\\"))
        except Exception as e:
            print(f"SOMETHING WENT WRONG... \n{e}")

            
    input_dir = f"{getcwd()}\\INPUT\\"
    output_dir = f"{getcwd()}\\OUTPUT\\"
    
    return work_dir, input_dir, output_dir


def rotate(work_dir, input_dir, output_dir):
    """
    Check folder with .py file for *.pdf documents
    and rotate all pages in doc on 90 degrees.
    After rotate:
    - save new doc to folder OUTPUT with [ ROTATED ] in name
    - save old doc to folder INPUT
    """
    output_writer = PdfFileWriter()
    for x in listdir(work_dir):
        if not x.endswith(".pdf"):
            continue

        with open(x, "rb") as inputf:
            pdfOne = PdfFileReader(inputf)
            numPages = pdfOne.numPages

            for i in list(range(0, numPages)):
                page = pdfOne.getPage(i).rotateClockwise(90)
                output_writer.addPage(page)

            with open(x[:-4] + "   [ ROTATED ].pdf", "wb") as outfile:
                output_writer.write(outfile)

        shutil.move(x, input_dir+x)
        shutil.move(outfile.name, output_dir+outfile.name)


def main():
    work_dir, input_dir, output_dir = create()
    rotate(work_dir, input_dir, output_dir)


if __name__ == "__main__":
    main()
    input("PRESS ANY KEY FOR EXIT")
