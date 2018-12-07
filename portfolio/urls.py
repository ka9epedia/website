from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('member/', views.member, name='member'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
