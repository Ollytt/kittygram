from django.urls import include, path

from rest_framework.routers import SimpleRouter

#from cats.views import APICat
#from cats.views import CatList, CatDetail
from cats.views import CatViewSet

#from cats.views import cat_list

#urlpatterns = [
   #path('cats/', cat_list, name='cat_list'),
#]

#urlpatterns = [
    #path('cats/', APICat.as_view()),
#]

#urlpatterns = [
    #path('cats/', CatList.as_view()),
    #path('cats/<int:pk>/', CatDetail.as_view()),
#]

# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]
