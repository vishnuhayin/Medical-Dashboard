from django.shortcuts import render
import requests, json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"X-RapidAPI-Key": "63b1248df0msh530c720cf43fba4p16311fjsn0f3e08c990d4",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def CovidIndex(request):
    no_of_results = response['results']
    country_list = []
    for item in range(no_of_results):
        country_list.append(response['response'][item]['country'])
    
    country_list.sort()

    if request.method == "POST":
        selected_country = request.POST['selected_country']
        for item in range(no_of_results):
            if selected_country == response['response'][item]['country']:
                new = response['response'][item]['cases']['new']
                active = response['response'][item]['cases']['active']
                critical = response['response'][item]['cases']['critical']
                recovered = response['response'][item]['cases']['recovered']
                deaths = response['response'][item]['deaths']['total']
                total = response['response'][item]['cases']['total']

        context = {
            'new': new, 'deaths':deaths, 'active':active,
            'critical':critical, 'recovered':recovered,'total':total,
            'selected_country':selected_country, 'country_list':country_list
        }
        print(context)
        return render(request, "CovidIndex.html", context)

    # context = {'response':response['response']}
    return render(request, "CovidIndex.html", {'country_list':country_list})