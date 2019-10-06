
from django.contrib import admin
from django.urls import path, include

from user.views import ( index, user_login, user_logout,
    success, MyProfile)

urlpatterns = [
    path('', index, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('profile/', MyProfile.as_view(), name="my_profile"),
    path('profile/update', MyProfile.as_view(), name="update_profile"),
]
