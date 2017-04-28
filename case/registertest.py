# encoding: utf-8
'''
@author: lileilei
@file: registertest.py
@time: 2017/4/26 21:09
'''
import yaml,unittest,time
from log import  log_case
from public.zhuce_pub import Regust
from appium import webdriver
class Registe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        title = u'注册测试'
        cls.logs = log_case.Logger(title)
        cls.dis_app = {}
        cls.dis_app['platformName'] = 'Android'
        cls.dis_app['platformVersion'] = '5.0.2'
        cls.dis_app['deviceName'] = 'emulator-5554'
        cls.dis_app['appPackage'] = 'com.aixuetang.online'
        cls.dis_app['appActivity'] = 'com.aixuetang.mobile.activities.HomeActivity'
        cls.deriver = webdriver.Remote('http://localhost:4723/wd/hub', cls.dis_app)
        cls.faile=open(r'C:\Users\Administrator\Desktop\xuesheng\data\data_case.yaml','r',encoding='utf-8')
        cls.data=yaml.load(cls.faile)
        cls.faile.close()
        cls.data=cls.data['zhuce']
        cls.res=Regust(cls.deriver)
    def testreg_1(self):
        try:
            self.user=self.data['zhuce1']['username']
            self.password=self.data['zhuce1']['password']
            self.yanzheng=self.data['zhuce1']['yanzhengma']
            self.suc=self.data['zhuce1']['suc']
            self.asserts=self.data['zhuce1']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst1.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg1 fail  reson is :%s'%e)
    def testreg_2(self):
        try:
            self.user=self.data['zhuce2']['username']
            self.password=self.data['zhuce2']['password']
            self.yanzheng=self.data['zhuce2']['yanzhengma']
            self.suc=self.data['zhuce2']['suc']
            self.asserts=self.data['zhuce2']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst2.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg2 fail  reson is :%s'%e)
    def testreg_3(self):
        try:
            self.user=self.data['zhuce3']['username']
            self.password=self.data['zhuce3']['password']
            self.yanzheng=self.data['zhuce3']['yanzhengma']
            self.suc=self.data['zhuce3']['suc']
            self.asserts=self.data['zhuce3']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst3.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg3 fail  reson is :%s'%e)
    def testreg_4(self):
        try:
            self.user=self.data['zhuce4']['username']
            self.password=self.data['zhuce4']['password']
            self.yanzheng=self.data['zhuce4']['yanzhengma']
            self.suc=self.data['zhuce4']['suc']
            self.asserts=self.data['zhuce4']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst4.pang')
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg4 fail  reson is :%s'%e)
    def testreg_5(self):
        try:
            self.user=self.data['zhuce5']['username']
            self.password=self.data['zhuce5']['password']
            self.yanzheng=self.data['zhuce5']['yanzhengma']
            self.suc=self.data['zhuce5']['suc']
            self.asserts=self.data['zhuce5']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst5.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))

            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg5 fail  reson is :%s'%e)
    def testreg_6(self):
        try:
            self.user=self.data['zhuce6']['username']
            self.password=self.data['zhuce6']['password']
            self.yanzheng=self.data['zhuce6']['yanzhengma']
            self.suc=self.data['zhuce6']['suc']
            self.asserts=self.data['zhuce6']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst6.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg6 fail  reson is :%s'%e)
    def testreg_7(self):
        try:
            self.user=self.data['zhuce7']['username']
            self.password=self.data['zhuce7']['password']
            self.yanzheng=self.data['zhuce7']['yanzhengma']
            self.suc=self.data['zhuce7']['suc']
            self.asserts=self.data['zhuce7']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst7.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))
            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg7 fail  reson is :%s'%e)
    def testreg_8(self):
        try:
            self.user=self.data['zhuce8']['username']
            self.password=self.data['zhuce8']['password']
            self.yanzheng=self.data['zhuce8']['yanzhengma']
            self.suc=self.data['zhuce8']['suc']
            self.asserts=self.data['zhuce8']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst8.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))

            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg8 fail  reson is :%s'%e)
    def testreg_9(self):
        try:
            self.user=self.data['zhuce9']['username']
            self.password=self.data['zhuce9']['password']
            self.yanzheng=self.data['zhuce9']['yanzhengma']
            self.suc=self.data['zhuce9']['suc']
            self.asserts=self.data['zhuce9']['assert']
            self.asser_return=self.res.register2(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst9.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))

            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg9 fail  reson is :%s'%e)
    def testreg_10(self):
        try:
            self.user=self.data['zhuce10']['username']
            self.password=self.data['zhuce10']['password']
            self.yanzheng=self.data['zhuce10']['yanzhengma']
            self.suc=self.data['zhuce10']['suc']
            self.asserts=self.data['zhuce10']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst10.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))

            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg10 fail  reson is :%s'%e)
    def testreg_11(self):
        try:
            self.user=self.data['zhuce11']['username']
            self.password=self.data['zhuce11']['password']
            self.yanzheng=self.data['zhuce11']['yanzhengma']
            self.suc=self.data['zhuce11']['suc']
            self.asserts=self.data['zhuce11']['assert']
            self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\xuesheng\jietu\zhuce\regst11.pang')
            self.logs.info_log(('input data:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (self.user, self.password, self.yanzheng,self.suc, self.asserts)))

            time.sleep(1)
            self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
        except Exception as e:
            self.logs.error_log(e)
            print('reg11 fail  reson is :%s'%e)
    @classmethod
    def tearDownClass(cls):
        cls.deriver.quit()