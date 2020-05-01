from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locales import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresasViewSet)
router.register(r'clasificacionEmpresas', views.ClasificacionesEmpresasViewSet)
router.register(r'medidasSanitarias', views.MedidasSanitariasViewSet)
router.register(r'profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]