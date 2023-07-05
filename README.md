# fb-comment-lister
This takes in an exported xlsx file from https://exportcomments.com/ and produces a list of names and their comment count.

## How do I use this program?

1. In order to use this program, simply download `dist/export-names.exe` and run the file. Opening the program will produce a similar case below.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/0cb978f7-fffa-426a-860a-e4fac59abbad)

2. Select your imported XLSX files (presumably exported from https://exportcomments.com/) and click `Open`.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/6c631324-e2c4-4b56-80e8-bea4208dcf56)

   
3. TXT files will then be produced at the place where `export-names.exe` is located. The filename is labeled as `[date] fc-<id>.txt` where `<date>` is the date of the first comment in the XLSX file (located at "E8").
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/2a8068ba-a37f-4413-9bb7-3977de07c798)

4. After successful operation, the program will close. Below are sample outputs. Each entry is formatted as `[comment_count] <name>`.
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/e9e1b820-b271-4a00-9ca6-4a184654be47)

## I do not trust the EXE file. Where is the source code?
If you do not trust the EXE file, you can manually run the python file `export-names.py` by either running `python export-names.py` or `python3 export-names.py`, whichever is usable depending on your Python distribution.

