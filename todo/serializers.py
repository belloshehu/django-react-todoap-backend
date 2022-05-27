from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    """ Create serialized instances of Todo model."""
    class Meta:
        model = Todo
        fields = '__all__'