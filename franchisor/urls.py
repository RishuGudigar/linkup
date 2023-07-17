from django.urls import path,include
from .views import Index,display,test,ProfileView,userProfileView,Data,ProfileEditView,account_redirect,contact,feedback

from . import views 
from django.conf import settings
from django.conf.urls.static import static


app_name='franchisor'





urlpatterns = [
   
    path('',Index.as_view(),name='Index'),
    path('main_display/',views.display,name='display'),
    path('forms/',Data.as_view(),name='Data'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    path('user_profile/<int:pk>',userProfileView.as_view(),name='user_profile'),
    path('profile/edit/<int:pk>/',ProfileEditView.as_view(), name='profile-edit'),
    path('contact/', contact, name='contact'),
    path('feedback/',feedback,name='feedback'),
    path('redirect/',account_redirect,name='account_redirect'),
    path('test/',test,name='test')
    
    
    # path('',views.account_redirect,name='account-redirect')
]

if settings.DEBUG:
 urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)