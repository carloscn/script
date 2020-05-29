# -*- coding: UTF-8 -*-
import os
import time
import xlrd
import xlrd
import xlwt
from xlutils.copy import copy
import matplotlib.pyplot as plt
import numpy as np

class analyse():
    samples = 10
    excel_name = ".\hash_drbg_report.xls"
    excel_sheet_number = 0
    excel_col_n = 0
    excel_raw_n = 0
    lengend_list = []
    cur_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    rb = 0
    col_cur = 0
    raw_cur = 0
    init = 0
    def __init__(self):
        self.init = 0
        self.col_cur = 0
        self.raw_cur = 0

    def read_header(self):
        self.rb = xlrd.open_workbook(self.excel_name)
        sheet = self.rb.sheet_by_index(self.excel_sheet_number)
        self.excel_raw_n = sheet.nrows
        self.excel_col_n = sheet.ncols
        self.lengend_list = sheet.col_values(0)
        self.lengend_list = self.lengend_list[1:]
        print(self.lengend_list)

    def plot_frequency(self):
        for j in range(1, int(self.excel_col_n)) :
            print(self.lengend_list[j-1])
            sheet = self.rb.sheet_by_index(self.excel_sheet_number)
            row = sheet.row_values(j)
            x = np.linspace(0 ,1 , self.samples)
            alist = []
            for i in range(0, int(self.excel_col_n/self.samples)):
                temp_r = row[int(1 + i*self.samples): int(self.samples + self.samples * i + 1)]
                temp_n = [ float(x) for x in temp_r ]
                mean = np.mean(temp_n)
                print(self.cur_list[i] + ": " + str(mean))
                print(temp_n)
                alist.append(mean)
                plt.plot(temp_n,'-<')
            a = np.max(temp_n)
            np.where(a)
            print(self.lengend_list[j-1] + " max is " + self.cur_list[np.argmax(alist)])
            plt.title(self.lengend_list[j-1])
            plt.grid(linestyle=":")
            plt.legend(self.cur_list)
            plt.axis([0, self.samples, 80, 120])
            plt.show()



if __name__ == '__main__':
    t = analyse();
    t.read_header()
    t.plot_frequency()


