"""
创建URL映射polls,URLconf
"""
from os import name
from django.urls import path
from . import views

"""
    path()参数
    第一个route:匹配url
    第二个view:匹配函数
    第三个kwargs:传递参数(此处没用到)
    第四个name:为URL取名可以在Django中任意地方唯一引用它
"""
app_name = 'polls'
urlpatterns = [ 
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/<question_id>/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
