from django.http import HttpResponse

def fb(request):
    return HttpResponse('<h1>Lets connect with friends</h1>')