# fb-comment-lister
This takes in an exported xlsx file from https://exportcomments.com/ and produces a list of names and their comment count.

## How do I use this program?

1. In order to use this program, simply download `dist/export-names.exe` and run the file. Opening the program will produce a similar case below.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/feeb4999-cdda-4823-8ea0-c17112d07129)


2. Select your imported XLSX files (presumably exported from https://exportcomments.com/) and click `Open`.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/c1e66473-e184-42f6-a2ea-a07c44cf5970)


   
3. TXT files will then be produced at the place where `export-names.exe` is located. The filename is labeled as `[date] fc-<id>.txt` where `<date>` is the date of the first comment in the XLSX file (located at "E8").
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/0b292c13-bf2b-446f-bd89-cadde6f95f2e)


4. After successful operation, the program will close. Below are sample outputs. Each entry is formatted as `[comment_count] <name>`.
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/f6b5f026-348a-49f0-ac47-85ea0a808c90)



## I do not trust the EXE file. Where is the source code?

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/d0162fc2-8822-424e-8c46-b13493d436da)

I exported the PY file into EXE using `pyinstaller --onefile export-names.py`; However, if you do not trust the EXE file, you can manually run the python file `export-names.py` by either running `python export-names.py` or `python3 export-names.py`, whichever is applicable depending on your Python distribution. From there, you can investigate exactly how the program works, and perhaps compile one on your own.
