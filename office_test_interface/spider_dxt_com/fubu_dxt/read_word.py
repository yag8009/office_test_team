#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : read_word
# @Time    : 2020/6/13
import docx

import os,zipfile,shutil

def read_word(file_name):
    # path = "append/***.docx"
    strfile = []
    file = docx.Document(file_name)
    for p in file.paragraphs:
        strfile.append(p.text)
    return strfile


def getimage(docdir):
    os.chdir(docdir)
    dirlist = os.listdir(docdir)
    for i in dirlist:
        if i.endswith(".docx"): #匹配docx文件
            docname = i.split(".") #以“.”做成列表形式
            os.rename(i,"%s.ZIP"%docname[0]) #重命名为ZIP格式
            f = zipfile.ZipFile("%s.ZIP"%docname[0], 'r')
            for file in f.namelist():
                if "word" in file:
                    f.extract(file)  #将压缩包里的word文件夹解压出来
            f.close()
            oldimagedir = r"%s\word\media"%docdir #定义图片文件夹
            shutil.copytree(oldimagedir,"%s\%s"%(docdir,docname[0])) #拷贝到新目录，名称为word文件的名字
            os.rename("%s.ZIP" % docname[0],"%s.docx"% docname[0]) #将ZIP名字还原为DOCX
            shutil.rmtree("%s\word"%docdir) #删除word文件夹


if __name__ == '__main__':
    doc = read_word('word_data//夜市摆地摊用什么收银软件和管理库存好.docx')
    print(doc)  # 输出行数：1075

    getimage(r'E:\office_test_team\office_test_interface\spider_dxt_com\fubu_dxt\word_data')
