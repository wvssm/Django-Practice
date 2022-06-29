from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#작성한 뷰를 호출하기 위해서 url 코드를 작성, 그 후 뷰와 연결