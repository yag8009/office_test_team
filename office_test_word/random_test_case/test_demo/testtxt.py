#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : testtxt
# @Time    : 2020/2/11
import re

from public_random.random_ID_card import random_ID_card
from public_random.random_city import random_city
from public_random.random_cn_name import random_cn_name
from public_random.random_phone import random_phone
from public_random.random_string import random_numint

images = "/images/other/20200213/f99f97dfe248465f9b457df707bd1540.jpeg"


# 注册信息
def zhuceTest():
    with open('C:\\Users\\admin\\Downloads\\data\\zhucedata.csv', 'w+') as f:  # 设置文件对象
        for i in range(1, 10000):
            f.write('注册帐号@/svc/api/zsUser/register@{\
"referrer":"",\
"phone":"' + random_phone() + '",\
"smsCode":"111111",\
"password":"w123456"\
}' + "\n")


# 获取注册信息 中的phone，userid
def Txtread():
    lst = []
    with open('C:\\Users\\admin\\Downloads\\data\\zhuce_log.csv', 'r') as f:
        das = f.read()
        dat = das.split("\n")
        for i in dat:
            if "接口调用成功" in i:
                phone = re.findall(r'198.*?\"', i)
                userIds = re.findall(r'Id\":\".*?\"', i)
                lst.append(("".join(phone)[:-1], "".join(userIds)[5:-1]))
    with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'w+') as f:  # 设置文件对象
        for yw in lst:
            f.write(yw[1] + "\n")
    with open('C:\\Users\\admin\\Downloads\\data\\phonedata.csv', 'w+') as fa:  # 设置文件对象
        for yws in lst:
            fa.write(yws[0] + "\n")


# 企业
def qiyedata():
    with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'r') as f:
        das = f.read()
        dat = das.split("\n")
        with open('C:\\Users\\admin\\Downloads\\data\\qiyedata.csv', 'w+') as fqiye:  # 设置文件对象
            for userId in dat:
                fqiye.write(
                    '企业开户@/svc/api/zsUser/registerMerchant@{\
"qyCardHead":"' + images + '",\
"qyAccountName":"开户名称",\
"qyCardId":"432432199901010011",\
"city":"北京市",\
"qyUserName":"法人名称",\
"netName":"网点名称",\
"qyImg":"' + images + '",\
"userCardHead":"' + images + '",\
"qyAccountBank":"银行",\
"qyAccountNum":"123456789",\
"province":"北京",\
"qyCardCountry":"' + images + '",\
"qyUserPhone":"' + random_phone() + '",\
"photo":"' + images + '",\
"qyAccountImg":"' + images + '",\
"userId":"' + userId + '",\
"qyName":"企业名称",\
"district":"东城区",\
"userCardCountry":"' + images + '",\
"detailAddress":"地址信息",\
"userType":"2"\
}' + "\n")


# geren
def gerendata():
    with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'r') as f:
        das = f.read()
        dat = das.split("\n")
        with open('C:\\Users\\admin\\Downloads\\data\\gerendata.csv', 'w+') as fgeren:  # 设置文件对象
            for userId in dat:
                fgeren.write(
                    '个人开户@/svc/api/zsUser/registerMerchant@{\
"city":"北京市",\
"netName":"111",\
"userCardHead":"' + images + '",\
"province":"北京",\
"photo":"' + images + '",\
"userId":"' + userId + '",\
"district":"东城区",\
"userCardCountry":"' + images + '",\
"detailAddress":"222",\
"userType":"1"\
}' + "\n")


def phoneest():
    with open('C:\\Users\\admin\\Downloads\\data\\xuanphonedata.csv', 'w+') as f:  # 设置文件对象
        for i in range(1, 10000):
            f.write(
                '查询号码@/svc/api/phone/findPhoneList@{\
"pattern_def_id":"",\
"hrl":"' + random_numint(4) + '",\
"region_id":"",\
"pagesize":"20",\
"phonePart":"",\
"matchCount":"",\
"net":"",\
"matchPattern":"",\
"pagenumber":"1",\
"res_level":""\
}' + "\n")


def yukaidata():
    # lis = []
    with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'r') as f:
        userids = f.read()
        user_id = userids.split("\n")

    with open('C:\\Users\\admin\\Downloads\\data\\testphone.csv', 'r') as f:
        phone = f.read()
        xphone = phone.split("\n")

    with open('C:\\Users\\admin\\Downloads\\data\\yukaikadata.csv', 'w+') as fyukaika:  # 设置文件对象
        for lix in range(len(user_id)):
            fyukaika.write(
                '预开卡@/svc/api/order/saveBuyOrder@{\
"cardAddress":"",\
"orderType":"1",\
"originalPrice":"0",\
"city":"",\
"comboYcName":"",\
"comboZzId":"",\
"zzCode":"",\
"reserveFee":"0",\
"addressId":"110",\
"phonePrice":"0",\
"llCode":"111088800203",\
"comboDxName":"",\
"comboJbName":"（mini）芝麻29元套餐",\
"comboYcId":"",\
"comboNumId":"",\
"userHead":"",\
"price":"0",\
"comboLhName":"",\
"detailedAddress":"",\
"ycCode":"",\
"userBirthday":"",\
"userNation":"",\
"address":"北京市",\
"jbCode":"111088800201",\
"comboLlName":"特惠流量包组件（赠送，必选）",\
"cardDate":"",\
"comboDxId":"",\
"netType":"100001",\
"numCode":"",\
"comboNumName":"",\
"lhCode":"",\
"userName":"",\
"userId":"' + user_id[lix] + '",\
"yc_s_price":"0",\
"cardOrg":"",\
"comboLlId":"1197062912992792576",\
"phone":"' + xphone[lix] + '",\
"num_s_price":"0",\
"lh_c_price":"0",\
"num_c_price":"0",\
"comboZzName":"",\
"yc_c_price":"0",\
"userCardId":"",\
"comboJbId":"1197062559077421056",\
"lh_s_price":"0",\
"dxCode":"",\
"comboLhId":""\
}@' + user_id[lix] + "\n")


