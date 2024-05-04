from django.urls import path
from app2.views import dashboard,products, profileadd, profile_list, profile_view

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('products/',products,name='products'),
    path('profileadd/',profileadd,name='profileadd'),
    path('profilelist/',profile_list,name='profile_list'),
    path('profileview/<int:profile_id>/view/',profile_view,name='profile_view')

]
