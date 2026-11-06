
from django.contrib import admin
from .models import BirthdayWish


@admin.register(BirthdayWish)
class BirthdayWishAdmin(admin.ModelAdmin):

    # Display fields in admin list
    list_display = (
        'card_title',
        'birthday_person',
        'sender_name',
        'age',
        'created_at',
    )

    # Search birthday cards
    search_fields = (
        'card_title',
        'birthday_person',
        'sender_name',
        'message',
    )

    # Filter birthday cards
    list_filter = (
        'created_at',
    )

    # Default ordering
    ordering = ('-created_at',)

    # Read-only fields
    readonly_fields = (
        'id',
        'created_at',
    )

    # Fields displayed in edit form
    fieldsets = (

        ('Birthday Card Details', {
            'fields': (
                'id',
                'card_title',
                'birthday_person',
                'sender_name',
                'age',
                'message',
            )
        }),

        ('Birthday Customization', {
            'fields': (
                'image',
            )
        }),

        ('Additional Information', {
            'fields': (
                'created_at',
            )
        }),

    )

    # Number of records per page
    list_per_page = 20
