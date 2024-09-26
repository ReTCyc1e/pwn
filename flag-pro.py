import os
from time import sleep

def str_insert(str_origin, pos, str_add):
    str_list = list(str_origin)  # 字符串转list
    str_list.insert(pos, str_add)  # 在指定位置插入字符串
    str_out = ''.join(str_list)  # 空字符连接
    return str_out

def flags():
    random_number = os.urandom(16)
    flag = random_number.hex()
    flag = str_insert(flag,8,"-")
    flag = str_insert(flag,13,"-")   # 8+4+1
    flag = str_insert(flag,18,"-")   # 8+4+1+4+1
    flag = str_insert(flag,23,"-")   # 8+4+1+4+1+4+1
    flag = "flag" + "{" + flag + "}"
    return flag

while True:
    flag = flags()
    print(f"{flag}")
    try:
        sleep(1)
    except:
        print("stop!")
        exit()

