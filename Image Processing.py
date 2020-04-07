# Xu Song
# author:Xu Song

#函数库调用
from PIL import Image
import os

#给出必要文件夹路径
os.system("cp -r ./images ./backup")
src_folder = "./images"
resize_folder = "resize"
gray_folder = "gray"

#调整图片的大小到800*800
def resize(filename,resize):
    Im = Image.open(os.path.join(src_folder,filename))
    if Im.mode != "RGB":
        Im = Im.convert("RGB")
    out = Im.resize((800,800)) 
    out.save(os.path.join(resize,filename),'PNG')

#将显示灰度图片
def image2gray(filename,gray):
    Im = Image.open(os.path.join(resize_folder,filename))
    Gr = Im.convert('L')
    Gr.save(os.path.join(gray,filename),quality=95)

#检查文件是否存在并返回
def folderCheck(foldername):
    if foldername:
        if not os.path.exists(foldername):
            os.mkdir(foldername) 
            print("Info: Folder \"%s\" created" % foldername)
        elif not os.path.isdir(foldername):
            print("Error: Folder \"%s\" conflict" % foldername)
            return False
    return True
    pass
 
def main():
    if folderCheck(resize_folder) and folderCheck(src_folder) and folderCheck(gray_folder):
        #遍历所有图片，调用resize函数
        print("Resizing")
        for filename in os.listdir(src_folder):
            if filename.split('.')[-1].upper() in ("JPG","JPEG","PNG","BMP","GIF"):
                resize(filename,resize_folder)
        print("Resized")
        pass

        #遍历所有图片，调用image2gray函数
        print("Greying")
        for filename in os.listdir(resize_folder):
            if filename.split('.')[-1].upper() in ("JPG","JPEG","PNG","BMP","GIF"):
                image2gray(filename,gray_folder)
        print("Greyed")
        pass


if __name__ == '__main__':
    main()