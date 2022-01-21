from django.shortcuts import render,redirect,HttpResponseRedirect ,HttpResponse
from django.db.models import Q
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.

def homePage(request):
    global postlarim

    Mypostlar = CreatePost.objects.all()
    query = request.GET.get('q')

    if query:
        Mypostlar = Mypostlar.filter(
            Q(title__icontains=query) |
            Q(tag__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(Mypostlar,5)

    sayfa = request.GET.get('sayfa')
    postlarim = paginator.get_page(sayfa)
    deneme = CreatePost.objects.filter(tag='django')
    all = deneme.count()
    return render(request,'index.html',{'postlarim':postlarim,'deneme':all})

def aboutPage(request):
    return render(request,'about.html')

def contactPage(request):
    return render(request,'contact.html')

def ContactMail(request):
    if request.method == 'POST':
        name = request.POST.get('AboutName')
        email = request.POST.get('AboutEmail')
        message = request.POST.get('AboutMessage')
        context = "Mesaj: {} \n\nGönderen:{}\n\nE-Posta:\n{}".format(message,name,email)
        send_mail('freedom-iletisim',context,'tahayagma@gmail.com',['tahayagma@gmail.com'])
        messages.success(request,'Mesajınız gönderildi.')
        return HttpResponseRedirect('iletisim')




def detailPage(request,slug):
    global postID

    postdetail = CreatePost.objects.get(slug=slug)
    postID = postdetail.id
    yorumlar = MakeComment.objects.filter(Comments_id=postID)
    yorumlar_sayisi = yorumlar.count()
    return render(request,'detail.html',{'postdetail':postdetail,'yorumlar_sayisi':yorumlar_sayisi,'yorumlar':yorumlar})



def commentsave(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        data = MakeComment(
            nameSurname = name,
            email = email,
            Content = message,
            Comments_id = postID
        )
        data.save()
        for i in postlarim:
            a = i.slug
            messages.success(request, 'Mesajınız gönderildi.')
        return  HttpResponseRedirect('anasayfa/{}'.format(a))


def tags(request,tag):
    tagss = CreatePost.objects.get(tag=tag)
    return render(request,'index.html',{'tagss':tagss})
