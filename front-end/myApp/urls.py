from django.urls import path
from . import views
from .views import send_email


urlpatterns = [
    path('', views.login_page, name='login'),  # <-- Make sure the name is 'login'
    path('main/', views.check_readings_page, name='main'),
    path('signup/', views.signup_page, name='signup'),
    path('image_line/', views.check_readings_page, name='image_line'),
    path('send_email/', views.send_email, name='send_email'),
    path('problemsTable/', views.problemsTable, name='problemsTable'),
    path('communityTable/', views.communityTable, name='communityTable'),
    path('page1/', views.page1_view, name='page1'),
]
