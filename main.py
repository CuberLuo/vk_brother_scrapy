# -*- coding:utf-8 -*-

import os
import json
from urllib.request import urlretrieve


def convert_ev1_to_flv():
    video_folder_path = r'./video'
    for root, dirs, files in os.walk(video_folder_path):
        for file in files:
            relative_path = os.path.join(root, file)
            abs_path = os.path.abspath(relative_path)
            os.system(f'ev1_decode {abs_path}')
            path_removed_ev1 = abs_path.replace('.ev1', '')
            os.rename(f'{abs_path}.flv', f'{path_removed_ev1}.flv')


def get_url_list():
    txt_path = r'./data/大雁教你语法长难句1080p_加密视频地址.txt'
    url_list = []
    with open(txt_path, 'r', encoding='UTF-8') as f:
        for line in f:
            url_list.append(line.replace('\n', ''))
    return url_list


def get_chapter_list():
    json_path = r'./data/章节.json'
    chapter_list = []
    with open(json_path, 'r', encoding='UTF-8') as f:
        json_arr = json.load(f)
    for element in json_arr:
        chapter_list.append(element['periods_title'])
    return chapter_list


def run():
    os.mkdir('video')
    url_list = get_url_list()
    chapter_list = get_chapter_list()
    for index, url in enumerate(url_list):
        print(f'{chapter_list[index]}下载中...')
        try:
            urlretrieve(url, filename=rf'./video/{chapter_list[index]}.ev1')
            print('下载完毕!')
        except Exception as e:
            print('网络请求失败!')
            print(e)
    try:
        convert_ev1_to_flv()
    except Exception as e:
        print('视频格式转换失败!')
        print(e)


if __name__ == '__main__':
    run()
