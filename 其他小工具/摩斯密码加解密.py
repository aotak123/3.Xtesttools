# coding=utf-8
                    ####################——————tak制作  vol.606——————####################
                    ####################——————tak制作移植 2.X版——————####################

dict1 = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-.', 'e': '.','f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---','p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-','5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '?': '..--..','/': '-..-.','()': '-.--.-','-': '-....-','.': '.-.-.-','：': "———···"
         }

dict2 = dict(zip(dict1.values(), dict1.keys()))

def encode():
    words = input("请输入需要加密的内容：").strip().lower() #Input a sentence you want to endoce, NO PUNCTUATION
    for letter in words:
        if letter == ' ':
            print('/', end='')
        else:
            print(dict1[letter], end='')
    print()


def decode():
    codes = input("请输入摩斯密码：").strip().split(" ")  #Input Morse code you want to decode, ONLY MORSE CODE:
    for sign in codes:
        if sign == '/':
            print(' ', end='')
        else:
            print(dict2[sign], end='')
    print()


while 1 == 1:
    choice = input("1：摩斯密码加密\n"# Morse code encode
                       "2：莫斯密码解密\n"# Morse code decode
                       "请选择输入 [1/2]")

    if choice == '1':
        encode()
    elif choice == '2':
        decode()
    else:
        break
                    ####################——————tak制作  vol.606——————####################
                    ####################——————tak制作移植 2.X版——————####################
"""
Code producer：aotak
Mobile：+86 18817762560
E-Mail：hujunyi@021.com 
"""