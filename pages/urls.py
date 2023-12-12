# pages/urls.py
from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  #При использовании Views на основе класса мы всегда добавляем as_view() в
                                                    #конце имени view.
]