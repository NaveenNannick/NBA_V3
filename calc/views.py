from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.db.models.functions import ExtractYear
from django.db.models import F
from datetime import date
from django.utils import timezone
from django.contrib import messages
from calc.models import CAY
from .utils import STR, FCR, FQ, FR, FP, IWO
from profiles.models import Profile
from django.http import HttpResponse
import csv




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

oneweek_values = Profile.objects.values_list('oneweek', flat=True)
if not oneweek_values:
    ow = 0.0  # or whatever default value you want to use
else:
    ow = float(oneweek_values.first())

twoweek_values = Profile.objects.values_list('twoweek', flat=True)
if not twoweek_values:
    tw = 0.0  # or whatever default value you want to use
else:
    tw = float(twoweek_values.first())
ow = [float(p.oneweek) for p in Profile.objects.all()]
tw = [float(p.twoweek) for p in Profile.objects.all()]

i1 = Profile.objects.values_list('interaction',flat=True)

current_year1 = timezone.now().year
one_year_ago = current_year1 - 1
two_years_ago = current_year1 - 2

cay_queryset0 = CAY.objects.filter(year__year=current_year1)
cay_queryset1 = CAY.objects.filter(year__year=one_year_ago)
cay_queryset2 = CAY.objects.filter(year__year=two_years_ago)

cl0 = list(cay_queryset0.values_list('STR', 'FCR', 'FQ', 'FR', 'FP', 'IWO'))
cl1 = list(cay_queryset1.values_list('STR', 'FCR', 'FQ', 'FR', 'FP', 'IWO'))
cl2 = list(cay_queryset2.values_list('STR', 'FCR', 'FQ', 'FR', 'FP', 'IWO'))



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
        try:
            value52 = round(((value52+cl1[0][1]+cl2[0][1])/3),2)
        except IndexError:
            value52 = 0
        try:
            value53 = round(((value53+cl1[0][2]+cl2[0][2])/3),2)
        except IndexError:
            value53 = 0
        try:
            value54 = round(((value54+cl1[0][3]+cl2[0][3])/3),2)
        except IndexError:
            value54 = 0
        try:
            value55 = round(((value55+cl1[0][4]+cl2[0][4])/3),2)
        except IndexError:
            value55 = 0
        try:
            value56 = round(((value56+cl1[0][5]+cl2[0][5])/3),2)
        except IndexError:
            value56 = 0



        total =value52+value53+value54+value55+value56
        if value51 is None:
              value51 = 0
        else:
              value51 =round(((value51+cl1[0][0]+cl2[0][0])/3),2)
              total+=value51
        total = round(total,2)
        context ={
            'value51':value51,
            'value52':value52,
            'value53':value53,
            'value54':value54,
            'value55':value55,
            'value56':value56,
            'total':total,
        }
        return render(request,'dashboard.html',context)


def Avg(request):
    a, b, c = 0, 0, 0 
    cay_data = CAY.objects.all()
    my_instance = CAY.objects.first()
    year_value = None
    if my_instance:
        year_value = my_instance.year.year

    if request.method == 'POST':
        a = float(request.POST.get('1y'))
        b = float(request.POST.get('2y'))
        c = float(request.POST.get('3y'))

        ca51 = STR(a,b,c,N)
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
            cay_instance.STR = ca51
            cay_instance.FCR = ca52
            cay_instance.FQ = ca53
            cay_instance.FR = ca54
            cay_instance.FP = ca55
            cay_instance.IWO = ca56
            cay_instance.save()
            messages.success(request, 'Data updated successfully.')
        else:
            cay_instance = CAY(year=date.today(), STR=ca51, FCR=ca52[0], FQ=ca53[0], FR=ca54[0], FP=ca55[0], IWO=ca56[0])
            cay_instance.save()
            messages.success(request, 'Data saved successfully.')
        
        return redirect('avg')
    
    context = {
        'ca51': a,
        'ca52': b,
        'ca53': c,
    }
    
    
    return render(request, 'avgcay.html',{'cay_data': cay_data})

def export_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cay_data.csv"'
    writer = csv.writer(response)

    writer.writerow(['Year', 'STR', 'FCR', 'FQ', 'FR', 'FP', 'IWO'])

    for cay in CAY.objects.all():
        writer.writerow([
            cay.year_value,
            cay.STR,
            cay.FCR,
            cay.FQ,
            cay.FR,
            cay.FP,
            cay.IWO,
        ])

    return response