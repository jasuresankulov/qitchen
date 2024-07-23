from rest_framework import serializers
from .models import MenuItem
# from .models import Book, BookImage

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['url','name', 'description', 'price', 'available']


