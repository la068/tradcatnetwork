from django.shortcuts import render
from .models import Post, Contact, About, PrivacyPolicy, TermsOfUse

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-date_posted")
    data={"posts":posts}
    return render(request, "blog/index.html", data)

def view_post(request, post_id):
    post=Post.objects.get(id=post_id)
    data = {"post":post}
    return render(request, "blog/view_post.html", data)

def contact(request):
    info = Contact.objects.all()
    data = {"contact":info}
    return render(request, "blog/contact.html", data)

def about(request):
    about = About.objects.all()
    return render(request, "blog/about.html", {"about":about})

#privacy policy
def privacy_policy(request):
    policy = PrivacyPolicy.objects.all()
    return render(request, "blog/privacy_policy.html", {"policy":policy})

#terms of use
def terms_of_use(request):
    terms = TermsOfUse.objects.all()
    return render(request, "blog/terms_of_use.html", {"terms":terms})


#Themes
def theme(request):
    time=datetime.now.hour
    if time >=18:
        theme = "dark"
    else:
        theme = "light"
    return render(request, "blog/index.html", {"theme":theme})
