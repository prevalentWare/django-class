from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewset, IngresoViewset, GastoViewset
from .views import register, login

router = DefaultRouter()
router.register(r'categorias', CategoriaViewset)
router.register(r'ingresos', IngresoViewset)
router.register(r'gastos', GastoViewset)


urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('', include(router.urls)),
]