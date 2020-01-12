import xlrd


def CheckFile(pFilePath):
    try:
        data = xlrd.open_workbook(pFilePath)
    except:
        rtList = ['文件读取失败,请确认文件格式为xls或xlsx']
        return rtList
    else:
        table = data.sheets()[0]
        cell_A1 = table.row(0)[1].value
        rtList = [cell_A1, 'chemistry', 1997, 2000]
        return rtList