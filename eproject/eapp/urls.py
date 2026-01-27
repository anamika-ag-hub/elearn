from django.urls import path
from . import views
from django.conf import settings 
from  django.conf.urls.static import static 
urlpatterns = [
    path('',views.login),
    path('about/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('courses/<str:cat>',views.courses,name='courses'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('new/',views.new,name='new'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('savedata /', views.savedata, name='savedata'),
    path('userdata/',views.userdata, name='userdata'),
    path('newdata/', views.newdata, name='newdata')
    
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)