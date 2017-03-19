from django.conf.urls import url 
from cpccs import views 
 
 
urlpatterns = [ 
    url(r'^sectors/$',  
        views.SectorList.as_view(),  
        name=views.SectorList.name), 
    url(r'^usuarios/$',  
        views.UsuarioList.as_view(),  
        name=views.UsuarioList.name), 
    url(r'^$', 
        views.ApiRoot.as_view(), 
        name=views.ApiRoot.name), 
] 