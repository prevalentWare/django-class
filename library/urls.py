from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, CategoryViewSet
from .views import register, login

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('', include(router.urls)),
]