from django.shortcuts import render,redirect
from .models import Event, Profile, Purchase, Contribution

# Create your views here.

def home(request):
    events = Event.objects.all().order_by('-id')
    profiles = Profile.objects.all()
    event_contributions = Contribution.objects.all()

    if request.method == 'POST':
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        contributors = request.POST.getlist('contributors')
        new_event = Event(subject=subject, date=date)
        new_event.save()
        current_event = Event.objects.get(subject=subject, date=date)
        print(contributors)
        for contributor in contributors:
            user = Profile.objects.get(pk=contributor)
            new_data = Contribution(event=current_event, profile=user, amount=0)
            new_data.save()
        return redirect('/')
    context={'events':events, 'profiles':profiles,'event_contributions':event_contributions}
    return render(request, 'home.html', context)

def addProfile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        profile_pic = request.FILES.get('profile_pic')
        profile = Profile.objects.create(name=name, profile_pic=profile_pic)
        profile.save()
        return redirect('/')
    return render(request, 'addProfile.html')