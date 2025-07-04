from django.shortcuts import render
from .serializers import SubjectSerizlizer , CourseSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView , UpdateAPIView
from .models import Subject , Course
from rest_framework import permissions
from .persmissions import IsOwnerOrReadOnly , IsUsernameJohn , IsPremiumUserAndPremiumCourse , IsYearEven , IsUserSuperUser , OnlyPutAndPatch



class SubjectListAPIView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerizlizer

class IsPremiumAPIView(ListAPIView):
    queryset = Course.objects.filter(is_premium=True)
    serializer_class = CourseSerializer
    permission_classes = [IsPremiumUserAndPremiumCourse , permissions.IsAuthenticated]

class SubjetAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerizlizer
    permission_classes = [permissions.IsAuthenticated , OnlyPutAndPatch]


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrReadOnly , permissions.IsAuthenticated , IsYearEven , IsUserSuperUser ]

class CourseUpdateAPIView(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [OnlyPutAndPatch]
