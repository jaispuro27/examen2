from rest_framework import serializers
from ToDoS.models import Pending

class PendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = '__all__'

class PendingIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id']

class PendingIDTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'title']

class PendingUnresolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'title','is_resolved']

class PendingResolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'title','is_resolved']

class PendingIDUserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'user_id']
        
class PendingResolvedIDUserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'user_id']
        
class PendingUnresolvedIDUserIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = ['id', 'user_id']