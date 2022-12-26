# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:21:13 2022

@author: k9981
"""

import qrcode
from tkinter import *


class QR:
    def __init__(self):
        self.save_path = []
        self.make_QR()
        
        window = Tk()
        window.title("QR코드 생성기")
        window.geometry("1000x800")
        
        i = 0
        
        for path in self.save_path:
            print(path)
            
            imgs = PhotoImage(file = path, master = window)
            lbl_text = Label(window, text = path)
            #lbl_text.pack()
            
            lbl_img = Label(window, image = imgs)
            lbl_img.image = imgs
            #lbl_img.pack()
            
            lbl_text.grid(row = 1, column = i)
            lbl_img.grid(row = 0, column = i)
            i += 1
        
        window.mainloop()
    
    def make_QR(self):
        self.file_path = 'QR코드\qr코드모음.txt'
        with open(self.file_path, 'rt', encoding="UTF8") as f:
            read_lines = f.readlines()
            
            i=0
            
            for line in read_lines:
                line = line.strip()
                print(line)
                
                qr_data = line
                qr_img = qrcode.make(qr_data)
                
                self.save_path.append("QR코드\\" + qr_data[12:] + ".png")
                qr_img.save(self.save_path[i])
                i += 1

QR()