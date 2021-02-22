import openpyxl
excel_document = openpyxl.load_workbook('prueba.xlsx')
sheet = excel_document['Ingredientes']
sheet['C2'] = "Hola de nuevo"
excel_document.save('prueba.xlsx')
print(sheet['A2'].value)