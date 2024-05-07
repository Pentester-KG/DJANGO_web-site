from django.urls import path
from .views import info_view, hobby_view, current_time_view


urlpatterns = [
    path('info/', info_view, name="info"),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', current_time_view, name='time')
]