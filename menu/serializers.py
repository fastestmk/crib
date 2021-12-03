from .models import MenuItem
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        extra_kwargs = {
        	# 'category': {'required': True, 'allow_blank': False},
			'name': {'required': True, 'allow_blank': False},
        	'price': {'required': True}
        }
        exclude = ('active', 'created', 'modified',)
