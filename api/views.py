# rest_frameworkからapi_view, responseモジュールをインポート
from rest_framework.decorators import api_view
from rest_framework.response import Response
# シリアライザーとDBをインポートして、フロント側にデータを送信する準備する。
from .serializers import TodosSerializer
from .models import TodoTable

from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def api_Overview(request):
    api_urls = {
        'List': '/todo-list/',
        'Detail': '/todo-detail/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>/',
        'Delete': '/todo-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def todoList(request):
    todos = TodoTable.objects.all().order_by('-id')
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = TodoTable.objects.get(id=pk)
    serializer = TodosSerializer(todo, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def todoCreate(request):
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    todo = TodoTable.objects.get(id=pk)
    serializer = TodosSerializer(instance=todo, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = TodoTable.objects.get(id=pk)
    todo.delete()
    return Response("todo is deleted successfully")




# {
#     "id" : "4",
#     "text" : "new post",
#     "completed" : "false"
# }