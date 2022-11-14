from django.urls import path
from .views import *

app_name = 'portal'
urlpatterns = [
    path('', index_page, name='home_page'),
    path('members/', list_view_member, name='list_member_url'),
    path('attendances/', list_view_attendance, name='list_attendance_url'),
    path('att_summ/', attendance_summmaries_list, name='list_summary_attendance_url'),
    path('groups/', groups_list, name='list_group_url'),
    path('chapels/', chapel_list, name='list_chapel_url'),
    path('grouplead/', db_user_list, name='list_grouplead_url'),
    # path('members/<int:pk>', members_details, name='details_member_urls'),
    # path('groups/<int:pk>/', groups_details, name='details_group_urls'),
    path('chapels/<int:id>/', chapel_detail, name='details_chapels_urls'),
    # # path('grouplead/<int:id>/', db_detail, name='details_grouplead_urls'),
    # # path('members/<id>/', details_membs, name='details_members_urls'),
    # path('addgroup/', create_view_group, name='add_group_url'),
    # path('addchapel/', create_chapel, name='add_chapel_url'),
    path('memlist/', memberindex, name='lazyloadmem'),
    # # path('dbuserlistindex/', db_userindex, name='mems'),
    # path('groups/<int:pk>/delete', group_delete, name='delete_group'),
    # path('groups/<int:pk>/delete', dbuser_delete, name='delete_group_head'),
    # path('add_member/', create_members, name='add_member_url'),
]