#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : yag8009
# @FileName  : dijia
# @Time    : 2020/2/13
import random

from public_random.random_ID_card import random_ID_card
from public_random.random_city import random_city
from public_random.random_cn_name import random_cn_name
from public_random.random_phone import random_phone


class DiJia:
    def __init__(self):
        self.images = "/images/other/20200213/f99f97dfe248465f9b457df707bd1540.jpeg"
        self.lis = [('503746195503181140', '宋狰汉', '15531093663', '湖北荆州市公安县'),
                    ('64901119710308930X', '朱镉', '15528358237', '山西长治市屯留县'),
                    ('511516196706271061', '岑艴', '15528643210', '天津河西区全境'),
                    ('45301619680319924X', '奚阌巨', '15530147306', '江苏淮安市楚州区'),
                    ('815170195006166750', '郝裤锃', '15502007944', '河北沧州市肃宁县'),
                    ('325462195805206560', '于倪怀', '15542504023', '北京房山区南窖乡'),
                    ('126236195110185521', '秦蹁忮', '15528358237', '湖南郴州市宜章县'),
                    ('228222194301265121', '苏蹈焯', '15502007944', '山东泰安市东平县'),
                    ('910451196405093481', '郝兼台', '15568788956', '山东聊城市临清市'),
                    ('713801197703013740', '汪汀可', '15502705326', '宁夏银川市贺兰县')]

        # self.lis = []
        # for i in range(0, 1000):
        #     self.lis.append((random_ID_card(), random_cn_name(), random_phone(), ''.join(random_city())))
        # print(self.lis)

        with open('C:\\Users\\admin\\Downloads\\data\\useriddata.csv', 'r') as f:
            userids = f.read()
            self.user_id = userids.split("\n")

        with open('C:\\Users\\admin\\Downloads\\data\\testphone.csv', 'r') as f:
            phone = f.read()
            self.xphone = phone.split("\n")

    # 注册
    def zhu_ce(self):
        with open('C:\\Users\\admin\\Downloads\\data\\zhucedata.csv', 'w+') as f:  # 设置文件对象
            for i in range(len(self.lis)):
                f.write('注册帐号@/svc/api/zsUser/register@{"referrer": "","phone": "' + self.lis[i][
                    2] + '","smsCode": "111111","password": "w123456"}' + "\n")
        with open('C:\\Users\\admin\\Downloads\\data\\shenfendata.csv', 'w+') as f:  # 设置文件对象
            for i in range(len(self.lis)):
                f.write(
                    '身份识别@/svc/api/zsUser/userCheck@{\
"Idcardnumber":"' + self.lis[i][0] + '",\
"Idcardaddress":"' + self.lis[i][3] + '",\
"Idcardname":"' + self.lis[i][1] + '",\
"type":"1",\
"Idcardvalidity":"20170627-20370627"\
}' + "\n")

    # 个人商户
    def Ge_Ren(self):
        with open('C:\\Users\\admin\\Downloads\\data\\gerendata.csv', 'w+') as fgeren:  # 设置文件对象
            for i in range(len(self.user_id)):
                fgeren.write('个人商户@/svc/api/zsUser/registerMerchant@{\
"city":"北京市",\
"netName":"个人网点",\
"userCardHead":"' + self.images + '",\
"province":"北京",\
"photo":"' + self.images + '",\
"userId":"' + self.user_id[i] + '",\
"district":"东城区",\
"userCardCountry":"' + self.images + '",\
"detailAddress":"个人网点地址",\
"userType":"1"\
}' + "\n")

    # 企业商户
    def Qi_Ye(self):
        with open('C:\\Users\\admin\\Downloads\\data\\qiyedata.csv', 'w+') as fqiye:  # 设置文件对象
            for i in range(len(self.user_id)):
                fqiye.write('企业商户@/svc/api/zsUser/registerMerchant@{\
"qyCardHead":"' + self.images + '",\
"qyAccountName":"企业开户名称",\
"qyCardId":"123321199901010011",\
"city":"北京市",\
"qyUserName":"企业法人",\
"netName":"企业网点名称",\
"qyImg":"' + self.images + '",\
"userCardHead":"' + self.images + '",\
"qyAccountBank":"企业开户银行",\
"qyAccountNum":"123456789012345",\
"province":"北京",\
"qyCardCountry":"' + self.images + '",\
"qyUserPhone":"' + self.lis[i][2] + '",\
"photo":"' + self.images + '",\
"qyAccountImg":"' + self.images + '",\
"userId":"' + self.user_id[i] + '",\
"qyName":"企业名称",\
"district":"东城区",\
"userCardCountry":"' + self.images + '",\
"detailAddress":"企业网点名称地址",\
"userType":"2"\
}' + "\n")

    # 查询号码
    def Cha_Xun(self):
        with open('C:\\Users\\admin\\Downloads\\data\\xuanphonedata.csv', 'w+') as f:  # 设置文件对象
            for i in range(1, 10):
                f.write('查询号码@/svc/api/phone/findPhoneList@{\
"pattern_def_id":"",\
"hrl":"2800986",\
"region_id":"",\
"pagesize":"30",\
"matchCount":"",\
"net":"",\
"matchPattern":"",\
"pagenumber":"1",\
"res_level":""\
}' + "\n")

    # 预开卡
    def Yu_Kai_Ka(self):
        with open('C:\\Users\\admin\\Downloads\\data\\yukaikadata7.csv', 'w+') as fyukaika:  # 设置文件对象
            for i in range(len(self.xphone)):
                user_id = random.choice(self.user_id)
                fyukaika.write(
                    '预开卡@/svc/api/order/saveBuyOrder@{\
"cardAddress":"北京市朝阳区兰花苑南路7号靠近玛尔比恩(LamarBeane)国际早教中心",\
"orderType":"1",\
"originalPrice":"0",\
"city":"北京市",\
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
"detailedAddress":"北京市朝阳区兰花苑南路7号靠近玛尔比恩(LamarBeane)国际早教中心",\
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
"userId":"' + user_id + '",\
"yc_s_price":"0",\
"cardOrg":"",\
"comboLlId":"1197062912992792576",\
"phone":"' + self.xphone[i] + '",\
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
}@' + user_id + "\n")


    # 正常开卡
    def Kai_Ka(self):
        with open('C:\\Users\\admin\\Downloads\\data\\kaikadata.csv', 'w+') as fkaika:  # 设置文件对象
            for i in range(len(self.xphone)):
                user_id = random.choice(self.user_id)
                lis = random.choice(self.lis)
                fkaika.write(
                    '正常开卡@/svc/api/order/saveBuyOrder@{\
"cardAddress":"' + lis[3] + '",\
"orderType":"0",\
"originalPrice":"0",\
"city":"北京市",\
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
"userHead":"' + self.images + '",\
"price":"0",\
"comboLhName":"",\
"detailedAddress":"北京市朝阳区兰花苑南路7号靠近玛尔比恩(LamarBeane)国际早教中心",\
"ycCode":"",\
"userBirthday":"' + lis[0][6:14] + '",\
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
"userName":"' + lis[1] + '",\
"userId":"' + user_id + '",\
"yc_s_price":"0",\
"cardOrg":"' + lis[3][-3:-1] + '公安局",\
"comboLlId":"1197062912992792576",\
"phone":"' + self.xphone[i] + '",\
"num_s_price":"0",\
"lh_c_price":"0",\
"num_c_price":"0",\
"comboZzName":"",\
"yc_c_price":"0",\
"userCardId":"' + lis[0] + '",\
"comboJbId":"1197062559077421056",\
"lh_s_price":"0",\
"dxCode":"",\
"comboLhId":""\
}@' + user_id + "\n")


if __name__ == "__main__":
    # DiJia().zhu_ce()
    # DiJia().Ge_Ren()
    # DiJia().Qi_Ye()
    # DiJia().Cha_Xun()
    DiJia().Yu_Kai_Ka()
    # DiJia().Kai_Ka()
    print("OK!!!")
