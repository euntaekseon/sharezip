from django.shortcuts import render, get_object_or_404
from hosting.models import Room
import os
from django.db.models import Q

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL= '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Create your views here.
def home(request):
    return render(request,'home.html')

def base (request):
    return render(request,'base.html')

def findroom (request):
    rooms=Room.objects.all()
  
    return render(request, 'findroom.html',{'rooms':rooms,'media_root': MEDIA_ROOT, 'media_url': MEDIA_URL})

def result(request):
    return render(request,'home.html')

def detail(request, room_id):
    room=get_object_or_404(Room,pk=room_id)
    options = request.POST.getlist('options', False)
    
    return render(request,'detail.html',{'room':room})


def filter(request):
    rtype = request.GET['condition']
    start = request.GET['start']
    end = request.GET['end']
    gu = request.GET['gu']
    dong = request.GET.get('dong','all')
    rtype = request.GET['condition']
    period = request.GET['rent']
    gender = request.GET['gender']
    btype = request.GET['type']
    cost = request.GET['cost']
    deposit = request.GET['deposit']
    
    # 성별, 타입이 일치하고 가격이 cost보다 이하인 방들
    _q1 = Q(gender__exact = gender)
    _q2 = Q(building_type__exact = btype)
    _q3 = Q(cost__lte = cost)
    _q4 = Q(deposit__lte = deposit)
    _q5 = Q(start_date__lte = start)
    _q5 = Q(end_date__gte = end)
    _q6 = Q(period__exact = period)

    if(gu == "서울시 전체"):
        #filtered_rooms = Room.objects.filter(_q1 and _q2 and _q3 and _q4 and _q5 and _q6)
        filtered_rooms = Room.objects.filter(rent_type = rtype).filter(gender = gender).filter(cost__lte = cost).filter(deposit__lte = deposit).filter(start_date__lte = start).filter(end_date__lte = end).filter(period = period)
    # dong = all 이면 같은 구 
    elif(dong == "전체"):
        _q7 = Q(addr_gu__exact = gu)
        #filtered_rooms = Room.objects.filter(_q1 and _q2 and _q3 and _q4 and _q5 and _q6 and _q7)
        filtered_rooms = Room.objects.filter(rent_type = rtype).filter(addr_gu = gu).filter(gender = gender).filter(cost__lte = cost).filter(deposit__lte = deposit).filter(start_date__lte = start).filter(end_date__lte = end).filter(period = period)
    # dont != all 이면 같은 동
    else:
        _q7 = Q(addr_dong__exact = dong)
        #filtered_rooms = Room.objects.filter(_q1 and _q2 and _q3 and _q4 and _q5 and _q6 and _q7)
        filtered_rooms = Room.objects.filter(rent_type = rtype).filter(addr_dong = dong).filter(addr_gu = gu).filter(gender = gender).filter(cost__lte = cost).filter(deposit__lte = deposit).filter(start_date__lte = start).filter(end_date__lte = end).filter(period = period)

    if(btype != 0):
        filtered_rooms = filtered_rooms.filter(building_type = btype)

    return render(request, 'result.html', {'filtered_rooms':filtered_rooms, 'gender':gender, 'gu':gu, 'dong':dong, 'cost':cost, 'start':start, 'end':end})
    
def myrooms(request, username):
    myrooms = Room.objects.filter(creator__exact = username)
    return render(request, 'myrooms.html', {'myrooms':myrooms})
