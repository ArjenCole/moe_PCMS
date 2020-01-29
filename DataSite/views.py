from django.shortcuts import render
from django.shortcuts import HttpResponse
from DataSite import models
from DataSite import views_login
from DataSite import views_check
from DataSite import models
from django.db.models import Q
# Create your views here.


def index(request):
    # return HttpResponse("hello world!")
    return render(request, "index.html",)


def home(request):
    # return HttpResponse("hello world!")
    return render(request, "home.html",)


def login(request):
    return views_login.login(request)


def register(request):
    return render(request, "register.html",)


def tables(request):
    return render(request, "tables.html",)


def charts(request):
    return render(request, "charts.html",)


def retrieval(request):
    return render(request, "retrieval.html",)


def check(request):
    if request.method == 'GET':
        return render(request, 'check.html')
    elif request.method == 'POST':
        obj = request.FILES.get('fileInputed')
        if obj is None:
            checkList = ['未选择校验文件']
            return render(request, "check.html", {"checkList": checkList})
        else:
            # f = open(os.path.join('uploadFiles', obj.name), 'wb')
            tFilePath = 'E:\\CIDP\\UPLOADCHECK\\' + obj.name
            tFile = open(tFilePath, 'wb')
            for line in obj.chunks():
                tFile.write(line)
            tFile.close()
            # checkList = ['physics', 'chemistry', 1997, 2000]
            checkList = views_check.CheckFile(tFilePath)
            return render(request, "check.html", {"checkList": checkList})


def upload(request):
    return render(request, "upload.html",)


def forms(request):
    return render(request, "forms.html",)


def gantt(request):
    return render(request, "gantt.html",)


def moe_HOME(request):
    return views_login.home(request)


def moe_investment_estimate(request):
    # 获取登陆用户对应的全部记录
    tProjectID = request.session['Project']
    tRecord = models.Investment_Estimate_Info.objects.filter(Project=tProjectID)
    tIElist = []
    for feIE in tRecord:
        tIElist.append(feIE)
    if request.method == 'GET':
        return render(request, "moe_investment_estimate.html", {'IElist': tIElist})
    if request.method == 'POST':
        tPOSTtype = request.POST.get("type", None)
        if tPOSTtype == 'upload':
            obj = request.FILES.get('fileInputed')
            if obj is None:
                return render(request, "moe_investment_estimate.html", {'IElist': tIElist})
            else:
                uploadResult = uploadIE(obj.name)
                return render(request, "moe_investment_estimate.html", {"uploadResult": uploadResult, 'IElist': tIElist})


def uploadIE(pFilePath):
    return "录入数据"

def moe_Tender_offer(request):
    return render(request, "moe_Tender_offer.html", )


def moe_Tender_offer_diff(request):
    return render(request, "moe_Tender_offer_diff.html", )


def moe_Tender_offer_diff_analysis(request):
    return render(request, "moe_Tender_offer_diff_analysis.html", )


def moe_Tender_offer_risk(request):
    return render(request, "moe_Tender_offer_risk.html", )


def moe_Controlled_price(request):
    return render(request, "moe_Controlled_price.html", )


def moe_Controlled_price_diff(request):
    return render(request, "moe_Controlled_price_diff.html", )


def moe_Controlled_price_analysis(request):
    return render(request, "moe_Controlled_price_analysis.html", )


def moe_Monthly_report_analysis(request):
    return render(request, "moe_Monthly_report_analysis.html", )


def moe_Cost_Quota(request):
    if request.method == 'POST':
        tPOSTcategoary = request.POST.get("Categoary", None)
        tPOSTbottom = request.POST.get("Bottom", None)
        tPOSTtop = request.POST.get("Top", None)
        tlist = models.Technical_Economic_Indicators.objects.filter(Project__Categoary=tPOSTcategoary).filter(Scale__gt=tPOSTbottom).filter(Scale__lt=tPOSTtop)
    return render(request, "moe_Cost_Quota.html", {'projectlist': tlist})

