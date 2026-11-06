
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import BirthdayWish, BirthdayImage


# Base Page
def base(request):
    return render(request, 'base.html')


# Homepage with 7 Birthday Templates
def home(request):

    templates = [
        {
            "id": "classic",
            "name": "Classic Birthday",
            "description": "Elegant & Timeless",
            "emoji": "🎂",
            "gradient": "classic",
            "preview": "A beautiful cake, candles and elegant birthday message."
        },
        {
            "id": "romantic",
            "name": "Romantic Wish",
            "description": "Filled with Love",
            "emoji": "💖",
            "gradient": "romantic",
            "preview": "A romantic birthday design with hearts and roses."
        },
        {
            "id": "photo_gallery",
            "name": "Photo Gallery",
            "description": "Beautiful Memories",
            "emoji": "📸",
            "gradient": "gallery",
            "preview": "A collection of personal photos and special memories."
        },
        {
            "id": "surprise",
            "name": "Surprise Box",
            "description": "A Special Surprise",
            "emoji": "🎁",
            "gradient": "surprise",
            "preview": "An animated gift box birthday surprise."
        },
        {
            "id": "cake_theme",
            "name": "Cake Celebration",
            "description": "Sweet & Joyful",
            "emoji": "🧁",
            "gradient": "cake",
            "preview": "A colorful cake-themed birthday celebration."
        },
        {
            "id": "cinematic",
            "name": "Cinematic",
            "description": "Dreamy & Magical",
            "emoji": "🌙",
            "gradient": "cinematic",
            "preview": "A dark, dreamy birthday experience."
        },
        {
            "id": "minimal",
            "name": "Minimal",
            "description": "Simple & Beautiful",
            "emoji": "🌸",
            "gradient": "minimal",
            "preview": "A clean and modern birthday greeting."
        },
    ]

    return render(request, 'home.html', {
        'templates': templates
    })


# Create Birthday Wish
def create_birthday(request):

    # Get selected layout from homepage
    selected_theme = request.GET.get('theme', 'classic')

    # Validate theme
    valid_themes = dict(BirthdayWish.THEME_CHOICES)

    if selected_theme not in valid_themes:
        selected_theme = 'classic'

    if request.method == "POST":

        selected_theme = request.POST.get('theme', 'classic')

        if selected_theme not in valid_themes:
            selected_theme = 'classic'

        birthday = BirthdayWish(
            card_title=request.POST.get("card_title"),
            sender_name=request.POST.get("sender_name"),
            birthday_person=request.POST.get("birthday_person"),
            age=request.POST.get("age"),
            message=request.POST.get("message"),
            image=request.FILES.get("image"),
            theme=selected_theme,
        )

        birthday.save()

        return redirect('link_created', uuid=birthday.id)

    return render(request, 'create_birthday.html', {
        'selected_theme': selected_theme
    })


# Birthday Link Created
def link_created(request, uuid):

    birthday = get_object_or_404(BirthdayWish, id=uuid)

    birthday_url = request.build_absolute_uri(
        reverse('birthday_cake', kwargs={'uuid': birthday.id})
    )

    return render(request, 'link_created.html', {
        'birthday': birthday,
        'birthday_url': birthday_url
    })


# Birthday Cake Page
def birthday_cake(request, uuid):

    birthday = get_object_or_404(BirthdayWish, id=uuid)

    return render(request, 'birthday_cake.html', {
        'birthday': birthday
    })


# Birthday Wish Page
def birthday_wish(request, uuid):

    birthday = get_object_or_404(BirthdayWish, id=uuid)

    # Get all additional birthday photos
    birthday_images = [
        {
            'url': photo.image.url,
            'message': photo.message
        }
        for photo in birthday.photos.all()
    ]

    # Select layout based on saved theme
    theme_templates = {
        'classic': 'birthday_templates/classic.html',
        'romantic': 'birthday_templates/romantic.html',
        'photo_gallery': 'birthday_templates/photo_gallery.html',
        'surprise': 'birthday_templates/surprise.html',
        'cake_theme': 'birthday_templates/cake_theme.html',
        'cinematic': 'birthday_templates/cinematic.html',
        'minimal': 'birthday_templates/minimal.html',
    }

    template_name = theme_templates.get(
        birthday.theme,
        'birthday_templates/classic.html'
    )

    return render(request, template_name, {
        'birthday': birthday,
        'birthday_images': birthday_images
    })
