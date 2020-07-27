from django.shortcuts import render

# Create your views here.
def home_view(request,api, *args, **kwargs): # *args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    current  = api
    
    return render(request, "index.html", {})