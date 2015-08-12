#!/usr/bin/env python
# -*- coding: utf8 -*-
import MySQLdb
raw = [x.split(";") for x in open("/home/alexandr/E2E/2015_6_crashes.csv")]
rmp = {}
db = MySQLdb.connect(host="localhost", user="root", passwd="admin", db="django_tech_smart", charset='utf8')
cursor = db.cursor()
MONTH = "06.2015"
for CRASH_CODE, NODE_CODE, DISTRICT, S_ATV, S_VPTV, S_VBB, S_VBB_ETH, DATE_REPORT, DATE_BEGIN, DATE_OVER, CINTERVAL, CRASH_REASON, CRASH_DESCR, CITY, HOUSE, HOUSE_ID, SYSUSER, Q_ABON_SERV_ATV, Q_ABON_SERV_DTV, Q_ABON_SERV_VBB, Q_ABON_SERV_ETH, Q_ABON_SERV_OTT, Q_ABON, COUNT_FLAT, TREATMENTS, DEPARTMENT, DATE_REG, DATE_OVEROPER, TITLE_, STARTDATE, ENDDATE, SDINTERVAL in raw:
    CITY = CITY.decode('cp1251').encode('utf8')
    if CITY == "\"Вінниця\"":
        CRASH_CODE = "".join(CRASH_CODE.split("\"")[0:-1])
        DATE_REPORT = "".join(DATE_REPORT.split("\"")[0:-1])
        DATE_BEGIN = "".join(DATE_BEGIN.split("\"")[0:-1])
        DATE_OVER = "".join(DATE_OVER.split("\"")[0:-1])
        CINTERVAL = "".join(CINTERVAL.split("\"")[0:-1])
        S_VPTV = int("".join(S_VPTV.split("\"")[0:-1]))
        S_ATV = int("".join(S_ATV.split("\"")[0:-1]))
        S_VBB = int("".join(S_VBB.split("\"")[0:-1]))
        S_VBB_ETH = int("".join(S_VBB_ETH.split("\"")[0:-1]))
        HOUSE = HOUSE.decode('cp1251').encode('utf8')
        SYSUSER = SYSUSER.decode('cp1251').encode('utf8')
        DISTRICT = DISTRICT.decode('cp1251').encode('utf8')
        DEPARTMENT = DEPARTMENT.decode('cp1251').encode('utf8')
        CRASH_REASON = CRASH_REASON.decode('cp1251').encode('utf8')
        CRASH_DESCR = CRASH_DESCR.decode('cp1251').encode('utf8')
        COUNT_FLAT = int("".join(COUNT_FLAT.split("\"")[0:-1]))
        Q_ABON_SERV_ATV = int("".join(Q_ABON_SERV_ATV.split("\"")[0:-1]))
        Q_ABON_SERV_DTV = int("".join(Q_ABON_SERV_DTV.split("\"")[0:-1]))
        Q_ABON_SERV_VBB = int("".join(Q_ABON_SERV_VBB.split("\"")[0:-1]))
        Q_ABON_SERV_ETH = int("".join(Q_ABON_SERV_ETH.split("\"")[0:-1]))
        Q_ABON_SERV_OTT = int("".join(Q_ABON_SERV_OTT.split("\"")[0:-1]))
        Q_ABON = int("".join(Q_ABON.split("\"")[0:-1]))
        sql = """INSERT INTO E2E (CRASH_CODE, NODE_CODE, DISTRICT, S_ATV, S_VPTV, S_VBB, S_VBB_ETH, DATE_REPORT, DATE_BEGIN, DATE_OVER, CINTERVAL, CRASH_REASON, CRASH_DESCR, HOUSE, HOUSE_ID, SYSUSER, Q_ABON_SERV_ATV, Q_ABON_SERV_DTV, Q_ABON_SERV_VBB, Q_ABON_SERV_ETH, Q_ABON_SERV_OTT, Q_ABON, COUNT_FLAT, TREATMENTS, DEPARTMENT, DATE_REG, DATE_OVEROPER, MONTH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        sql_params = (CRASH_CODE, NODE_CODE, DISTRICT, S_ATV, S_VPTV, S_VBB, S_VBB_ETH, DATE_REPORT, DATE_BEGIN, DATE_OVER, CINTERVAL, CRASH_REASON, CRASH_DESCR, HOUSE, HOUSE_ID, SYSUSER, Q_ABON_SERV_ATV, Q_ABON_SERV_DTV, Q_ABON_SERV_VBB, Q_ABON_SERV_ETH, Q_ABON_SERV_OTT, Q_ABON, COUNT_FLAT, TREATMENTS, DEPARTMENT, DATE_REG, DATE_OVEROPER, MONTH)
        cursor.execute(sql, sql_params)
        db.commit()
db.close()
print 'Job well done'