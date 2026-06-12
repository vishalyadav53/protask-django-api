from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.pagination import PageNumberPagination      
from django_filters.rest_framework import DjangoFilterBackend   
from rest_framework.views import APIView                        
from rest_framework.response import Response                    
from .models import Task
from drf_yasg.utils import swagger_auto_schema
from .serializers import TaskSerializer, UserRegisterSerializer  

class TaskPagination(PageNumberPagination):
    page_size = 2  
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = TaskPagination  

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed']  
    search_fields = ['title', 'description']  

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# 🔥 YEH WALI CLASS CHECK KARO AUR FILE KO SAVE KARO
class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    # it will show the box for execution
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Bhai, naya user successfully register ho gaya!"}, status=201)
        return Response(serializer.errors, status=400)