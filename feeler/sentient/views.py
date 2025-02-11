'''module: views
this setups an endpoint to serve out prediction and other defined endpoints.
'''

################ auth imports start 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
################ end

# for logout endpoint;
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import JsonResponse
import json
from .predict import predict_emotion
from .models import SentimentHistory

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    '''this is a test endpoint for auth - we will keep it :)'''
    return Response({'message': "API running - you're authenticated"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict_sentiment(request):
    '''TensorFlow ML model endpoint - does the sentiment analysis and saves to history'''
    try:
        text = request.data.get('text', '').strip()

        if not text:
            return Response(
                {'error': 'Text input cannot be empty'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Perform the prediction
        sentiment, confidence = predict_emotion(text)

        # Save the prediction to the database
        SentimentHistory.objects.create(
            user=request.user,
            text=text,
            sentiment=sentiment,
            confidence=confidence
        )

        # Return the response to the user
        return Response({
            'sentiment': sentiment,
            'confidence': confidence
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {'error': str(e)}, 
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([AllowAny])  # Allow all users to access registration
def register_user(request):
    '''registration'''
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email', '')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    '''LOGOUT of moodlens'''
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    '''History Endpoint - last 5'''
    try:
        sentiments = SentimentHistory.objects.filter(user=request.user).order_by('-created_at')[:5]
        data = [
            {
                'text': s.text,
                'sentiment': s.sentiment,
                'confidence': s.confidence,
                'created_at': s.created_at
            } for s in sentiments
        ]
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_visualization_data(request):
    '''data points for graph
    generate data for a line chart or sine wave based on sentiment history
    '''
    try:
        sentiments = SentimentHistory.objects.filter(user=request.user).order_by('-created_at')[:5]
        data = {
            'labels': [s.created_at.strftime('%Y-%m-%d %H:%M') for s in sentiments],
            'sentiments': [1 if s.sentiment == 'positive' else -1 for s in sentiments],  # 1 for positive, -1 for negative
        }
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
