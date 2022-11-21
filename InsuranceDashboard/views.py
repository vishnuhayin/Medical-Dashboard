'''#'''
import itertools
from json import dumps
from django.db.models import Avg, Sum, Min, Max
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

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

    min_age = KaggleRegionInsurance.objects.all().aggregate(min_age=Min('age'))
    max_age = KaggleRegionInsurance.objects.all().aggregate(max_age=Max('age'))
    age = [number for number in range(min_age['min_age'], max_age['max_age'] + 1)]
    avg_bmi = []
    avg_bmi_male = []
    avg_bmi_female = []
    avg_amount = []
    avg_amount_male = []
    avg_amount_female = []

    for item in age:
        avg_bmi_item = KaggleRegionInsurance.objects.filter(age = item).aggregate(avg_bmi = Avg('bmi'))
        avg_bmi_male_item = KaggleRegionInsurance.objects.filter(age = item, sex = 'male').aggregate(avg_bmi_male = Avg('bmi'))
        avg_bmi_female_item = KaggleRegionInsurance.objects.filter(age = item, sex = 'female').aggregate(avg_bmi_female = Avg('bmi'))
        avg_amount_item = KaggleRegionInsurance.objects.filter(age = item).aggregate(avg_amount = Avg('charges'))
        avg_amount_male_item = KaggleRegionInsurance.objects.filter(age = item, sex = 'male').aggregate(avg_amount_male = Avg('charges'))
        avg_amount_female_item = KaggleRegionInsurance.objects.filter(age = item, sex = 'female').aggregate(avg_amount_female = Avg('charges'))        
        
        avg_bmi.append(avg_bmi_item['avg_bmi'])
        avg_bmi_male.append(avg_bmi_male_item['avg_bmi_male'])
        avg_bmi_female.append(avg_bmi_female_item['avg_bmi_female'])
        avg_amount.append(avg_amount_item['avg_amount'])
        avg_amount_male.append(avg_amount_male_item['avg_amount_male'])
        avg_amount_female.append(avg_amount_female_item['avg_amount_female'])

    smoker_count = {
        'smoking_under_20' : KaggleRegionInsurance.objects.filter(age__lt = 20).count(),
        'smoking_20_30' : KaggleRegionInsurance.objects.filter(age__gt = 20, age__lt = 30).count(),
        'smoking_30_40' : KaggleRegionInsurance.objects.filter(age__gt = 30, age__lt = 40).count(),
        'smoking_40_50' : KaggleRegionInsurance.objects.filter(age__gt = 40, age__lt = 50).count(),
        'smoking_above_50' : KaggleRegionInsurance.objects.filter(age__gt = 50).count()
    }

    smoker_region_wise_count = {
        'smoking_ne' : KaggleRegionInsurance.objects.filter(region = 'northeast').count(),
        'smoking_nw' : KaggleRegionInsurance.objects.filter(region = 'northwest').count(),
        'smoking_se' : KaggleRegionInsurance.objects.filter(region = 'southeast').count(),
        'smoking_sw' : KaggleRegionInsurance.objects.filter(region = 'southwest').count()
    }

    dataJSON = dumps(
        ne_male_insurance_amount|nw_male_insurance_amount|se_male_insurance_amount|sw_male_insurance_amount|
        ne_female_insurance_amount|nw_female_insurance_amount|se_female_insurance_amount|sw_female_insurance_amount|
        holder_count|smoker_count|smoker_region_wise_count
        )
    
    ageJSON = dumps(age)
    avg_bmiJSON = dumps(avg_bmi)
    avg_bmi_maleJSON = dumps(avg_bmi_male)
    avg_bmi_femaleJSON = dumps(avg_bmi_female)
    avg_amountJSON = dumps(avg_amount)
    avg_amount_maleJSON = dumps(avg_amount_male)
    avg_amount_femaleJSON = dumps(avg_amount_female)

    return render(request, "chart.html",{'data': dataJSON,'age':ageJSON,'avg_bmi':avg_bmiJSON,
                                        'avg_bmi_male':avg_bmi_maleJSON,'avg_bmi_female':avg_bmi_femaleJSON,
                                        'avg_amount':avg_amountJSON,'avg_amount_male':avg_amount_maleJSON,'avg_amount_female':avg_amount_femaleJSON
                                        })


    return render(request, "table.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/insurance")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("/signin.html")
    else:
        return render(request, "signin.html")

def signout(request):
    auth.logout(request)
    return redirect('../')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # is_staff = request.POST['is_staff']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "username taken")
                return redirect('/insurance/signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email taken")
                return redirect('/insurance/signup')
            else:
                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, password = password1, email = email)
                user.save()
                print("User Created")
                return redirect('/insurance/signin')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('/insurance/signup')
    else:
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
