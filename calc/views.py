from django.shortcuts import render,redirect
from .utils import STR, FCR, FQ
from profiles.models import Profile



query_set = Profile.objects.all()
N = query_set.filter(department='MCA').count()
"""
def STR(request):
    query_set = Profile.objects.all()
    N = query_set.filter(department='MCA').count()

    if request.method == 'POST':
       
        sfr = (a + b + c) / N
        assest1 = 20 * (20/sfr)
        return render(request, 'dashboard.html', {'assest1': assest1})
    else:
        return render(request, 'dashboard.html')

def FCR(request):
    query_set = Profile.objects.all()
    N = query_set.filter(department='MCA').count()
    if request.method == 'POST':
       
        cri = (2.25*((2*x)+y+(0.5)*z)) / N
        assest2 = 20*cri
        return render(request, 'dashboard.html', {'assest2': assest2})
    else:
        return render(request, 'dashboard.html')
"""
def dashboard(request):

        a = float(request.POST.get('1sty'))
        b = float(request.POST.get('2ndy'))
        c = float(request.POST.get('3rdy'))

        x = float(query_set.filter(designation = 1).count())
        y = float(query_set.filter(designation = 3).count())
        z = float(query_set.filter(designation = 2).count())

        p1 = float(query_set.filter(phd = 1).count())
        p2 = float(query_set.filter(phd = 2).count())

        value51 = STR(a,b,c,N)
        value52 = FCR(x,y,z,N)
        value53 = FQ(p1,p2,N)
        context ={
            'value51':value51,
            'value52':value52,
            'value53':value53,
        }
        return render(request,'dashboard.html',context)


    
