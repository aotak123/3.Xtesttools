# -*- coding: utf-8 -*-

import random


def create_phone():
    # 第二位数字
    second = [4, 6, 7, 9][random.randint(0, 3)]

    # 第三位数字
    third = {
        # 3: random.randint(0, 9),
        # 4: [0, 1, 2, 3, 4, 6, 8][random.randint(0, 6)],
        4: [i for i in range(10) if i not in [5, 7, 9]][random.randint(0, 6)],
        6: [i for i in range(10) if i not in [2, 5, 6]][random.randint(0, 6)],
        # 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        # 7: [i for i in range(10) if i not in [5, 6]][random.randint(0, 7)],
        7: [4, 9][random.randint(0, 1)],  # 174 179 百世快运单号
        9: [i for i in range(10) if i not in [1, 8, 9]][random.randint(0, 6)],
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# 生成手机号
phone = create_phone()
print(phone)
