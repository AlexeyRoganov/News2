from django.urls import path
from .views import PostsList, PostsList2


urlpatterns = [path('', PostsList.as_view()), path('search', PostsList2.as_view())]


