from rest_framework import serializers
from api.models import Company
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model=Company
        fields="__all__"