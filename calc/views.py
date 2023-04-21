from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models.functions import ExtractYear
from django.db.models import F
from datetime import date
from django.contrib import messages
from calc.models import CAY
from .utils import STR, FCR, FQ, FR, FP, IWO, STRA
from profiles.models import Profile



query_set = Profile.objects.all()
N = query_set.filter(department='MCA').count()
x = float(query_set.filter(designation = 1).count())
y = float(query_set.filter(designation = 3).count())
z = float(query_set.filter(designation = 2).count())

p1 = float(query_set.filter(phd = 1).count())
p2 = float(query_set.filter(phd = 2).count())


current_year = date.today().year
r1 = Profile.objects.annotate(age=current_year - ExtractYear('yearofjoining'))
exp = list(r1.values_list('age', flat=True))

ow = float(Profile.objects.values_list('oneweek', flat=True).first())
tw = float(Profile.objects.values_list('twoweek', flat=True).first())
ow = [float(p.oneweek) for p in Profile.objects.all()]
tw = [float(p.twoweek) for p in Profile.objects.all()]

i1 = Profile.objects.values_list('interaction',flat=True)


def dashboard(request):
        a, b, c = 0, 0, 0 

        if request.method == 'POST':
            a = float(request.POST.get('1sty'))
            b = float(request.POST.get('2ndy'))
            c = float(request.POST.get('3rdy'))

        value51 = STR(a,b,c,N)
        value52 = FCR(x,y,z,N)
        value53 = FQ(p1,p2,N)
        value54 = FR(exp,N)
        value55 = FP(ow,tw,N)
        value56 = IWO(i1,N)
        total =value52[0]+value53[0]+value54[0]+value55[0]+value56[0]
        if value51 is None:
              value51 = 0
        else:
              total+=value51
        
        context ={
            'value51':value51,
            'value52':value52[0],
            'value53':value53[0],
            'value54':value54[0],
            'value55':value55[0],
            'value56':value56[0],
            'total':total,
        }
        return render(request,'dashboard.html',context)

def Avg(request):
    a, b, c = 0, 0, 0 
    my_instance = CAY.objects.first()
    year_value = None
    if my_instance:
        year_value = my_instance.year.year

    if request.method == 'POST':
        a = float(request.POST.get('1y'))
        b = float(request.POST.get('2y'))
        c = float(request.POST.get('3y'))

    ca51 = STRA(a,b,c,N)
    ca52 = FCR(x,y,z,N)
    ca53 = FQ(p1,p2,N)
    ca54 = FR(exp,N)
    ca55 = FP(ow,tw,N)
    ca56 = IWO(i1,N)
    print("Values:", ca51, ca52, ca53, ca54, ca55, ca56)
    
    
    cay_instance = CAY.objects.first()
    year_value = cay_instance.year.year if cay_instance else None
    if year_value and year_value == date.today().year:
        cay_instance.year = date.today()
        cay_instance.STR = ca51[0]
        cay_instance.FCR = ca52[1]
        cay_instance.FQ = ca53[1]
        cay_instance.FR = ca54[1]
        cay_instance.FP = ca55[1]
        cay_instance.IWO = ca56[1]
        cay_instance.save()
        messages.success(request, 'Data updated successfully.')
    else:
        cay_instance = CAY(year=date.today(), STR=ca51[0], FCR=ca52[1], FQ=ca53[1], FR=ca54[1], FP=ca55[1], IWO=ca56[1])
        cay_instance.save()
        messages.success(request, 'Data saved successfully.')
        
    context = {
        'ca51': ca51,
        'ca52': ca52,
        'ca53': ca53,
        'ca54': ca54,
        'ca55': ca55,
        'ca56': ca56,
    }
    
    return render(request, 'avgcay.html',context)