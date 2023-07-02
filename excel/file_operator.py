import os
from datetime import datetime
from config import *


# 获取文件完整路径,参数为所处子目录、文件名
def get_file_full_path(sub_path: str, file_name: str) -> str:
    return "".join([get_dir_path(sub_path), "\\", file_name])


def get_root_path(dir_path: str) -> str:
    return dir_path.rsplit("\\", 1)[0]


# 获取当前目录或子目录路径
def get_dir_path(sub_path="") -> str:
    abs_dir = os.path.dirname(os.path.abspath(__file__))
    if sub_path == "":
        return abs_dir
    else:
        return "".join([abs_dir, "\\", sub_path])


# 加时间戳将 路径.旧文件名 生成 路径.新文件名
def get_new_file_name(file_name_ext: str) -> str:
    name_type = file_name_ext.rsplit(".", 1)
    name_type[0] = "".join([name_type[0], "-", str(datetime.today()).replace(" ", "-").replace(":", "-")])
    return ".".join(name_type)


# 创建目录
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def append_file_path(file_path: str, new_sub_path: str, file_name_ext) -> str:
    return "\\".join([file_path, new_sub_path, file_name_ext])


# 生成文件主路径 + 子文件夹 + 新文件名
def gene_new_file_path(file_path: str, new_sub_path: str) -> str:
    path_list = file_path.rsplit("\\", 2)
    path_list[1] = new_sub_path
    path_list[2] = get_new_file_name(path_list[2])
    create_dir("\\".join([path_list[0], path_list[1]]))
    return "\\".join(path_list)


# 从配置文件加载参数组装路径
def path() -> str:
    root_path = get_root_path(get_dir_path())
    create_dir("\\".join([root_path, sub_dir]))
    return append_file_path(root_path, sub_dir, get_new_file_name(".".join([file_name, file_ext])))
