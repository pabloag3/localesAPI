from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from locales import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresasViewSet)
router.register(r'clasificacionEmpresas', views.ClasificacionesEmpresasViewSet)
router.register(r'medidasSanitarias', views.MedidasSanitariasViewSet)
router.register(r'profile', views.UserProfileViewSet)
router.register(r'empresaMedidas', views.EmpresasMedidasViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]