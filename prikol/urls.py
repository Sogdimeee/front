from django.contrib import admin
from django.urls import path
from users.views import RegisterView, TokenView, CheckAuthView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/check-auth/', CheckAuthView.as_view(), name='check_auth'),
]
