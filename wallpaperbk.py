import os
import shutil

clearnpath="d:/Common_program/MissMaggie2.0.0/DownloadedImage/"
backuppath="//10.8.9.2/photo/Material/wallpaper/"


def app(clearnpath, backuppath):

    if os.path.exists(clearnpath):
        if os.path.exists(backuppath):
            path_lists = os.listdir(clearnpath)
            backup_lists = os.listdir(backuppath)

            for path_list in path_lists:
                full_path = os.path.join(clearnpath, path_list)
                if os.path.isfile(full_path):
                    if path_list in backup_lists:
                        os.remove(full_path)
                    else:
                        shutil.move(full_path, backuppath)
        else:
            print("备份目录不存在或路径错误")
    else:
        print("原目录不存在或路径错误")

    return None


if __name__ == '__main__':
        app(clearnpath, backuppath)