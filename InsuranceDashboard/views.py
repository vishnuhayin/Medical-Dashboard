'''#'''
import itertools
from json import dumps
from django.db.models import Avg, Sum
from django.shortcuts import render
from django.http import HttpResponse

from .models import KaggleTestInsurance, KaggleTrainInsurance, KaggleRegionInsurance

# Create your views here.

def index(request):

    regional_insurance_slice = KaggleRegionInsurance.objects.all().order_by('id')[:5]

    avg_age = KaggleRegionInsurance.objects.all().aggregate(avg_age=Avg('age'))
    avg_insurance = KaggleRegionInsurance.objects.all().aggregate(avg_insurance=Avg('charges'))

    total_count = KaggleRegionInsurance.objects.all().count()
    smoker_count = KaggleRegionInsurance.objects.filter(smoker = True).count()
    male_count = KaggleRegionInsurance.objects.filter(sex = 'male').count()
    female_count = KaggleRegionInsurance.objects.filter(sex = 'female').count()
    
    holder_count = {
        'ne_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northeast' , sex = 'male').count(),
        'nw_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northwest' , sex = 'male').count(),
        'se_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southeast' , sex = 'male').count(),
        'sw_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southwest' , sex = 'male').count(),
        'ne_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northeast' , sex = 'female').count(),
        'nw_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northwest' , sex = 'female').count(),
        'se_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southeast' , sex = 'female').count(),
        'sw_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southwest' , sex = 'female').count()
    }

    ne_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northeast', sex = 'male').aggregate(ne_male_insurance_amount = Sum('charges'))
    nw_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northwest', sex = 'male').aggregate(nw_male_insurance_amount = Sum('charges'))
    se_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southeast', sex = 'male').aggregate(se_male_insurance_amount = Sum('charges'))
    sw_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southwest', sex = 'male').aggregate(sw_male_insurance_amount = Sum('charges'))

    ne_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northeast', sex = 'female').aggregate(ne_female_insurance_amount = Sum('charges'))
    nw_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northwest', sex = 'female').aggregate(nw_female_insurance_amount = Sum('charges'))
    se_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southeast', sex = 'female').aggregate(se_female_insurance_amount = Sum('charges'))
    sw_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southwest', sex = 'female').aggregate(sw_female_insurance_amount = Sum('charges'))

    dataJSON = dumps(
        ne_male_insurance_amount|nw_male_insurance_amount|se_male_insurance_amount|sw_male_insurance_amount|
        ne_female_insurance_amount|nw_female_insurance_amount|se_female_insurance_amount|sw_female_insurance_amount|
        holder_count
        )
    


    return render(
        request,"index.html",
        {
            'RegionalInsuranceSlice': regional_insurance_slice,
            'avg_age':int(avg_age['avg_age']),
            'smoker_count_per':round((smoker_count/total_count)*100,2),
            'avg_insurance':round(avg_insurance['avg_insurance'],2),
            'male_count':round(male_count/female_count,2),
            'data': dataJSON
        })

def button(request):
    return render(request, "button.html")

def typography(request):
    return render(request, "typography.html")

def element(request):
    return render(request, "element.html")

def widget(request):
    return render(request, "widget.html")

def form(request):
    return render(request, "form.html")

def table(request):

    regional_insurance_full = KaggleRegionInsurance.objects.all()

    return render(request, "table.html", {'full_data': regional_insurance_full})

def chart(request):

    holder_count = {
        'ne_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northeast' , sex = 'male').count(),
        'nw_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northwest' , sex = 'male').count(),
        'se_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southeast' , sex = 'male').count(),
        'sw_male_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southwest' , sex = 'male').count(),
        'ne_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northeast' , sex = 'female').count(),
        'nw_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'northwest' , sex = 'female').count(),
        'se_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southeast' , sex = 'female').count(),
        'sw_female_holders_count' : KaggleRegionInsurance.objects.filter(region = 'southwest' , sex = 'female').count()
    }

    ne_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northeast', sex = 'male').aggregate(ne_male_insurance_amount = Sum('charges'))
    nw_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northwest', sex = 'male').aggregate(nw_male_insurance_amount = Sum('charges'))
    se_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southeast', sex = 'male').aggregate(se_male_insurance_amount = Sum('charges'))
    sw_male_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southwest', sex = 'male').aggregate(sw_male_insurance_amount = Sum('charges'))

    ne_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northeast', sex = 'female').aggregate(ne_female_insurance_amount = Sum('charges'))
    nw_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'northwest', sex = 'female').aggregate(nw_female_insurance_amount = Sum('charges'))
    se_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southeast', sex = 'female').aggregate(se_female_insurance_amount = Sum('charges'))
    sw_female_insurance_amount = KaggleRegionInsurance.objects.filter(region = 'southwest', sex = 'female').aggregate(sw_female_insurance_amount = Sum('charges'))

    dataJSON = dumps(
        ne_male_insurance_amount|nw_male_insurance_amount|se_male_insurance_amount|sw_male_insurance_amount|
        ne_female_insurance_amount|nw_female_insurance_amount|se_female_insurance_amount|sw_female_insurance_amount|
        holder_count
        )

    return render(request, "chart.html",{'data': dataJSON})


    return render(request, "table.html")

def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request, "signup.html")

def _404(request):
    return render(request, "404.html")

def blank(request):
    return render(request, "blank.html")





def about(request):
    data = KaggleTestInsurance.objects.all()
    urban = KaggleTestInsurance.objects.filter(residence_area_type = 'Urban').values()
    rural = KaggleTestInsurance.objects.filter(residence_area_type = 'Rural').values()

    for datas in urban:
        datas['age_in_days'] = int(datas['age_in_days'])//365
        
    context = {
        'data':data,
        'urban': urban,
        'rural': rural
    }

    return render(request, "_index.html", context)
