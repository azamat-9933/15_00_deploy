from django.urls import path
from clinics.views import *

urlpatterns = [
    path('actions/', ActionListView.as_view()),
    path('online-appointments/', OnlineAppointmentCreateAPIView.as_view()),
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('specialists/', SpecialistListAPIView.as_view(), name='specialists-list'),
    path('contact-chief-doctor/', ContactChiefDoctorCreateAPIView.as_view(), name='contact-chief-doctor'),
    path('feedbacks/', FeedbackCreateListAPIView.as_view(), name='feedback'),
    path('about-us/', AboutUsAPIView.as_view(), name='about-us'),
    path('photogallery-categories/', PhotoGalleryCategoryListAPIView.as_view(), name='photogallery-categories'),
    path('photogalleries/', PhotoGalleryListAPIView.as_view(), name='photogalleries'),
    path('licenses/', LicenseListAPIView.as_view(), name='licenses'),
    path('specialists/<int:pk>/', SpecialistDetailAPIView.as_view(), name='specialist-detail'),
    path('news-categories/', NewsCategoryListAPIView.as_view(), name='news-categories'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-list'),
    path('vacancies/', VacancyListAPIView.as_view(), name='vacancies-list'),
    path('contacts/', ContactAPIView.as_view(), name='contacts'),
    path('story-categories/', StoryCategoriesListAPIView.as_view(), name='story-categories-detail'),
    path('home-slider/', HomeSliderListView.as_view(), name='home-slider')
]