from rest_framework import serializers
from polls.models import Person

class PersonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        exclude = ["owner"]
