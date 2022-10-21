from django.shortcuts import render
def index(request):
    return render(request, 'mainpage/main.html')
def contacts(request):
    return render(request, 'mainpage/contacts.html')
def internet_addiction(request):
    return render(request, 'mainpage/internet_addiction.html')
def administration(request):
    return render(request, 'mainpage/administration.html')
def stop_buling(request):
    return render(request, 'mainpage/stop_buling.html')
def s_e_e(requst):
    return render(requst, 'mainpage/s.e.e.html')
def corisni_posilanya(request):
    return render(request, 'mainpage/corisni_posilanya.html')
def rozdil1_statut(requst):
    return render(requst, "mainpage/rozdil1_statut.html")
def strategiarozvitku(request):
    return render(request, 'mainpage/strategiarozvitku.html')
def programs_yaki_rel_v_zakladi(request):
    return render(request, 'mainpage/programs_yaki_rel_v_zakladi.html')
def teacherslist(request):
    return render(request, 'mainpage/rozdil2_kadroviysklad.html')
# Create your views here.
