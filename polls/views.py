from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView,CreateAPIView
from polls.models import Person
from .serializers import PersonListSerializer, PersonDetailSerializer,PersonUpdateSerializer,PersonCreateSerializer
from rest_framework.filters import SearchFilter,OrderingFilter


class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name','last_name',]

class PersonDetailView(RetrieveAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'

class PersonUpdateView(RetrieveUpdateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'

class PersonDeleteView(DestroyAPIView):
	queryset = Person.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'person_id'

class PersonCreateView(CreateAPIView):
    serializer_class = PersonCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



