import os
import random

def numbering(re_numbering = False):
    directory = input("경로를 입력하세요: ")

    list = [file for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file))]
    files_count = len(list)

    number_list = []

    for i in range(files_count):
        number_list.append(i)

    for filename in list:
        number = number_list[random.randrange(len(number_list))]

        old_file = os.path.join(directory, filename)
        
        if re_numbering == True:
            new_filename = ("%d. " + filename[filename.find(".") + 2:]) % (number + 1)
        else:
            new_filename = ("%d. " + filename) % (number + 1)

        new_file = os.path.join(directory, new_filename)
        
        os.rename(old_file, new_file)
        print(filename + " -> " + new_filename)
        
        number_list.remove(number)
    
    print("*** 완료되었습니다. ***")
        
if __name__ == "__main__":
    select = input("새로 숫자를 붙인다면 1, 다시 숫자를 붙인다면 2를 입력하세요: ")
    if select == "1":
        numbering()
    elif select == "2":
        numbering(True)
