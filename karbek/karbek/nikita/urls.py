from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('cookie/', views.set_cookie),
    path('cookie2/', views.deletercooike)
]
