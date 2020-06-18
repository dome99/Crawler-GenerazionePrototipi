import os


def execute_cocos():
    file_list = os.listdir('./prototipi')
    for file in file_list:
        print("python ./cocos/Pozz.py ./prototipi/" + file + " 5")
        os.system("python ./cocos/Pozz.py ./prototipi/" + file + " 5")


def execute_recommender():
    file_list = os.listdir('./prototipi')
    for file in file_list:
        print("python Recommender.py " + file)
        os.system("python Recommender.py " + file)


if __name__ == '__main__':
    #execute_cocos()
    execute_recommender()