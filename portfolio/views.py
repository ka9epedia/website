from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Degree, Skill, Summary, Project, Publication, Members
from .forms import ContactForm, SummaryForm

#ホーム
def home(request):
    skills = Skill.objects.all()
    degrees = Degree.objects.all()
    summary = Summary.objects.first()
    projects = Project.objects.all()
    publication = Publication.objects.all()
    member = Members.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            subject = "You have a new message from {}: <{}>" \
                      .format(name, email)
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email]
            contact_message = "Sent by: %s\n\nEmail: %s\n\nMessage:\n\n%s" \
                              % (name, email, message)
            send_mail(subject,
                      contact_message,
                      from_email,
                      [to_email],
                      fail_silently=False)
            return JsonResponse({
                'success': True,
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })

    return render(request, 'portfolio/index.html', {'skills': skills,
                                                    'degrees': degrees,
                                                    'summary': summary,
                                                    'projects': projects,
                                                    'publication': publication,
                                                    'member': member,
                                                    'form': form})
#ブログページ設定
def blog(request):
    summary = Summary.objects.first()

    return render(request, 'portfolio/blog.html', {'summary': summary})

#メンバーページ設定
def member(request):
    summary = Summary.objects.first()
    member = Members.objects.all()

    return render(request, 'portfolio/member.html', {'summary': summary,
                                                     'member': member})

#コンタクトページ設定
def contact(request):
    summary = Summary.objects.first()

    return render(request, 'portfolio/contact.html', {'summary': summary})

#イベントページ設定
def event(request):
    summary = Summary.objects.first()

    return render(request, 'portfolio/event.html', {'summary': summary})

#アンケートページ設定
def questionnaire(request):
    return render(request, 'portfolio/questionnaire.html')
