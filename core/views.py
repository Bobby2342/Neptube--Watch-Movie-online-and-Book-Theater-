from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

from core.models import Movie, Theater, User

# Create your views here.

@login_required
def home(request):
    movie = Movie.objects.all()
    return render (request,'home.html',{'movie':movie})

def upload(request):
    if request.method =='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        url = request.POST.get('url')
        imgurl=request.POST.get('imgurl')
        video =request.FILES.get('video')

        movie = Movie.objects.create(

            name=name,
            description=description,
            url=url,
            imgurl=imgurl,
            video=video,

            
        )

        return HttpResponse('Movie created sucessfully!')
    


    return render (request,'upload.html')


def videoplayer(request, movie_id):
    movie = Movie.objects.get( pk=movie_id)
    return render(request, 'videoplayer.html',{'movie':movie})
def videoplayer_without_id(request):
    movie = Movie.objects.all()
    return render(request, 'videoplayer.html',{'movie':movie})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
        
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return HttpResponseRedirect('/dashboard/')
        else:
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:  # Handle GET requests separately
        return render(request, 'login.html')
    

def logout(request):

    logout(request)

    return redirect('home')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

    



        # Create and save the new user
        user = User.objects.create(
            name=name,
            email=email,
            password=password
        )

        # Redirect to the login page or another appropriate page
        return redirect('login')

    return render(request, 'signup.html')

def theater(request):

    theater =Theater.objects.all()
    return render(request, 'theater.html',{'theater':theater})


def ticket(request):

    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        hallname = request.POST.get('hallname')
        imgurl =request.POST.get('imgurl')
        price = request.POST.get('price')
        location = request.POST.get('location')

        theater = Theater.objects.create(

            name =  name,
            description = description,
            hallname = hallname,
            imgurl = imgurl,
            price = price,
            location=location,


        )

        return HttpResponse('Ticket Created Successfully')

    return render(request, 'ticket.html')


def bookticket(request):
    return render(request, 'bookticket.html')


def theaterdetails(request, theater_id):
    theater = get_object_or_404(Theater, pk=theater_id)
    return render(request, 'theaterdetails.html', {'theater': theater})

# views.py
from django.shortcuts import render
from social_django.models import UserSocialAuth

def profile(request):
    user = request.user

    # Get the user's social authentication details for Google
    social_auth = UserSocialAuth.objects.filter(user=user, provider='google-oauth2').first()

    gmail_login_name = None
    if social_auth:
        gmail_login_name = social_auth.uid  # Assuming UID is the Gmail login (email)
        profile_picture_url = social_auth.extra_data.get('picture')
    return render(request, 'profile.html', {'gmail_login_name': gmail_login_name},{'profile_picture_url':profile_picture_url})