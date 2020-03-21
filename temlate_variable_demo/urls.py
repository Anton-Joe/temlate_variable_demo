"""temlate_variable_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

class Person(object):
    def __init__(self, name):
        self.person_name = name


def index(request):
    # 第一种  {{ name }}
    context1 = {
        'name': '叶敬轩'
    }
    # 第二种 {{ person.name }}
    context2 = {
        'person': {
            'name': '第二种叶敬轩'
        }
    }
    # 第三种  {{ person.person_name }}
    p = Person('类中的叶敬轩')
    context3 = {
        'person': p
    }
    # 第四种  {{ school.1 }}
    context4 = {
        'school':[
            '西南大学',
            '清华大学'
        ],
        'age': 17,
        'heros':[
            '鲁班二号',
            '程咬金'
        ]
    }
    return render(request, 'index.html', context=context4)


urlpatterns = [
    path('', index),
]