def kaikadata():
    with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'r') as f:
        userids = f.read()
        user_id = userids.split("\n")

    with open('C:\\Users\\admin\\Downloads\\data\\testphone.csv', 'r') as f:
        phone = f.read()
        xphone = phone.split("\n")
    with open('C:\\Users\\admin\\Downloads\\data\\kaikadata.csv', 'w+') as fkaika:  # 设置文件对象
        for lix in range(len(user_id)):
            idcord = random_ID_card()
            city = random_city()
            fkaika.write(
                '开卡@/svc/api/order/saveBuyOrder@{\
"cardAddress":"' + ''.join(city) + '",\
"orderType":"0",\
"originalPrice":"0",\
"city":"",\
"comboYcName":"",\
"comboZzId":"",\
"zzCode":"",\
"reserveFee":"0",\
"addressId":"110",\
"phonePrice":"0",\
"llCode":"111088800203",\
"comboDxName":"",\
"comboJbName":"（mini）芝麻29元套餐",\
"comboYcId":"",\
"comboNumId":"",\
"userHead":"/images/gr/20200211/71d9f73e711142dcaddac5da449d9c10.jpeg",\
"price":"0",\
"comboLhName":"",\
"detailedAddress":"",\
"ycCode":"",\
"userBirthday":"' + idcord[6:14] + '",\
"userNation":"汉",\
"address":"北京市",\
"jbCode":"111088800201",\
"comboLlName":"特惠流量包组件（赠送，必选）",\
"cardDate":"20170627-20370627",\
"comboDxId":"",\
"netType":"100001",\
"numCode":"",\
"comboNumName":"",\
"lhCode":"",\
"userName":"' + random_cn_name() + '",\
"userId":"' + user_id[lix] + '",\
"yc_s_price":"0",\
"cardOrg":"' + random_city()[2] + '公安局",\
"comboLlId":"1197062912992792576",\
"phone":"' + xphone[lix] + '",\
"num_s_price":"0",\
"lh_c_price":"0",\
"num_c_price":"0",\
"comboZzName":"",\
"yc_c_price":"0",\
"userCardId":"' + idcord + '",\
"comboJbId":"1197062559077421056",\
"lh_s_price":"0",\
"dxCode":"",\
"comboLhId":""\
}@' + user_id[lix] + "\n")


def userCheckTest():
    with open('C:\\Users\\admin\\Downloads\\data\\shenfendata.csv', 'w+') as f:  # 设置文件对象
        for i in range(1, 300000):
            f.write(
                '身份信息@/svc/api/zsUser/userCheck@{\
"Idcardnumber":"' + random_ID_card() + '",\
"Idcardaddress":"' + ''.join(random_city()) + '",\
"Idcardname":"' + random_cn_name() + '",\
"type":"1",\
"Idcardvalidity":"20170627-20370627"\
}' + "\n")


def ReadTest():
    with open('C:\\Users\\admin\\Downloads\\yukaika_log.csv', 'r') as f:
        phone = f.read()
        xphone = phone.split("\n")
    with open('C:\\Users\\admin\\Downloads\\orderId7.csv', 'w+') as fkaika:  # 设置文件对象
        for lix in xphone:
            if "20" in lix:
                fkaika.write(lix + "\n")


def ReadsTest():
    with open('C:\\Users\\admin\\Downloads\\orderId7.csv', 'r') as f:
        phone = f.read()
        xphone = phone.split("\n")
    with open('C:\\Users\\admin\\Downloads\\orderIddata7.csv', 'w+') as fkaika:  # 设置文件对象
        for lix in xphone:
            # fkaika.write('{"iccId":"280098600000000' + random_numint(4) + '","orderId":"'+lix+'"}' + "\n")
            fkaika.write('{"iccId":"280098700000001' + random_numint(4) + '","orderId":"'+lix+'"}' + "\n")

if __name__ == "__main__":
    # lis = []
    # for i in range(1, 10):
    #     lis.append((random_ID_card(), random_cn_name(), random_phone(), ''.join(random_city())))
    # print(lis)
    ReadsTest()
    # Txtread()
    # qiyedata()
    # gerendata()
    # phoneest()
    # yukaidata()
    # kaikadata()
    # userCheckTest()
    print("完成")
