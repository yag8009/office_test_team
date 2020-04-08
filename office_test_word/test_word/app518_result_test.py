#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @Time    : 2019/1/10 17:59

# 取值

import time
import wave

import pyaudio
import requests


def get_info():
    t = int(round(time.time() * 1000))
    # t = time.strftime("%Y-%m-%d", time.localtime())
    url = 'https://111p8.cc/anls-api/data/cqssc/numTrend/100.do?_t={}'.format(t)
    # data = {"pageIndex": 1, "playGroupId": "cq_ssc", "pageSize": 50}
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) '
        'Version/11.0 Mobile/15A372 Safari/604.1',
        'accept': 'application/json, text/plain, */*'}

    rnum = 0
    while rnum != 200:
        try:
            r = requests.post(url, headers=headers, timeout=(5, 10))
            rnum = int(r.status_code)
            time.sleep(1)
            chunk = 1024
            wf = wave.open('E:\\office_test_team\\office_test_word\\test_word\\Global.wav', 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(chunk)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(chunk)
            stream.stop_stream()
            stream.close()
            p.terminate()
        except:
            rnum = 0
            time.sleep(1)

    print("请求数据成功！！！")

    html = r.json()
    list_json = []
    for i in html['bodyList']:
        x = str(i['openNum']).replace(', ', '')[1:6]
        list_json.append((i['issue'], "".join(x)))

    list_json1 = sorted(list_json, key=lambda asd: asd[0], reverse=False)
    return list_json1


def getinfo(args, data):
    """
        预计
        :param args: [('20191121056', '73901'), ('20191121057', '80705'),
        :param data: 0～9
        :return: [('002', '86440', '|1对', '1'), ('006', '58336', '|1对', '1'),
        """
    result_true = 0
    result_error = 0
    result_count = 0
    result_list = []

    cmplist = args
    try:
        for i in range(len(cmplist)):
            result_count = result_count + 1
            str_int = str(data)
            units1 = i + 1
            units2 = i + 2
            units3 = i + 3
            units4 = i + 4
            units5 = i + 5
            if units1 < len(cmplist):
                if str_int in cmplist[units1][1]:
                    result_true = result_true + 1
                    result_list.append(
                        (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s对" % str_int))
                    )
                elif units2 < len(cmplist):
                    if str_int in cmplist[units2][1]:
                        result_true = result_true + 1
                        result_list.append(
                            (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s对" % str_int))
                        )
                    elif units3 < len(cmplist):
                        if str_int in cmplist[units3][1]:
                            result_true = result_true + 1
                            result_list.append(
                                (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s对" % str_int))
                            )
                        elif units4 < len(cmplist):
                            if str_int in cmplist[units4][1]:
                                result_true = result_true + 1
                                result_list.append(
                                    (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s对" % str_int))
                                )
                            elif units5 < len(cmplist):
                                if str_int in cmplist[units5][1]:
                                    result_true = result_true + 1
                                    result_list.append(
                                        (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s对" % str_int))
                                    )
                                else:
                                    result_error = result_error + 1
                                    result_list.append(
                                        (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s--" % str_int))
                                    )
                            else:
                                result_list.append(
                                    (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s--" % str_int))
                                )
                        else:
                            result_list.append(
                                (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s--" % str_int))
                            )
                    else:
                        result_list.append(
                            (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s--" % str_int))
                        )
                else:
                    result_list.append(
                        (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s--" % str_int))
                    )
            else:
                result_list.append(
                    (cmplist[i][0][8:], cmplist[i][1], str_int, ("|%s-|" % str_int))
                )

        print(
            "锁|%s|  总: %s OK: %s 占比:%.2f%%" % (data, result_count, result_true, (result_true / result_count * 100))
        )
    except BaseException:
        print(
            "锁|%s|  总: %s OK: %s 占比:0.00%%" % (data, result_count, result_true)
        )
    return result_list


def getValue(args):
    list_res = [[0 for i in range(22)] for i in range(len(args))]
    j0 = getinfo(args, "0")
    j1 = getinfo(args, "1")
    j2 = getinfo(args, "2")
    j3 = getinfo(args, "3")
    j4 = getinfo(args, "4")
    j5 = getinfo(args, "5")
    j6 = getinfo(args, "6")
    j7 = getinfo(args, "7")
    j8 = getinfo(args, "8")
    j9 = getinfo(args, "9")

    for i in range(len(list_res)):
        list_res[i][0] = j0[i][0]
        list_res[i][1] = j0[i][1]
        list_res[i][2] = j0[i][3]
        list_res[i][3] = int(j0[i][2])
        list_res[i][4] = j1[i][3]
        list_res[i][5] = int(j1[i][2])
        list_res[i][6] = j2[i][3]
        list_res[i][7] = int(j2[i][2])
        list_res[i][8] = j3[i][3]
        list_res[i][9] = int(j3[i][2])
        list_res[i][10] = j4[i][3]
        list_res[i][11] = int(j4[i][2])
        list_res[i][12] = j5[i][3]
        list_res[i][13] = int(j5[i][2])
        list_res[i][14] = j6[i][3]
        list_res[i][15] = int(j6[i][2])
        list_res[i][16] = j7[i][3]
        list_res[i][17] = int(j7[i][2])
        list_res[i][18] = j8[i][3]
        list_res[i][19] = int(j8[i][2])
        list_res[i][20] = j9[i][3]
        list_res[i][21] = int(j9[i][2])

    lsls = 1
    if len(list_res) <= 100:
        lsls = len(list_res) - 1
    else:
        lsls = 100

    for shu in range(lsls):
        if len(list_res) > lsls:
            print(list_res[len(list_res) - (lsls - shu)])
        else:
            print("[请修改显示参数]")

    print("显现 合计：")
    for y in [30, 13]:
        p0 = 0
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        p6 = 0
        p7 = 0
        p8 = 0
        p9 = 0

        for i in range(len(args)):
            if i >= (len(args) - int(y)):
                for k in range(5):
                    if args[i][1][k] == "0":
                        p0 = p0 + 1
                    if args[i][1][k] == "1":
                        p1 = p1 + 1
                    if args[i][1][k] == "2":
                        p2 = p2 + 1
                    if args[i][1][k] == "3":
                        p3 = p3 + 1
                    if args[i][1][k] == "4":
                        p4 = p4 + 1
                    if args[i][1][k] == "5":
                        p5 = p5 + 1
                    if args[i][1][k] == "6":
                        p6 = p6 + 1
                    if args[i][1][k] == "7":
                        p7 = p7 + 1
                    if args[i][1][k] == "8":
                        p8 = p8 + 1
                    if args[i][1][k] == "9":
                        p9 = p9 + 1
                    else:
                        pass
                else:
                    pass
        xlist2 = {
            "0C": p0,
            "1C": p1,
            "2C": p2,
            "3C": p3,
            "4C": p4,
            "5C": p5,
            "6C": p6,
            "7C": p7,
            "8C": p8,
            "9C": p9}
        dict4 = sorted(xlist2.items(), key=lambda asd: asd[1], reverse=True)
        print(dict4)

    print("error 合计：")
    for x in [30, 13]:
        error0 = 0
        error1 = 0
        error2 = 0
        error3 = 0
        error4 = 0
        error5 = 0
        error6 = 0
        error7 = 0
        error8 = 0
        error9 = 0

        for i in range(len(list_res)):
            if i >= (len(list_res) - int(x)):
                if list_res[i][2] == "|0--":
                    error0 = error0 + 1
                if list_res[i][4] == "|1--":
                    error1 = error1 + 1
                if list_res[i][6] == "|2--":
                    error2 = error2 + 1
                if list_res[i][8] == "|3--":
                    error3 = error3 + 1
                if list_res[i][10] == "|4--":
                    error4 = error4 + 1
                if list_res[i][12] == "|5--":
                    error5 = error5 + 1
                if list_res[i][14] == "|6--":
                    error6 = error6 + 1
                if list_res[i][16] == "|7--":
                    error7 = error7 + 1
                if list_res[i][18] == "|8--":
                    error8 = error8 + 1
                if list_res[i][20] == "|9--":
                    error9 = error9 + 1
                else:
                    pass
            else:
                pass
        xlist2 = {
            "0E": error0,
            "1E": error1,
            "2E": error2,
            "3E": error3,
            "4E": error4,
            "5E": error5,
            "6E": error6,
            "7E": error7,
            "8E": error8,
            "9E": error9
        }
        dict4 = sorted(xlist2.items(), key=lambda asd: asd[1], reverse=False)
        print(dict4)

    print("pass 合计：")
    for x in [30, 13]:
        rst0 = 0
        rst1 = 0
        rst2 = 0
        rst3 = 0
        rst4 = 0
        rst5 = 0
        rst6 = 0
        rst7 = 0
        rst8 = 0
        rst9 = 0

        for i in range(len(list_res)):
            if i >= (len(list_res) - int(x)):
                if list_res[i][2] == "|0对":
                    rst0 = rst0 + 1
                if list_res[i][4] == "|1对":
                    rst1 = rst1 + 1
                if list_res[i][6] == "|2对":
                    rst2 = rst2 + 1
                if list_res[i][8] == "|3对":
                    rst3 = rst3 + 1
                if list_res[i][10] == "|4对":
                    rst4 = rst4 + 1
                if list_res[i][12] == "|5对":
                    rst5 = rst5 + 1
                if list_res[i][14] == "|6对":
                    rst6 = rst6 + 1
                if list_res[i][16] == "|7对":
                    rst7 = rst7 + 1
                if list_res[i][18] == "|8对":
                    rst8 = rst8 + 1
                if list_res[i][20] == "|9对":
                    rst9 = rst9 + 1
                else:
                    pass
            else:
                pass
        xlist2 = {
            "0P": rst0,
            "1P": rst1,
            "2P": rst2,
            "3P": rst3,
            "4P": rst4,
            "5P": rst5,
            "6P": rst6,
            "7P": rst7,
            "8P": rst8,
            "9P": rst9
        }
        dict4 = sorted(xlist2.items(), key=lambda asd: asd[1], reverse=True)
        print(dict4)


if __name__ == '__main__':
    ar = get_info()
    getValue(ar)
    time.sleep(20)
    # while True:
    #     try:
    #         tss = datetime.datetime.now()
    #         if "09" <= str(tss.strftime('%H')) < "23":
    #             if str(tss.strftime('%M:%S')) in ['12:50', '32:50', '52:50']:
    #                 print(tss.strftime('%Y-%m-%d %H:%M:%S'))
    #                 ar = get_info()
    #                 getValue(ar)
    #             else:
    #                 pass

    #         else:
    #             pass
    #     except Exception as eve:
    #         print(eve)
