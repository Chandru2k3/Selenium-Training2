import xlrd

path = r'C:\Users\CHANDRASHEKHAR\Desktop\Software testing\Selenium\Execution'


def excel_data():
    workbook = xlrd.open_workbook(path)                 ## book object
    worksheet = workbook.sheet_by_name("reg")           ## sheet object
    rows = worksheet.get_rows()                         ## generator object
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    return d










































































