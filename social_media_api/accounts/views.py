from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]  # <= This is the problem
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

User = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Follow a specific user."""
        user_to_follow = get_object_or_404(User, id=user_id)
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(user_to_follow)
        return Response({"detail": f"You are now following {user_to_follow.username}"},
                        status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Unfollow a specific user."""
        user_to_unfollow = get_object_or_404(User, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"},
                        status=status.HTTP_200_OK)
