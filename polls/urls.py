from django.urls import path
from . import views, fun


urlpatterns = [
    path('', views.index, name ='index'),
    path('fun/', fun.index, name = 'fun'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<in:question_id>/vote/', views.vote, name='vote')
]