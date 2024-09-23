from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import MySQLdb
from .models import Post, main_notice, banner, dday
from datetime import datetime
import re
import json


config = {
    'host' : 'localhost',
    'user' : 'root',
    'password': 'a1b2c3d4e5',
    'database' : 'menondb',
    'port' :3306,
    'charset': 'utf8',
    'use_unicode' : True
}
today = datetime.today().date()
print(today)

def home(request):
    sql = 'SELECT * FROM home_main_notice'
    sql2 = 'SELECT * FROM home_banner'
    sql3 = 'SELECT * FROM home_dday'
    sql4 = 'SELECT * FROM home_gallery'
    sql5 = 'SELECT * FROM home_post'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        cursor.execute(sql)
        notice = cursor.fetchall()
        cursor.execute(sql2)
        banner = cursor.fetchall()
        cursor.execute(sql3)
        dday = cursor.fetchall()
        cursor.execute(sql4)
        gallery = cursor.fetchall()
        cursor.execute(sql5)
        posts = cursor.fetchall()

        conn.commit()  # 변경 사항을 커밋
        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        notice = []
        banner = []
        dday = []
        gallery = []

    post_list = []
    for item in posts:
        # 예를 들어, item[1]이 태그라고 가정하고 분리
        tags = item[4].split(' ')  # 띄어쓰기로 분리
        # 각 항목을 리스트로 변환하고 태그도 추가
        post_list.append(list(item) + [tags])  # 태그를 마지막에 추가
    

    return render(request, 'base.html', {'notice': notice, 'banner':banner, 'gallery':gallery,'posts':post_list})

def main(request):
    sql = 'SELECT * FROM home_main_notice'
    sql2 = 'SELECT * FROM home_banner'
    sql3 = 'SELECT * FROM home_dday'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        cursor.execute(sql)
        notice = cursor.fetchall()
        cursor.execute(sql2)
        banner = cursor.fetchall()
        cursor.execute(sql3)
        dday = cursor.fetchall()

        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        notice = []
        banner = []
        dday = []

    dday_list = []
    
    for i in dday:
        target = i[2]
        d_day = (today - target).days
        dday_list.append(list(i) + [d_day])

    return render(request, 'main.html', {'notice': notice, 'banner':banner, 'dday':dday_list})

def section2(request):
    sql = 'SELECT * FROM home_post'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        cursor.execute(sql)
        post = cursor.fetchall()
        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        post = []
        
    post_list = []
    for item in post:
        # 예를 들어, item[1]이 태그라고 가정하고 분리
        tags = item[4].split(' ')  # 띄어쓰기로 분리
        # 각 항목을 리스트로 변환하고 태그도 추가
        post_list.append(list(item) + [tags])  # 태그를 마지막에 추가

    return render(request, 'section2.html', {'post':post_list})

def gallery(request):
    sql4 = 'SELECT * FROM home_gallery ORDER BY id DESC'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        cursor.execute(sql4)
        gallery = cursor.fetchall()
        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        gallery = []

    return render(request, 'gallery.html', {'gallery':gallery,})

def section4(request):
    sql = 'SELECT * FROM home_post'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        cursor.execute(sql)
        post = cursor.fetchall()
        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        post = []
        
    post_list = []
    for item in post:
        # 예를 들어, item[1]이 태그라고 가정하고 분리
        tags = item[4].split(' ')  # 띄어쓰기로 분리
        # 각 항목을 리스트로 변환하고 태그도 추가
        post_list.append(list(item) + [tags])  # 태그를 마지막에 추가
    return render(request, 'section4.html',{'post':post_list})

def section5(request):
    sql = 'SELECT * FROM home_post'
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()

        cursor.execute(sql)
        post = cursor.fetchall()
        conn.close()  # 연결 종료
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        post = []
        
    post_list = []
    for item in post:
        # 예를 들어, item[1]이 태그라고 가정하고 분리
        tags = item[4].split(' ')  # 띄어쓰기로 분리
        # 각 항목을 리스트로 변환하고 태그도 추가
        post_list.append(list(item) + [tags])  # 태그를 마지막에 추가
    return render(request, 'section5.html',{'post':post_list})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.tag:
        tags = post.tag.split()  # 띄어쓰기로 분리하여 리스트로 변환
    else:
        tags = []

    return render(request, 'post_detail.html', {'post': post, 'tags': tags})