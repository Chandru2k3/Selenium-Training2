from openpyxl import Workbook

workbook = Workbook()

worksheet = workbook.active

worksheet.title = 'Persnol_info'

worksheet['A1'] = "name"
worksheet['B1'] = "place"
worksheet['C1'] = "email_id"
worksheet['D1'] = "phone_number"

datalist = [
    ['venkat','hydrabad','venkat@gmail.com','839372828'],
    ['chandru','belgaun','chandru@gmial.com','8296205572']
]

for i in datalist:
    datalist.append(i)























