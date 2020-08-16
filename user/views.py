from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserUpdateForms,ProfileUpdateForm
from .models import Post
from .models import Profile
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
# class home(ListView):
#     template_name = 'home.html'
# def home(request):
#     return render(request, 'home.html')
class home(ListView):
    model = Post
    template_name='home.html'


def register(request):
    if request.method =='POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account Has Been Created for {username} Please LogIn')
            return redirect('login')
        else:
            form = UserRegisterForm()
    form = UserRegisterForm
    return render(request, 'register.html',context={'form':form} )
@login_required
def profile(request):
        if request.method =='POST':
            u_form = UserUpdateForms(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request,f'Your Account Has Been Updated')
                return redirect('profile')
        else:
            u_form = UserUpdateForms(instance=request.user)
            p_form =  ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form' : u_form,
            'p_form': p_form
        }
        return render(request, 'profile.html',context)
def service(request):
    if request.method=='POST':
        email = request.POST.get('Email')
        desc= request.POST.get('desc')
        service = Service(Email = email,desc=desc)
        service.save()
    return render(request,'service.html')
def contact(request):
    if request.method =='POST':
        name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        state = request.POST.get('state')
        email = request.POST.get('Email')
        city = request.POST.get('city')
        contact = Contact(first_name=name,last_name= last_name,state=state,Email=email,city=city)
        contact.save()
    return render(request,'contact.html')


def about(request):
    return render(request, 'about.html')


class ArticleDetail(DetailView):
    model = Post
    template_name = 'articledetail.html'
class AddPost(CreateView):
    model = Post
    template_name ='add_post.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return  super().form_valid(form)

def mehdi(request):
    return render(request, 'mehdi.html')

class blog(ListView):
    model = Post
    template_name= 'blog.html'