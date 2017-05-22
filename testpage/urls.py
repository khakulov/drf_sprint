from django.conf.urls import url
from django.views.decorators.cache import cache_control

from .views import ListAnimals

cached = cache_control(private=True, maxage=5 * 60 * 1)

urlpatterns = [
    url(r'^animals/$',
        ListAnimals.as_view(), name="list_animals"),
]