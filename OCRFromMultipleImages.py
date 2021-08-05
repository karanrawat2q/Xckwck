# Using tesseract extacting text from multiple images in a folder 
import os
import glob

path = r"C:\Users\Karan\Pictures\Screenshots\*.png"
pics = []
for img in glob.glob(path):
    pics.append(img)

os.chdir("C:\\Users\\Karan\\Pictures\\Screenshots")

for fileidx, filename in enumerate(pics):
    filename_clean = filename.replace("\\", "/")
    outfile = f"file{fileidx}"
    os.system(f"tesseract {filename_clean} {outfile}")