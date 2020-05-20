from django.urls import path
from . import views

app_name = 'cwPoll'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:poll_id>/', views.detail, name = 'detail'),
    path('<int:poll_id>/result/', views.result, name = 'result'),
    path('<int:poll_id>/vote/', views.vote, name = 'vote'),
]