import os
import re
from moviepy.editor import *

def exec_merge(input_path, isAlbum, to_path) :
    '''是专辑，则遍历专辑下的所有文件夹'''
    if isAlbum:
        dirs = os.listdir(input_path)
        for dir in dirs:
            lowest_file = input_path + "/" + str(dir) +"/lua.flv480.bili2api.32"
            merge(lowest_file, str(dir), to_path)  # 将该文件夹下的视频文件合并


def merge(path, p_num, to_path):
    '''
    1. 将非“.blv”结尾的文件删除。->过滤掉，不删除了
    2. 将.blv结尾的文件改成.mp4
    3. 将.blv结尾的文件按照文件名0123的顺序合并
    4. 将合成的文件输出到该目录下，以序号命名。
    :param path: 需要遍历的文件路径， p_num: 视频专辑分p，to_path:目的文件夹
    :return: 
    '''
    p = re.compile(r"\d+\.blv$")
    files = os.listdir(path)
    results = []  # 存放待遍历的文件名称
    L = []
    for file in files:
        match = p.match(file)
        if match:
            src_file = path + "/" + str(file)
            dst_file = path + "/" + str(file).replace(".blv", ".mp4")
            os.rename(src_file, dst_file)  # 改名
            results.append(dst_file)
    results = sort_files(results)

    for item in results:
        video = VideoFileClip(item)
        L.append(video)

    # 拼接视频
    final_clip = concatenate_videoclips(L)
    # 目标文件夹不存在，则创建
    if not os.path.exists(to_path):
        os.mkdir(to_path)
    final_clip.to_videofile(to_path + "/" + p_num + ".mp4", fps=24, remove_temp=False)
    print("视频合并成功")


def sort_files(L):
    '''
    :param L: 待排序的文件名列表：[0.mp4,1.mp4,10.mp4,2.mp4]
    :return: L1排序后的文件名列表：[0.mp4,1.mp4,1.mp4,10.mp4]
    '''
    p = re.compile(r"(.*?)(\d+)\.mp4")
    tmp = []
    L1 = []
    path = p.search(L[0]).group(1)
    for item in L:
        num = int(p.search(item).group(2))
        tmp.append(num)
    tmp.sort()
    for item in tmp:
        L1.append(path + str(item)+".mp4")
    return L1


exec_merge("C:/Users/guoyujian_lc/Desktop/18896337", True, "C:/Users/guoyujian_lc/Desktop/aim")