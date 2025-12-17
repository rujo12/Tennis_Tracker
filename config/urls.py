
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from players.views import PlayerViewSet, FavouritePlayerViewSet
from matches.views import MatchViewSet

router = DefaultRouter()
router.register(r"players", PlayerViewSet, basename="player")
router.register(r"favourites", FavouritePlayerViewSet, basename="favourite")
router.register(r"matches", MatchViewSet, basename="match")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include('djoser.urls')),
    path("api/auth/", include('djoser.urls.jwt')),
    path("api/", include(router.urls)),
    path('', include('frontend.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

