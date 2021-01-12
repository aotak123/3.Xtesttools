import exifread
import os
from tkinter.filedialog import *  # 别问我怎么不导入os模块就能 重命名，我也不知道，可能这个tkinter模块包含有os了吧，哈哈

Files_Names = {  # 全局变量，存储照片绝对路径  和  目录路径(即不包含照片名的路径)
    "all_path": [],
    "ml_name": ""
}


def mainapp():  # 创建窗体
    app = Tk()
    app.title("批量根据exif信息自动重命名照片")
    Label(app, text="批量根据exif信息自动重命名照片", font=("微软雅黑", 25, "bold")).pack()  # 画标签并设置显示的文字，字体，加粗
    Listbox(app, name='l_b', bg="#f2f2f2", fg="red").pack(fill=BOTH,
                                                          expand=True)  # 画列表框并指定名字,方便后续根据名字调用获取Listbox实例,指定背景，前景,显示方式
    Button(app, text="选择照片路径", command=ui_update).pack(fill=BOTH)  # command指定了当按下按钮，会调用哪个方法
    Button(app, text="开始Exif命命名", command=rename).pack(fill=BOTH)  # left

    app_width = 500  # 设置窗口宽度
    app_height = 500  # 设置窗口高度
    win_width = int((
                            app.winfo_screenwidth() - app_width) / 2)  # 设置窗口距离左上角原点的 宽度  屏幕总宽度-软件窗口宽度  再除2，即软件距离左侧窗口的宽度  转为整数，因为下面geometry只接受字符串型整数
    win_height = int((
                             app.winfo_screenheight() - app_height) / 2)  # 设置窗口距离左上角原点的 高度  屏幕总宽度-软件窗口高度  再除2，即软件距离顶边的高度  转为整数，因为下面geometry只接受字符串型整数
    app.geometry("%sx%s+%s+%s" % (app_width, app_height, win_width, win_height))  # 设置窗口显示的宽高度 及 距离原点的长宽度
    return app


def ui_update():  # 此方法用于把照片所有的路径读到 列表框，当点击按钮《选择照片路径》，就会调用此方法
    list_box = a.children["l_b"]  # 读取出列表框对象
    list_box.delete(0, END)  # 删除全部列表内容,防止你点了几次《选择照片路径》，重复添加了几次照片。
    Files_Names["ml_name"] = askdirectory()  # 选择照片所在的目录并存到变量里，后面重命名完成后，调用这个变量，显示文件夹出来
    Files_Names[
        "all_path"] = []  # 把存了照片的绝对路径的变量清空,防止你批量重命名完一个文件夹后(此时没关闭软件)，继续使用去选择下一个文件夹来重命名，如果不清空，将会出错，因为残留有上一次批量重命名的路径名。
    if Files_Names["ml_name"] != "":  # 此判断为了防止你点了《选择照片路径》按钮，又不选择文件夹,直接点了取消,此时返回空,就不执行遍历照片功能。
        Files_Names["ml_name"] += "/"
        list_name(Files_Names["ml_name"])  # 把选择的目录传入到list_name方法中，进行递归遍历照片文件路径


def list_name(ml_name):
    file_names = os.listdir(ml_name)  # 根据选择的目录列出里面的照片及目录 返回列表
    if file_names != "":  # 只要返回的照片和目录路径不为空，防止你犯二，选择了一个没有照片的空目录
        list_box = a.children["l_b"]  # 读取出列表框对象，下面在循环插入路径到列表框要用对象调用
        for i in range(0, len(file_names)):  # 列表转换为循环数。
            path = os.path.join(ml_name, file_names[i])  # 把目录名ml_name拼接上文件名file_names[i]，获得完整路径。
            if os.path.isfile(path):  # 如果为真，则是文件
                list_box.insert(END, path)  # 循环插入文件名到列表框
                Files_Names["all_path"].append(path)  # 完整的照片路径追加到 全局变量列表中
            else:  # 如果不是文件，那应该是目录,就加上/，再调用自身方法，进行递归列出下一层的文件，很多人在递归这里搞不明白。。。
                try:
                    list_name(path + "/")
                except:
                    print("访问目录出错，可能不是一个目录,或者是奇奇怪怪的文件名")


