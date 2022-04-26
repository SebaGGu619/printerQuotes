import requests
import os
import sys
import win32print
import json
import time
import keyboard

while True:
    if keyboard.is_pressed('q'):
        quote = requests.get("https://inspirobot.me/api?generateFlow=1")
        x = quote.json()
        quoteFinal = x["data"]
        quoteFinal = quoteFinal[1]
        quoteFinal = quoteFinal["text"]

        for i in range(len(quoteFinal) - 1):
            try:
                if quoteFinal[i + 1] == ' ':
                    pass
            except:
                break
            if quoteFinal[i] == '’':
                quoteFinal = quoteFinal[:i] + '\'' + quoteFinal[(i + 1):]

        for i in range(int(len(quoteFinal) / 41)):
            if quoteFinal[41 * (i + 1)] != ' ':
                j = 41 * (i + 1)
                while quoteFinal[j] != ' ':
                    j = j - 1
                for abc in range(((41 * (i + 1)) - j) - 1):
                    quoteFinal = quoteFinal[:j] + '  ' + quoteFinal[(j + 1):]

        # for i in range(len(quoteFinal)):
        #     try:
        #         if quoteFinal[i + 1] == ' ':
        #             pass
        #     except:
        #         break
        #     if quoteFinal[i] == '.' and quoteFinal[i + 1] == ' ':
        #         quoteFinal = quoteFinal[:(i + 1)] + '\n' + quoteFinal[(i + 2):]
        #     if quoteFinal[i] == ':' and quoteFinal[i + 1] == ' ':
        #         quoteFinal = quoteFinal[:(i + 1)] + '\n' + quoteFinal[(i + 2):]
        #     if quoteFinal[i] == '!' and quoteFinal[i + 1] == ' ':
        #         quoteFinal = quoteFinal[:(i + 1)] + '\n' + quoteFinal[(i + 2):]
        #     if quoteFinal[i] == '?' and quoteFinal[i + 1] == ' ':
        #         quoteFinal = quoteFinal[:(i + 1)] + '\n' + quoteFinal[(i + 2):]

        printer1 = win32print.OpenPrinter("EPSON TM-T88IV ReceiptE4")

        string = quoteFinal
        bytes = string.encode(encoding='UTF-8')

        win32print.StartDocPrinter(printer1, 1, ("Inspirational Quote", None, "TEXT"))
        win32print.StartPagePrinter(printer1)
        win32print.WritePrinter(printer1, bytes)
        win32print.EndPagePrinter(printer1)
        win32print.EndDocPrinter(printer1)
        win32print.ClosePrinter(printer1)

        time.sleep(1)

    if keyboard.is_pressed('esc'):
        break
