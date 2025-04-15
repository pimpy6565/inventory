from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.LoginV,name='Loginv'),
    path('create',views.create,name='create'),
    path('logout',views.log_out,name='log_out'),
    path('newflav',views.newf,name='newf'),
    path('addunits',views.addunits,name="addunits"),
    path('edit',views.edit,name="edit"),
    path('editb/<int:id>',views.editb,name='editb'),
    path('del/<int:id>',views.delp,name='delp'),
    path('cat',views.cat,name='cat'),
    path('select/<str:cat>',views.select,name='select'),
    path('search',views.search,name='search')

]