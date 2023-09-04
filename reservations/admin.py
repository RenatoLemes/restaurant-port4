from django.contrib import admin
from .models import Table, Reservation


# admin.site.register(Table)
# admin.site.register(Reservation)

# I need the admin classes here

# prepopulated_fields = {'slug': ('guest_name',)}

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('table_number', 'created_on', 'num_of_reservations')
    search_fields = ['table_number', ]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('id', 'guest_name', 'table', 'date_time',)
