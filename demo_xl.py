import openpyxl
from openpyxl.utils import get_column_letter

wb: openpyxl.workbook.workbook.Workbook  = openpyxl.load_workbook("data/media/books.xlsx")
sheet = wb["Feuil1"]
print(sheet["B2"].value)
for column in range(1,3):
    column_letter = get_column_letter(column)
    for row in range(1,sheet.max_row):
        print(sheet[f"{column_letter}{row}"].value)

