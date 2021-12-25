from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title":"Imronsyabani",
        "biodata":[
            {
                "nama":"imronsyabani",
                "umur":"19"
            }
        ]
    }
    return render(request,'index.html',context)