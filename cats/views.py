#from rest_framework.views import APIView
#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from rest_framework import generics

from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


# 1 вариант
#@api_view(['GET', 'POST'])
#def cat_list(request):
    # Обработчик для POST-запросов.
    #if request.method == 'POST':
        # Создаём объект сериализатора 
        # и передаём в него данные из POST-запроса
        #serializer = CatSerializer(data=request.data)
        # Если полученные данные валидны —
        # сохраняем данные в базу через save().
        #if serializer.is_valid():
            #serializer.save()
            # Возвращаем JSON со всеми данными нового объекта
            # и статус-код 201
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Если данные не прошли валидацию — 
        # возвращаем информацию об ошибках и соответствующий статус-код:
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #cats = Cat.objects.all()
    #serializer = CatSerializer(cats, many=True)
    #return Response(serializer.data)


# 2 ваариант
#class APICat(APIView):
    #def get(self, request):
        #cats = Cat.objects.all()
        #serializer = CatSerializer(cats, many=True)
        #return Response(serializer.data)

    #def post(self, request):
        #serializer = CatSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3 вариант Дженерики
#class CatList(generics.ListCreateAPIView):
    #queryset = Cat.objects.all()
    #serializer_class = CatSerializer


#class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Cat.objects.all()
    #serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
