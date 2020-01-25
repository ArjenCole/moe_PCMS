from django.shortcuts import render
from django.shortcuts import HttpResponse
from DataSite.models import User_Info
import hashlib
import base64
import time
import datetime
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
            qUser = User_Info.objects.get(Account=account)
            dbPassword = qUser.Password
        except:
            return render(request, 'login.html', {'error': "查无此账号！"}, )
        if epassword == dbPassword:
            request.session['UserAccount'] = qUser.Account
            request.session['UserName'] = qUser.Name
            request.session['UserDepartment'] = getDepartment(qUser)
            request.session.set_expiry(600)
            return render(request, "moe_HOME.html")
        else:
            return render(request, 'login.html', {'error': "账号密码错误！"}, )


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
