from django.urls import path
from reviews.views import AppDevClubReviewsView

urlpatterns = [
    path('reviews', AppDevClubReviewsView.as_view(), name='reviews'),
]