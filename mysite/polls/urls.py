"""
创建URL映射polls,URLconf
"""
from django.urls import path
from . import views

"""
    path()参数
    第一个route:匹配url
    第二个view:匹配函数
    第三个kwargs:传递参数(此处没用到)
    第四个name:为URL取名可以在Django中任意地方唯一引用它
"""
urlpatterns = [ 
    path('', views.index, name='index'),
]
