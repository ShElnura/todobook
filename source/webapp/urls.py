from django.urls import path

from webapp.views import IndexView, BookAddView, BookView, BookDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('book/<int:pk>/', BookView.as_view(), name='view'),
    path('book/add/', BookAddView.as_view(), name='create'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
]
