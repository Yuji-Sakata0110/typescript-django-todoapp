# rest_frameworkからapi_view, responseモジュールをインポート
from rest_framework.decorators import api_view
from rest_framework.response import Response
# シリアライザーとDBをインポートして、フロント側にデータを送信する準備する。
from .serializers import TodosSerializer
from .models import TodoTable
# from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.shortcuts import render

# todo home
class IndexView(TemplateView):
    template_name = 'index.html'

    def getTodoList(request):
        todos = TodoTable.objects.all().order_by('-id')
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data)

# requierd login
# @login_required
@api_view(['GET'])
def api_Overview(request):
    api_urls = {
        'List': '/todo_list/',
        'Detail': '/todo_detail/',
        'Create': '/todo_create/',
        'Update': '/todo_update/<str:pk>/',
        'Delete': '/todo_delete/<str:pk>/',
    }
    return Response(api_urls)


# @login_required
@api_view(['GET'])
def todoList(request):
    todos = TodoTable.objects.all().order_by('-id')
    serializer = TodosSerializer(todos, many=True)
    return Response(serializer.data)


# @login_required
@api_view(['GET'])
def todoDetail(request, pk):
    todo = TodoTable.objects.get(id=pk)
    serializer = TodosSerializer(todo, many=False)
    return Response(serializer.data)


# @login_required
@api_view(["POST"])
def todoCreate(request):
    serializer = TodosSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


# @login_required
@api_view(['POST'])
def todoUpdate(request, pk):
    todo = TodoTable.objects.get(id=pk)
    serializer = TodosSerializer(instance=todo, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


# @login_required
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