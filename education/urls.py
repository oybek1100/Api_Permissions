from django.urls import path
from .views import SubjetAPIView, SubjectListAPIView , CourseListAPIView , CourseAPIView , IsPremiumAPIView , CourseUpdateAPIView

urlpatterns = [
    path('subjects/', SubjectListAPIView.as_view()),
    path('subjects/<int:pk>/', SubjetAPIView.as_view()),
    path('courses/', CourseListAPIView.as_view()),
    path('courses/<int:pk>/', CourseAPIView.as_view()),
    path('premium/', IsPremiumAPIView.as_view()),
    path('courses/<int:pk>/update/', CourseUpdateAPIView.as_view())
]