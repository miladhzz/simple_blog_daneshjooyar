from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="index"),
    path('<str:tag_slug>/', views.post_list, name="index_tag"),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/', views.post_detail, name="post_detail"),
    path('contact-us/', views.contact_us, name="contact_us")
]
