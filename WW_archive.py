from zipfile import ZipFile
import os

def create_archive_ext(extention):
    #Функция находит все файлы с расширением extention и добывляет их в архив
    with ZipFile("test.zip", "a") as testzip:
        for file in os.listdir("."):
            if os.path.splitext(file)[1] == extention:
                testzip.write(file)

#create_archive_ext(".txt")

