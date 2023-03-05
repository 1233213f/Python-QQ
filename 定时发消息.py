#coding: utf-8
import pymysql	#导入pymysql模块

db = pymysql.connect("localhost","root","root","info_db" )  		#数据库链接信息
cursor = db.cursor()

#插入任务
def insertSchedule(schedule):
    insertsql = "insert into dutyschedule_tb(worktime,name) values(%s,%s)"
    try:
	    #这种查询语句可以防止sql注入
        cursor.execute(insertsql,(schedule['worktime'],schedule['name']))
        db.commit()
    except Exception:
        db.rollback()
        raise Exception

#删除任务
def deleteSchedule():
    deletesql = ""
    try:
        cursor.execute(deletesql)
        db.commit()
    except Exception:
        db.rollback()

def updateSchedule(user):
    updatesql = ""
    try:
        cursor.execute(updatesql)
        db.commit()
    except Exception:
        db.rollback()

#获取下一个任务
def findScheduleByNewTime():
    selectsql = "SELECT * FROM dutyschedule_tb where NOW() <= date_format(worktime,'%Y-%m-%d %H:%i:%S') ORDER BY worktime ASC;"
    try:
        cursor.execute(selectsql)
        results = cursor.fetchone()
        schedule = {}
        schedule['worktime'] = results[1]
        schedule['name'] = results[2]
        schedule['content'] = results[3]
        return schedule
    except Exception:
        return None
