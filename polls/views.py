from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from polls.models import Person
from .serializers import PersonListSerializer, PersonDetailSerializer,PersonUpdateSerializer,PersonCreateSerializer,RegistrationSerializer
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner



class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name',]
    permission_classes = [AllowAny]

class PersonDetailView(RetrieveAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'
	permission_classes = [IsAuthenticated] 

class PersonUpdateView(RetrieveUpdateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'

class PersonDeleteView(DestroyAPIView):
	queryset = Person.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'
	permission_classes = [IsOwner]

class PersonCreateView(CreateAPIView):
    serializer_class = PersonCreateSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Registration(CreateAPIView):
	serializer_class = RegistrationSerializer



