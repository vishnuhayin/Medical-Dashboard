'''urls and paths'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('button', views.button, name='button'),
    path('typography', views.typography, name='typography'),
    path('element', views.element, name='element'),
    path('widget', views.widget, name='widget'),
    path('form', views.form, name='form'),
    path('table', views.table, name='table'),
    path('chart', views.chart, name='chart'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('_404', views._404, name='_404'),
    path('blank', views.blank, name='blank'),


    path('_index', views.about, name='_index')
]