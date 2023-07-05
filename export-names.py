import openpyxl
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


## Getnames from comments
def exportColumnToText(xlsxFileNames, columnName):

    for xlsxFileName in xlsxFileNames:

        wb = openpyxl.load_workbook(xlsxFileName)
        sheet = wb.active
        names_count = {}
        row = 8  # Starting row (C8)
        
        date = str(sheet["E8"].value)[:10]
        filename = (os.path.basename(xlsxFileName)[17:])[:-5]
        outputFileName = f"[{date}] fc-{filename}.txt"

        while True:

            cellValue = sheet[columnName + str(row)].value
            if cellValue is None:
                break

            name = str(cellValue)
            if name in names_count:
                names_count[name] += 1
            else:
                names_count[name] = 1

            row += 1

        sorted_names_count = sorted(names_count.items(), key=lambda x: x[0])  # Sort by name

        with open(outputFileName, "w", encoding="utf-8") as outputFile:
            
            line = f"[date] \t{date}\n\n"
            outputFile.write(line)

            for name, count in sorted_names_count:
                line = f"[{count}]  \t{name}\n"
                outputFile.write(line)

    print("Export completed successfully.")


# Open file explorer dialog to select Excel files
Tk().withdraw()
xlsxFileNames = askopenfilenames(filetypes=[("Excel Files", "*.xlsx")])
columnName = "C"
exportColumnToText(xlsxFileNames, columnName)
