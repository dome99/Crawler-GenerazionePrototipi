# Esegue cocos con tutti i file presenti in ./prototipi/

import os


def execute_cocos():
    file_list = os.listdir('./prototipi')
    for file in file_list:
        print("python ./cocos/Pozz.py ./prototipi/" + file + " 5")
        os.system("python ./cocos/Pozz.py ./prototipi/" + file + " 5")


if __name__ == '__main__':
    execute_cocos()