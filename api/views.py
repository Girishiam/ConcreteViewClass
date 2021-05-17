from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
#list and create


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
