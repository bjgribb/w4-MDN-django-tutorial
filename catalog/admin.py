from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language, AuthorAdmin

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Author, AuthorAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass
