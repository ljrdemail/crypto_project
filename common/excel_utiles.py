# -*- coding: utf-8 -*-
import xlrd


from common.func import Func


class Excel(object):
    def __init__(self, file):

        self.file = file

        self.data = None
    #打开excel文件
    def open_excel(self):
        try:
            if not self.data:
                self.data = xlrd.open_workbook(self.file)
            return True
        except:
            Func.printErr("打开Excel文件失败！")
            return False


    def get_page_data(self, page,containtitle=True):
        try:
            if not self.open_excel():
                return None
            table = self.data.sheet_by_name(page)
            nrows = table.nrows #行数
            lists = []
            if containtitle:
                for num in range(1, nrows):
                    row = table.row_values(num)
                    if row:
                        lists.append(tuple(row))
            else:
                for num in range(0, nrows):
                    row = table.row_values(num)
                if row:
                    lists.append(tuple(row))

            return lists
        except:
            Func.printErr("打开Excel中用例数据失败！")

    def write_by_index(self, row, col, page,value):
        try:
            self.target.get_sheet(page).write(row, col, value)
            return True
        except:
            Func.printErr("按行列号写入Excel文件失败！")
            return False

    def save_excel(self):
        try:
            self.target.save(self.targetName)
            return True
        except:
            Func.printErr("保存Excel文件失败！")
            return False


if __name__ == '__main__':
    ec = Excel("..\\data\\cyprto_test_data.xls")
    stocklist=ec.get_page_data("candlestick")
    print (stocklist)


