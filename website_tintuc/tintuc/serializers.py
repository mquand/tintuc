from rest_framework import serializers
from .models import * 

class TacGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacGia
        fields = '__all__'  # Hoặc các trường cụ thể mà bạn muốn
class ChuyenMucSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChuyenMuc
        fields = '__all__'  