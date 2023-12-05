from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AppDevClubReviewsView(APIView):
    reviews = [
        'app dev is great',
        'you should join',
        'hello world',
        'add more react workshops'
    ]

    def get(self, request):
        return Response({'reviews': self.reviews})

    def post(self, request):
        new_review = request.data.get('review', None)
        if new_review is not None:
            self.reviews.append(new_review)
            return Response({'message': 'Review added successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Review cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)
