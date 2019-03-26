from rest_framework import serializers
from polls.models import Person
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ["username","password"]

	def create(self, validated_data):
		username = validated_data["username"]
		password = validated_data["password"]
		user = User(username=username)
		user.set_password(password)
		user.save()
		return validated_data


class UserSerializer(serializers.ModelSerializer):
	number_of_persons=serializers.SerializerMethodField()

	class Meta:
		model = User
		fields =["username","email","number_of_persons"]

	def get_number_of_persons(self,obj):
		return Person.objects.filter(owner=obj).count() 


class PersonListSerializer(serializers.ModelSerializer):
	person_details = serializers.HyperlinkedIdentityField(
		view_name="api-detail",
		lookup_field="id",
		lookup_url_kwarg="person_id")
	class Meta:
		model = Person
		fields = ['first_name','last_name','person_details']

class PersonDetailSerializer(serializers.ModelSerializer):
	owner = UserSerializer()    
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
