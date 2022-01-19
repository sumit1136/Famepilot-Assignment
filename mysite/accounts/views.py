from accounts.serializers import LoginSerializer, RegisterSerializer
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from . models import Person
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

@method_decorator(login_required, name='dispatch')
class profile(TemplateView):
    template_name = 'accounts/profile.html'
    def get(self,request,*args, **kwargs):
        self.username = request.user.username
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['json_data'] = Person.objects.get(username = self.username)
        return context

class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/login.html'
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        auth.login(request,user)
        print('Signed In')
        return redirect('home')
    def get(self,request):
        serializer = LoginSerializer()
        return Response({"serializer":serializer})

class Register(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'accounts/signup.html'
    
    def get(self, request):
        serializer = RegisterSerializer()
        return Response({"serializer":serializer})

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        person = serializer.validated_data['person']
        user = serializer.validated_data['user']
        person.save()
        print('Person added in Person table')
        user.save()
        print('Person added in authentication')
        return redirect('login')



