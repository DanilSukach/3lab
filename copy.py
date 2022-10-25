import os
import shutil


def copy(path: str) -> None:
    """Функция принимает путь к файлам: path и метку класса: label"""
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    info = os.listdir(path)
    for i in info:
        info_data = os.listdir(path + i)
        for j in info_data:
            shutil.copy(
                os.path.join(path+i, j), os.path.join("dataset_copy/", i + "_" + j)
            )


def main():
    copy("dataset/")
   


if __name__ == "__main__":
    main()
