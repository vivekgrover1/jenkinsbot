#!/usr/bin/python3

import pymysql


def get_status(user):
    # Open database connection
    db = pymysql.connect("db", "jenkinsbot", "jenkinsbot", "jenkinsbotdb")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # Prepare SQL query to INSERT a record into the database.
    sql = "select approval_status from jenkinsbot_job_status where username='{0}'".format(user)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            return (row[0])
    except:
        return "Error: unable to fetch data"
    # disconnect from server
    db.close()


def update_status(user):
    db = pymysql.connect("db", "jenkinsbot", "jenkinsbot", "jenkinsbotdb")
    cursor = db.cursor()
    sql = "update jenkinsbot_job_status set approval_status='Approved' where username='{0}'".format(user)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def add_user(user):
    db = pymysql.connect("db", "jenkinsbot", "jenkinsbot", "jenkinsbotdb")
    cursor = db.cursor()
    sql = "If Not Exists(select * from jenkinsbot_job_status where username='{0}') \
           Begin \
           insert into jenkinsbot_job_status values ('{0}','Not Approved') End".format(user)
    #sql = "insert into jenkinsbot_job_status values ('%s','Not Approved')" % user
    try:
        cursor.execute(sql)
        db.commit()

    except:
        db.rollback()
    db.close()
