# -*- coding: UTF-8 -*-
import os
import time
import xlrd
import xlrd
import xlwt
from xlutils.copy import copy
from xlwt import Workbook

class report():
    excel_name = "/home/carlos/Desktop/time.xls"
    report_dir = r"/home/carlos/sts-2.1.2_muti50thread/data/unsame_seed"
    col_cur = 0
    raw_cur = 0
    init = 0
    def __init__(self):
        self.init = 0
        self.col_cur = 0
        self.raw_cur = 0

    def write_to_excel(self, sheet_num, raw_number, col_number, value):
        rb = xlrd.open_workbook(self.excel_name)
        wb = copy(rb)
        sheet = wb.get_sheet(sheet_num)
        sheet.write(raw_number, col_number, value)
        wb.save(self.excel_name)

    def read_single_report_to_excel(self, sheet_num, txt_name, header):
        file_txt = open(txt_name)
        lines = file_txt.readlines()
        count = len(lines)
        payload_count = count - 20
        self.col_cur = self.col_cur + 1
        self.write_to_excel(sheet_num, self.raw_cur, self.col_cur, header)
        for i in range(0,payload_count):
            strlist = lines[7 + i].split(r' ')
            while '' in strlist:
                strlist.remove('')
            if "*" in strlist:
                p_value = strlist[-4]
            else:
                p_value = strlist[-3]
            if "." not in p_value:
                p_value = "bad"
            self.write_to_excel(sheet_num, i + 1, self.col_cur, p_value)
        #print("name:" + strlist[-1].strip() + "\tp-value:" + strlist[-3])


    def init_excel_doc(self, sheet_num, txt_name):
        file_txt = open(txt_name)
        lines = file_txt.readlines()
        count = len(lines)
        payload_count = count - 20
        header = "test item"
        self.write_to_excel(0, 0, 0, header);
        # read Bitrate and YUV info
        for i in range(sheet_num ,payload_count):
            strlist = lines[7 + i].split(" ")
            while '' in strlist:
                strlist.remove('')
            name = strlist[-1].strip()
            self.write_to_excel(0, i+1, 0, name);
        print("write header ok!")

    def run(self):
        for root, dirs, files in os.walk(self.report_dir):
            for name in files:
                file_name = os.path.join(root, name)
                if "finalAnalysisReport.txt" in file_name:
                    print("found : " + file_name)
                    header = file_name.split(r'/')[-7]
                    print(header)
                    if self.init == 0:
                        self.init_excel_doc(0, file_name)
                        self.init = 1
                    self.read_single_report_to_excel(0, file_name, header)


if __name__ == '__main__':
    t = report();
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('Sheet 1')
    # 保存Excel book.save('path/文件名称.xls')
    book.save(t.excel_name)
    t.run()


