from django.urls import path
from testapp.views import IndexView, UpdateView, AddView, search
urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('update/<int:pk>/', UpdateView.as_view(), name="update"),
    path('create/', AddView.as_view(), name="create"),
    path('search/', search, name="search")
    
]
