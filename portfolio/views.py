from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import Summary, Project, Publication, Member, Post
from .forms import ContactForm, SummaryForm

#ホーム
def home(request):
    summary = Summary.objects.first()
    projects = Project.objects.all()
    publication = Publication.objects.all()
    member = Member.objects.all()
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

    return render(request, 'portfolio/index.html', {'summary': summary,
                                                    'projects': projects,
                                                    'publication': publication,
                                                    'member': member,
                                                    'form': form})
#ブログページ設定
def blog(request):
    summary = Summary.objects.first()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'portfolio/post_detail.html', {'post': post})

#メンバーページ設定
def member(request):
    summary = Summary.objects.first()
    member = Member.objects.all()

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
