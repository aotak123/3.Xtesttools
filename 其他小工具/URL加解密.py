# coding=utf-8
import urllib

                    ####################——————tak制作  vol.605——————####################
                    ####################——————tak制作移植 2.X版——————####################



while True:
    type = input("\033[30m \n 请选择：\n 1：url加密\n 2：url解密\n ")
    if type == "1":
        note1 = input("\033[30m 请输入需要加密的内容\返回请输入:0 \033[0m \n")
        if note1 == "0":   #返回请输入:0
            continue
        else:
            A = urllib.quote(note1) # url加密
            print(A)

    if type == "2":
        note2 = input("\033[30m 请输入需要解密的内容\返回请输入:0 \033[0m \n")
        if note2 == "0":  # 返回请输入:0
            continue
        else:
            B = urllib.unquote(note2)  # url解密
            print(B)

                    ####################——————tak制作  vol.605——————####################
                    ####################——————tak制作移植 2.X版——————####################
