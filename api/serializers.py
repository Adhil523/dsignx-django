from rest_framework.serializers import ModelSerializer
from .models import userLogin,Entries

class userSerializer(ModelSerializer):
    class Meta:
        model=userLogin
        fields='__all__'

class entrySerializer(ModelSerializer):
    class Meta:
        model=Entries
        fields='__all__'
