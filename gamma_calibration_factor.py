# -*- coding: UTF-8 -*-
import numpy as np
from scipy.optimize import curve_fit


def gamma_function(x, a, b):
    '''拟合的gamma函数参数就是a和gamma'''
    return a * (x ** b)


class gamma_calibration_factor:
    '''
    crt 显示器单位 从nanoamperes转到candelas per squar
    对于采集的大于23组的3个亮度表，然后被用来开发一个转换因子(conversion factor)，以从辐射计的安培度数为每平方米的坎德拉。
    尺寸至少为5 cm x 5 cm（但不超过屏幕面积的25%）的测试正方形进行校准。测试区域外的屏幕应保持黑色
    DAC值从（0，0，0）开始，逐渐增加到（255，0，0）。对于低值（低于100），增量为8，对于较高值，增量为16。
    输入的 Gamma_principal_colour [[[value,Lr]，...]
                                  [[value,Lg]，...]
                                  [[value,Lg]],...]
    '''


    def __init__(self):
        '''是否需要黑电平校正(gain)、偏移(offset)'''
        self.GO_params = [1.0, 1.0]  # 初始增益、偏移


    def gamma_calibration(self, Gamma_principal_colour):


        '''
        params:
        params[0]-R通道的  params[1]-G通道的  params[2]-B通道的
        '''
        params = np.zeros((3,2))
        Gpc=Gamma_principal_colour
        params[0] = curve_fit(gamma_function, Gpc[0][:, 0], Gpc[0][:, 1] )[0]
        params[1] = curve_fit(gamma_function, Gpc[1][:, 0], Gpc[1][:, 1] )[0]
        params[2] = curve_fit(gamma_function, Gpc[2][:, 0], Gpc[2][:, 1])[0]
        self.params=params

    def get_params(self):
        return self.params

#
# #sample
# Asus_data=np.array([ [[2,4],[2,4],[2,4]],      [[2,4],[2,4],[2,4]],      [[2,4],[2,4],[2,4]]    ])
# Asus_gamma_params=gamma_calibration_factor()
# Asus_gamma_params.gamma_calibration(Asus_data)
# Asus_gamma_params.get_params()
