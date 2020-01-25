from django.shortcuts import render
from django.shortcuts import HttpResponse
from DataSite import models
import hashlib
import base64
import time
from datetime import datetime  # 导入datetime模块
import json
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    if request.method == 'POST':
        account = request.POST.get("loginUseraccount", None)
        password = request.POST.get("loginPassword", None)
        a = (account + password)
        epassword = encode(a)
        try:
            qUser = models.User_Info.objects.get(Account=account)
            dbPassword = qUser.Password
        except:
            return render(request, 'login.html', {'error': "查无此账号！"}, )
        if epassword == dbPassword:
            request.session['UserID'] = qUser.id
            request.session['UserAccount'] = qUser.Account
            request.session['UserName'] = qUser.Name
            request.session['UserDepartment'] = getDepartment(qUser)
            request.session.set_expiry(600)
            return home(request)
        else:
            return render(request, 'login.html', {'error': "账号密码错误！"}, )


def home(request):
    # 获取登陆用户对应的全部记录
    tRecord = models.User_Info.objects.get(id=request.session['UserID'])
    # 通过这一行的Project字段跨表到Project_Info表里找到对应的全部数据行的对象
    tProjectQuerySet = tRecord.Project.all()
    tProjectList = []
    tProjectID = request.POST.get("ProjectID", None);
    if tProjectID is None:
        tProjectID = 0
        i = 0
        tDateTime = datetime.date(datetime(1900, 1, 1))
        for feProject in tProjectQuerySet:
            tProjectList.append(feProject)
            if tProjectList[i].CreateDate > tDateTime:
                tDateTime = tProjectList[i].CreateDate
                tProjectID = i
        # 返回用户信息及项目列表
        return render(request, 'moe_HOME.html', {'UserName': request.session['UserName'], 'ProjectID': tProjectID, 'ProjectList': tProjectList})
    else:
        return render(request, 'moe_HOME.html', {'UserName': request.session['UserName'], 'ProjectID': tProjectID, 'ProjectList': tProjectList})


def getDepartment(pUser):
    try:
        departmentset = pUser.departments_set.all()
        rtDep = "";
        for fDep in departmentset:
            rtDep = rtDep + '\n' + fDep.Name
    except:
        rtDep = " "
    return rtDep


def encode(s):
    b = bytes(s, encoding='gb2312')
    h = hashlib.sha512(b).digest()
    c = base64.b64encode(h)
    d = str(c, encoding='gb2312')
    return d
