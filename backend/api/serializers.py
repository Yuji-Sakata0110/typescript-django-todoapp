from rest_framework import serializers
from .models import TodoTable

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTable
        fields = '__all__'