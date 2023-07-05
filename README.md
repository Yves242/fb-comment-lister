# fb-comment-lister
This takes in an exported xlsx file from https://exportcomments.com/ and produces a list of names and their comment count.

## How do I use this program?

1. In order to use this program, simply download `dist/export-names.exe` and run the file. Opening the program will produce a similar case below.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/3b359652-e410-4a49-bd8b-402b76fe8cdc)

2. Select your imported XLSX files (presumably exported from https://exportcomments.com/) and click `Open`.

![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/6c631324-e2c4-4b56-80e8-bea4208dcf56)

   
3. TXT files will then be produced at the place where `export-names.exe` is located. The filename is labeled as `[date] fc-<id>.txt` where `<date>` is the date of the first comment in the XLSX file (located at "E8").
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/e7235933-3ed2-47c3-8265-2798f82a1d6a)

4. After successful operation, the program will close. Below are sample outputs. Each entry is formatted as `[comment_count] <name>`.
   
![image](https://github.com/Yves242/fb-comment-lister/assets/70612985/e9e1b820-b271-4a00-9ca6-4a184654be47)


## I do not trust the EXE file. Where is the source code?

If you do not trust the EXE file, you can manually run the python file `export-names.py` by either running `python export-names.py` or `python3 export-names.py`, whichever is usable depending on your Python distribution. From there, you can see exactly how the program works. (I exported the PY file into EXE using `pyinstaller --onefile export-names.py`).

