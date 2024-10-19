
from django.http import JsonResponse

from main.models import Language, Navbar, Information, Contact, News, Donate, JoinToGroup


def main_page(request):
    languages = Language.objects.filter(status=0).values('kod', 'title', 'status')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    information = Information.objects.filter(status=0).values('language', 'title', 'full_desc', 'mini_desc', 'image', 'job', 'pdf', 'qr', 'status')
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    return JsonResponse(
        {
            'languages': list(languages),
            'navbar': list(navbar),
            'information': list(information),
            'contact': list(contact),
        }
    )


def about_us(request):
    information = Information.objects.filter(status=0).values('language', 'title', 'full_desc', 'mini_desc', 'image', 'job', 'status')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    return JsonResponse(
        {
            'navbar': list(navbar),
            'information': list(information),
            'contact': list(contact)
        }
    )


def regions(request):
    information = Information.objects.filter(status=0).values('language', 'title', 'full_desc', 'mini_desc', 'image', 'job','status')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    news = News.objects.filter(stattus=0).values('language', 'title', 'full_desc', 'mini_desc', 'video', 'image', 'posted_date', 'name')
    return JsonResponse(
        {
            'navbar': list(navbar),
            'information': list(information),
            'contact': list(contact),
            'news': list(news),
        }
    )


def documents(request):
    information = Information.objects.filter(status=0).values('language', 'title', 'full_desc', 'mini_desc', 'image', 'pdf' ,'status')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    return JsonResponse(
        {
            'navbar': list(navbar),
            'information': list(information),
            'contact': list(contact)
        }
    )


def press_sent(request):
    news = News.objects.filter(stattus=0).values('language', 'title', 'full_desc', 'mini_desc', 'video', 'image', 'posted_date', 'name')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    return JsonResponse(
    {
        'navbar': list(navbar),
        'news': list(news),
        'contact': list(contact)
    }
    )


def contacts(request):
    contact = Contact.objects.filter(status=0).values('language', 'address', 'phone1', 'phone2', 'email', 'status', 'instagram', 'telegram', 'youtube', 'whatsapp')
    navbar = Navbar.objects.filter(status=0).values('title', 'language', 'child_navbars', 'status')
    return JsonResponse(
        {
            'navbar': list(navbar),
            'contact': list(contact)
        }
    )






