# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from gamma_calibration_factor import gamma_calibration_factor
from element_chromaticties import element_chromaticties


def CIE2RGB(gamma_parm,A,CIEXYZ):
    '''
    :param gamma_parm:选用的各通道gamma参数列表 输入格式np 3×2
    :param A:所求的chromaticties_MAT, 当前的A或A逆，输入格式的是np.matrix()
    :param CIEXYZ: 需要反向的求RGB的XYZ 输入格式为np 3×n
    :return: 返回要求的RGB 输出的RGB为np 3×n
    '''


    XYZ_MAT=np.matrix(CIEXYZ)
    L_MAT=A*XYZ_MAT
    Lrgb=L_MAT.A    #给出的n×3的亮度np.array 用于伽马函数计算DAC(R,G,B)
    print('Lrgb',Lrgb[:,0])
    DAC=np.zeros_like(Lrgb)

    DAC[0] =   np.power(Lrgb[0]/ gamma_parm[0][0], 1/gamma_parm[0][1])
    DAC[1] =   np.power(Lrgb[1]/ gamma_parm[1][0], 1/gamma_parm[1][1])
    DAC[2] =   np.power(Lrgb[2]/ gamma_parm[2][0], 1/gamma_parm[2][1])

    print('DAC',DAC[:,0])
    return DAC


if __name__ == '__main__':
    Ausu_chromaticties = element_chromaticties()
    #读入三原色色块的xy,得到矩阵A
    path='ASUS_test.xlsx'
    ASUS_df=pd.read_excel(path)
    chromaticties=np.array(ASUS_df[['x','y']])
    principal_color_element=chromaticties[0:3,]
    Ausu_chromaticties.element_Chromaticities(np.array(principal_color_element))
    A=Ausu_chromaticties.get_A()
    # 读入各原色色块gamma值,得到伽马校正系数
    Asus_gamma_params = gamma_calibration_factor()
    gamma_data= np.array(ASUS_df['Lv'])
    R_gamma_data,G_gamma_data,B_gamma_data = [[0,gamma_data[3]]],[[0,gamma_data[3]]],[[0,gamma_data[3]]]
    for i in range(32):
        R_gamma_data.append([8+8*i,gamma_data[4+i]])
        G_gamma_data.append([8+8*i,gamma_data[36+i]])
        B_gamma_data.append([8+8*i,gamma_data[68+i]])
    Asus_data = np.array([R_gamma_data, G_gamma_data, B_gamma_data])
    Asus_gamma_params.gamma_calibration(Asus_data)
    gamma_params=Asus_gamma_params.get_params()

    # 读入各色块的xyL，转为XYZ，在转换为RGB



    for i in ['DAY_WHITEBACK', 'DAY_BRIGHT', 'DAY_BLACKBACK', 'DUST', 'NIGHT']:
        df = pd.read_excel('Colour_table.xlsx', sheet_name=i)

        xyL = np.array(df[['x', 'y', 'LUMINANCE']]).T

        XpYpZ=xyL[2]/xyL[1]

        XYZ=np.zeros_like(xyL)

        XYZ[0] = xyL[0]*XpYpZ

        XYZ[1] = xyL[2]

        XYZ[2] = (1-xyL[0]-xyL[1])*XpYpZ

        DAC = CIE2RGB(gamma_params,np.linalg.pinv(A),XYZ)
        print(xyL[:,0])
        print(XYZ[:,0])
        print(DAC[:,0])
        input()



