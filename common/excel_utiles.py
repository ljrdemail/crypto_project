# -*- coding: utf-8 -*-
import xlrd, xlwt
from xlutils.copy import copy
import time
from base.base import Base

class Excel(object):
    def __init__(self, file):

        self.file = Base.get_cur_dir(__file__)  + "\\" + file

        self.data = None
    #打开excel文件
    def open_excel(self):
        try:
            if not self.data:
                self.data = xlrd.open_workbook(self.file)
            return True
        except:
            Base.printErr("打开Excel文件失败！")
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
                        lists.append(row)
            else:
                for num in range(0, nrows):
                    row = table.row_values(num)
                if row:
                    lists.append(row)
            return lists
        except:
            Base.printErr("打开Excel中用例数据失败！")


if __name__ == '__main__':
    ec = Excel("..\\data\\cyprto_test_data.xlsx")

    stocklist=ec.get_page_data("candlestick")
    print (stocklist)


