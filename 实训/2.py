from openpyxl import load_workbook
staff_wb = load_workbook('../material/practice2.xlsx')
staff_ws = staff_wb.active
for i in range(2, 21):
    print(staff_ws['D' + str(i)].value)
for i in range(2, 21):
    staff_ws['D'+str(i)].value = "战略储备部"
    print(staff_ws['D' + str(i)].value)
    staff_wb.save('../material/practice2_result.xlsx')