def rename():
    for index, j_file_name in enumerate(Files_Names["all_path"]):  # 准备循环重命名
        with open(j_file_name, 'rb') as f:  # 打开照片文件并读取到f中
            tags = exifread.process_file(f)  # 从f中通过exifread.process_file获取exif信息(返回一个字典类型)
            image_exif_time = ""  # 清空exif拍摄时间信息,为下一个照片重命名做准备,不残留上一个照片的拍照时间
            image_Make_mode = ""  # 清空exif拍摄时间信息,为下一个照片重命名做准备,不残留上一个照片的手机型号
            if "EXIF DateTimeOriginal" in tags.keys():  # 如果这个存着拍摄时间的键 存在 上面取出的exif字典里
                image_exif_time = tags[
                    "EXIF DateTimeOriginal"]  # 把时间取出来,赋值给变量,准备拿它来当新文件名,下面两个同样道理，都是存着时间的，当判断这个键不存在时，就判断下面两个键有没有时间存着。

            elif "EXIF DateTimeDigitized" in tags.keys():  # 实践发现，这也是一个拍摄时间
                image_exif_time = tags["EXIF DateTimeDigitized"]
            elif "Image DateTime" in tags.keys():  # 实践发现，这也是一个拍摄时间
                image_exif_time = tags["Image DateTime"]

            if ":" in str(image_exif_time):  # 取出来的拍摄时间是 2020:01:01 18:18 这种形式，难看
                image_exif_time = str(image_exif_time).replace(":", "-")  # 换成2020-01-01 18-18 形式

            if "Image Make" in tags.keys() and "Image Model" in tags.keys():  # 如果存在品牌和 型号，就取出来
                image_Make_mode = "-" + str(tags["Image Make"]) + str(tags["Image Model"])

            if image_exif_time != "":  # 如果有拍摄时间,就进行 拆分目录 和 文件名
                img_path = "/".join(j_file_name.split("/")[0:-1])  # 取出照片目录    D:/ZM/2019.05.11社团周年庆
                img_name = j_file_name.split("/")[-1]  # 取出文件名。    656566.jpg
                hz = img_name.split(".")[-1]  # 取出后缀。     .jpg

            else:  # 如果没有拍摄时间，直接跳到循环尾，进行下一个照片exif时间的提取，不进行重命名了。
                continue

        try:  # try一下，防止出现未知错误    这里要注意,不能写在with里，因为会占用照片文件，导致重命名失败。
            new_file_name = ("%s/%s%s.%s") % (img_path, image_exif_time, image_Make_mode, hz)
            os.renames(j_file_name, new_file_name)
        except:  # 当出现未知错误,或者是照片里的exif拍摄时间重复,比如1秒拍了10张,这类照片因为时间一模一样，重命名不了，只能在时间一样的照片后面按顺序加上 数字 来重命名。
            for o in range(50):  # 防止你相机设备太牛逼，1秒拍了50张，导致时间一模一样的照片，所以设置循环50次,在文件名后面依次加上数字来重命名。
                try:
                    new_file_name = ("%s/%s%s-%s.%s") % (img_path, image_exif_time, image_Make_mode, str(o + 1), hz)
                    print("第%d张图片重命名中,疑似名字重复或照片文件损坏，重命名失败,将添加后缀%s继续重命名！50次内若重命名还是失败，将忽略些图片！" % (index, str(o + 1)))
                    print("原文件名：%s" % j_file_name)
                    print("预计新文件名：%s\n\n" % new_file_name)
                    os.renames(j_file_name, new_file_name)
                    break  # 当重命名成功后，立即跳出循环，不用笨笨的循环到50次。
                except:
                    pass
    # os.startfile(Files_Names["ml_name"])  # 所有文件重命名完成后，弹出照片所有的窗口
    print("重命名完成！")


a = mainapp()
a.mainloop()