from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^api/countries$',views.countries_list), #r tells django raw regular pattern
    url(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_detail)
]

#the next step is to point the root URLconf at the countries.urls module.