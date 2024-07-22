#Program 1: To create and write into excel.
import openpyxl
from openpyxl import Workbook
import os

# Change directory to the desired path
os.chdir("D:\Computer Languages\Programming Languages\AutomateTheBooringStuffCodes")

# Create a new workbook
wb = Workbook()

# Select the active worksheet
sheet = wb.active
sheet.title = 'sheet1'  # Rename the active sheet to 'sheet1'

# Modify the worksheet
sheet['A1'] = 44
sheet['A2'] = 'AR'

# Save the workbook
wb.save("demo.xlsx")
#-------------------------------------------------------------------------------------------------------------------------------
#Program 2: To read from workbook

import openpyxl
from openpyxl import Workbook
Workbook = openpyxl.load_workbook("demo.xlsx")
sheet = Workbook.get_sheet_by_name("sheet1")
print(str(sheet['A1'].value))

