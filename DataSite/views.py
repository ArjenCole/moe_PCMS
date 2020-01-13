from django.shortcuts import render
from django.shortcuts import HttpResponse
from DataSite import views_login
from DataSite import views_check
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
    return render(request, "moe_HOME.html", )


def moe_investment_estimate(request):
    return render(request, "moe_investment_estimate.html", )


def moe_Tender_offer(request):
    return render(request, "moe_Tender_offer.html", )


def moe_Tender_offer_diff(request):
    return render(request, "moe_Tender_offer_diff.html", )


def moe_Tender_offer_diff_analysis(request):
    return render(request, "moe_Tender_offer_diff_analysis.html", )


def moe_Tender_offer_risk(request):
    return render(request, "moe_Tender_offer_risk.html", )