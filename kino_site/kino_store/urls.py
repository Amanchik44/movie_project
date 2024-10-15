from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', MovieViewSet.as_view({'get': 'list'}), name='movie_list'),
    path('<int:pk>/', MovieViewSet.as_view({'get'}), name='movie_detail'),

    path('country', CountryViewSet.as_view({'get': 'list', }), name='country_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get'}), name='country_detail'),

    path('director', DirectorViewSet.as_view({'get': 'list'}), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get'}), name='director_detail'),

    path('actor', ActorViewSet.as_view({'get': 'List'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get'}), name='actor_detail'),

    path('janre/', JanreViewSet.as_view({'get': 'List'}), name='janre_list'),
    path('janre/<int:pk>/', JanreViewSet.as_view({'get'}), name='janre_detail'),

    path('user', UserProfileViewSet.as_view({'get': 'list'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get'}), name='user_detail'),

    path('movieLanguages', MovieLanguagesViewSet.as_view({'get': 'list'}), name='movieLanguages_list'),
    path('movieLanguages/<int:pk>/', MovieLanguagesViewSet.as_view({'get'}), name='movieLanguages_detail'),

    path('moments', MomentsViewSet.as_view({'get': 'list'}), name='moments_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get'}), name='moments_detail'),

    path('rating', RatingViewSet.as_view({'get': 'list'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get'}), name='rating_detail'),

    path('favorite', FavoriteViewSet.as_view({'get': 'list'}), name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get'}), name='favorite_detail'),

    path('favorite_movie', FavoriteMovieViewSet.as_view({'get': 'list'}), name='favorite_movie_list'),
    path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get'}), name='favorite_detail'),

    path('history', HistoryViewSet.as_view({'get': 'list'}), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get'}), name='history_detail'),
]