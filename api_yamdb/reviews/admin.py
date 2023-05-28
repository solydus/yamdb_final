from django.contrib import admin
from django.db.models import Avg
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title

from api_yamdb.settings import LISTING__PAGE


@admin.register(Genre)
class ClassGenreAdminka(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'slug'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('name',)
    list_per_page = LISTING__PAGE
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class ClassCategory(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'slug'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('name',)
    list_per_page = LISTING__PAGE
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Title)
class ClassTitle(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category',
        'get_genre',
        'count_reviews',
        'get_rating'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('name',)
    list_per_page = LISTING__PAGE
    search_fields = ('name', 'year', 'category')

    def get_genre(self, object):
        return '\n'.join((genre.name for genre in object.genre.all()))

    get_genre.short_description = 'Жанр/ы произведения'

    def count_reviews(self, object):
        return object.reviews.count()

    count_reviews.short_description = 'Количество отзывов'

    def get_rating(self, object):
        rating = object.reviews.aggregate(average_score=Avg('score'))
        return round(rating.get('average_score'), 1)

    get_rating.short_description = 'Рейтинг'


@admin.register(Review)
class ClassAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'author',
        'text',
        'score',
        'pub_date',
        'title'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('author', 'score', 'pub_date')
    list_per_page = LISTING__PAGE
    search_fields = ('author',)


@admin.register(GenreTitle)
class GenreTitle(admin.ModelAdmin):

    list_display = (
        'pk',
        'genre',
        'title'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('genre',)
    list_per_page = LISTING__PAGE
    search_fields = ('title',)


@admin.register(Comment)
class ClassComment(admin.ModelAdmin):

    list_display = (
        'pk',
        'author',
        'text',
        'pub_date',
        'review'
    )
    empty_value_display = 'пустое значение'
    list_filter = ('author', 'pub_date')
    list_per_page = LISTING__PAGE
    search_fields = ('author',)


admin.site.site_header = 'admin YaMDb'
admin.site.site_title = 'admin YaMDb'
