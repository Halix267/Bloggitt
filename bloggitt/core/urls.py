from . import views
from django.urls import path
from .views import PostLikeToggle , PostLikeAPIToggle,ProfileUpdateView,ProfileView

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('favorites/', views.favorites, name='favorites'),
    path('', views.postlist, name='home'),
    # path('post/detail/<slug:slug>/', views.postdetail, name='post_detail'),
    # path('post/detail/<slug:slug>/Favourites', views.Favorites, name='Favorites'),
    # path('about',views.aboutdetail,name='about'),
    path('post/like/<slug:slug>/', PostLikeToggle.as_view(), name='like-toggle'),
    path('api/like/<slug:slug>/', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    path('detail/<slug:slug>/', views.postdetail, name='post_detail'),
    path('detail/<slug:slug>/Favourites', views.Favorites, name='Favorites'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('about/',views.about,name='about')
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)