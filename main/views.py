from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    categories = [category.category_slug for category in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(category__category_slug=single_slug)
        series_urls = {}
        for matchedSerie in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__series=matchedSerie.series).earliest("tutorial_published")
            series_urls[matchedSerie] = part_one.tutorial_slug
        return render(request,
               template_name="main/category.html",
               context={"part_ones": series_urls})
    
    tutorials = [tutorial.tutorial_slug for tutorial in Tutorial.objects.all()]
    if single_slug in tutorials:
        return HttpResponse(f"{single_slug} is a tutorial.")
    
    return HttpResponse(f"{single_slug} does not corresponding to anything.")

# def homepage(request):
#     return render(request=request,
#                   template_name="main/home.html",   #django will look in every app for dir templates so this is why this syntax for main/templates/main/home.html
#                   context={"tutorials": Tutorial.objects.all}
#                   )
def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",   #django will look in every app for dir templates so this is why this syntax for main/templates/main/home.html
                  context={"categories": TutorialCategory.objects.all}
                  )

def aboutpage(request):
    return HttpResponse(
        "<h1>This is about page</h1>"
        "<p>Lorem ipsum dolor sit amet...</p>"
        )

def register(request):

    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data("username")
            # messages.success(request, f"New acc is created for user")
            login(request, user)
            return redirect("main:homepage")
        else:
            for message in form.error_messages:
                messages.error(request, f"{message}: {form.error_messages[message]}")
    # re-render register page
    form = NewUserForm
    return render(request=request,
                template_name="main/register.html",
                context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("passowrd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You logged in successfully with username {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm
    return render(request=request,
                  template_name="main/login.html",
                  context={"form":form})
