from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from django.core.mail import send_mail
from rest_framework import status
from .models import UserProfile
from .serializers import  ChangePasswordSerializer, UserProfileDetailSerializer

# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user":{
                'user': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role
            }   
        },status=200)
    
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserProfile
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile_detail(request):
    user = request.user
    user_ser = UserProfileDetailSerializer(user)
    return Response({'user': user_ser.data}, status=200)

@api_view(['POST'])
def create_user_profile(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    user_type = request.POST.get('user_type', 'is_student')

    # Check if email already exists
    if UserProfile.objects.filter(email=email).exists():
        return Response({'detail': 'Email address already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if username already exists
    if UserProfile.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if all required fields are present
    if not all([first_name, last_name, email, password, username, user_type]):
        return Response({'detail': 'All required fields are not present'}, status=status.HTTP_400_BAD_REQUEST)

    user_profile = UserProfile.objects.create(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        role=user_type
    )
    user_profile.save()
    message = f'Hello,\n\nThank you for signing up for Consultancy Management System! To get started, please click on the following link to verify your account : https://esan.hikingbees.com/api/verify-user-profile/?user={user.id} \n\nBest regards,\nESAN'

    send_mail(
        'Verify Your ESAN Account',
        message,
        'hreedhann9@gmail.com',
        [email],
        fail_silently=False,
    )
    return Response({'success': 'User profile created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_user_profile(request):
    user = request.user
    data = {
        'user': {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role,
        }
    }

    return Response(data, status=200)
    

@api_view(['GET'])
def get_users(request):
    users = UserProfile.objects.all()
    users_serializer = UserProfileDetailSerializer(users, many=True)
    return Response({"users": users_serializer.data}, status=200)

@api_view(['GET'])
def get_user_detail(request):
    username = request.GET.get("name")
    user = UserProfile.objects.get(username=username)
    users_serializer = UserProfileDetailSerializer(user)

    response_data = users_serializer.data
    return Response(response_data, status=200)

@api_view(['POST'])
def update_user_detail(request):
    username = request.POST.get("username")
    user = UserProfile.objects.get(username=username)

    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.email = request.POST.get("email")
    user.phone_number = request.POST.get("phone_number", "")
    user.address = request.POST.get("address", "")
    user.avatar = request.FILES.get("avatar")
    
    user.save()

    return Response({"success": "Updated successfully"}, status=200)
