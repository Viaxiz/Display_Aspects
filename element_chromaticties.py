# -*- coding: UTF-8 -*-
import numpy as np


class element_chromaticties:
    '''B2 设备需要初始校准'''

    def __init__(self):
        '''是否需要黑电平校正(gain)、偏移(offset)'''
        self.params=[1.0,1.0] # 初始增益、偏移
        self.A= np.zeros((3,3))

    def element_Chromaticities(self,principal_color_element):
        '''B.3.1 要求至少覆盖光度计采样面积的十倍，最好至少覆盖屏幕的80%
            DAC值为（255，0，0） (0,255,0) (0,0，255)
            输入的 principal_color_element [[xr,yr]，[xg,yg]，[xb,yb]]
        '''
        A=self.A
        Pce=principal_color_element
        A[0]= np.array([i[0]/i[1] for i in Pce ])
        A[1]=np.array([1,1,1])
        A[2]=np.array([(1-i[0]-i[1])/i[1] for i in Pce])
        self.A = np.matrix(A)

    def get_A(self):
        '''输出的是martrix A'''
        return self.A

    def get_pinvA(self):
        '''输出的是martrix (A的逆)'''
        return np.linalg.pinv(self.A)



# #sample
# Ausu_chromaticties=element_chromaticties()
#
# principal_color_element=np.array([[1/4,1/4],[1/4,1/4],[1/4,1/4]])
#
# Ausu_chromaticties.element_Chromaticities(np.array(principal_color_element))
#
# Ausu_chromaticties.get_A()
#
# Ausu_chromaticties.get_pinvA()