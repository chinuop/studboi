from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now=datetime.datetime.now()
    return render(request,"studboi/index.html",{
       "pranav" :now.month==11 and now.day==18 ,
       "vaibh" :now.month==11 and now.day==21,
       "chinmay":now.month==3 and now.day==6,
       "sanket":now.month==6 and now.day==3,
       "bhavesh": now.month==3 and now.day==17,
       "lavate": now.month==7 and now.day==23,
       "chetan":now.month==5 and now.day==21
    })
