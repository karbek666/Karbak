from django.http import HttpResponse
from django.shortcuts import render
from .models import MyModel
# Create your views here.
def index(request):
    user = MyModel.objects.all()
    return render(request, 'newhtml.html',{"users":user})

def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName', 'Hello this is your Cookies', max_age = None)
    return html

def showcookie(request):
    show = request.COOKIES.get('CookieName')
    if show:
        html = "Hello! {0}".format(show)
    else:
        html = "Cookie 'cookieName' is not set."
    return HttpResponse(html)

def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html
def deletercooike(request):
    html = HttpResponse('<h1>Cookie Deleter</h1>')
    html.delete_cookie('visit_count')
    return html