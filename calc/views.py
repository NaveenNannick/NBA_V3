from django.shortcuts import render,redirect
from django.db.models.functions import ExtractYear
from django.db.models import F
from datetime import date
from .utils import STR, FCR, FQ, FR, FP, IWO
from profiles.models import Profile



query_set = Profile.objects.all()
N = query_set.filter(department='MCA').count()


def dashboard(request):
        a, b, c = 0, 0, 0 

        if request.method == 'POST':
            a = float(request.POST.get('1sty'))
            b = float(request.POST.get('2ndy'))
            c = float(request.POST.get('3rdy'))
        
        
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



        value51 = STR(a,b,c,N)
        value52 = FCR(x,y,z,N)
        value53 = FQ(p1,p2,N)
        value54 = FR(exp,N)
        value55 = FP(ow,tw,N)
        value56 = IWO(i1,N)
        context ={
            'value51':value51,
            'value52':value52,
            'value53':value53,
            'value54':value54,
            'value55':value55,
            'value56':value56,
        }
        return render(request,'dashboard.html',context)
