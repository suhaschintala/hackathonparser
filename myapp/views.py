from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myview(request):
    from bs4 import BeautifulSoup
    import requests
    req = requests.get("https://www.msn.com/en-in/entertainment/bollywood/yay-he-called-me-a-film-star-abhishek-bachchans-reaction-to-trolls-is-sarcasm-goals-no/ar-BBL1peZ?ocid=spartandhp")
    text = req.text
    soup = BeautifulSoup(text)
    finalstring = ""
    for data in soup.find_all('p'):
        finalstring += data.text
    return HttpResponse(finalstring)
