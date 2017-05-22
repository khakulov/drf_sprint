from django.conf.urls import url
from django.views.decorators.cache import cache_control
from rest_framework.schemas import get_schema_view

from .views import ListAnimals

schema_view = get_schema_view(title='Animals API')

cached = cache_control(private=True, maxage=5 * 60 * 1)

urlpatterns = [
    url('^$', schema_view),
    url(r'^animals/$',
        ListAnimals.as_view(), name="list_animals"),
]