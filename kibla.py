#!/usr/bin/python
# -*- coding: utf-8 -*-


#a==============================================================================
#a    Objective : account of the Qiblah                                                      
#a    Author: Ahmed Raghdi <asmaaarab@gmail.com>                                   
#a    License: "Waqf" General Public License :
#a    http://www.ojuba.org/wiki/doku.php/waqf/license 
#a==============================================================================

#a==============================================================================
#a   ‫الخوارزمية مأخوذة من المؤلف الموسوم بـ:‬
#a   ‫القانون الرياضي لاتجاه الكعبة وتطبيقاته‬                              
#a   ‫تأليف: محمد العربي اللبي‬
#a   ‫قسم الرياضيات‬
#a   ‫ج امعة البحرين‬
#a   E-mail: labbi@sci.uob.bh‬‬
#a   ‫بتاريخ 24 ربيع الأول 1431‬
#a==============================================================================



import math


lat_makka = 21.422293
lon_makka = 39.825726
dif_lat_makka = 90-lat_makka

def Leeway(lat_city, lon_city):
    '''
    take latitude & longitude of city
    retun leeway of Qiblah by degrees
    '''
    dif_lon = math.fabs(lon_city - lon_makka)
    dif_lat_city = (90 - lat_city)
    tm = math.tan(math.radians(dif_lat_makka))
    cc = math.cos(math.radians(dif_lat_city))
    sc = math.sin(math.radians(dif_lat_city))
    cl = math.cos(math.radians(dif_lon))
    sl = math.sin(math.radians(dif_lon))
    A = math.atan((((cc)*(cl))-((1/tm)*(sc)))/sl)
    leeway = math.degrees(A)+90
    return leeway

def Direction(lat_city, lon_city):
    '''
    Take latitude & longitude of city
    retun direction of Qiblah
    '''
    if lon_makka > lon_city :
        direction = "East"
    elif lon_makka < lon_city :
        direction = "West"
    elif lat_makka == lat_city:
        if lat_makka > lat_city:
            direction = "North"
        if lat_makka < lat_city:
            direction = "South"
        elif lat_makka == lat_city:
            direction = "Qiblah"
    return direction

def Distance(lat_city, lon_city):
    '''
    take latitude & longitude of city
    retun distance from Makkah by km
    '''
    R = 6378.1
    dif_lon = math.fabs(lon_makka-lon_city)
    cm = math.cos(math.radians(lat_makka))
    sm = math.sin(math.radians(lat_makka))
    cc = math.cos(math.radians(lat_city))
    sc = math.sin(math.radians(lat_city))
    cd = math.cos(math.radians(dif_lon))
    distance = R*(math.acos((sm*sc)+(cm*cc*cd)))
    return distance
