from django.urls import path
from main.views import *

urlpatterns = [
    path('',show_news,name='show_news'),
    path('new_page/<int:id>',new_page,name='new_page'),
    path('edit_page/<int:id>',edit_page,name='edit_page'),
    path('delete_new/<int:id>',delete_new,name='delete_new'),
    path('add_new',add_new,name='add_new')
]
