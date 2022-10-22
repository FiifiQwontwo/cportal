from django.shortcuts import get_object_or_404, render, redirect
from portal.models import AttendanceSummaries, Attendances, Members, Groups, Chapels, DBUser
from django.core.cache import cache
from .forms import CreateGroupForm, CreateChapelForm, CreateMemberForm
import json


def index_page(request):
    memcounts = Members.objects.all().count()
    groupcount = Groups.objects.all().count()
    usercount = DBUser.objects.all().count()
    chapscount = Chapels.objects.all().count()
    db_usered = DBUser.objects.all().order_by('-id')[:30].select_related('chapel', 'group')

    context = {
        'memcounts': memcounts,
        'groupcount': groupcount,
        'usercount': usercount,
        'chapscount': chapscount,
        'db_usered': db_usered,

    }
    return render(request, 'index.html', context)


def memberindex(request):
    mil = Members.objects.all().order_by('-id')[:5].select_related('group', 'chapel')
    # nil = DBUser.objects.filter(group__id = Members.group)

    context = {
        'mil': mil,
        # 'nil': nil
    }
    return render(request, 'membersindex.html', context)


def list_view_member(request):
    memlist = Members.objects.all().select_related('chapel', 'group')
    # groud = DBUser.objects.filter(group__id=Members.group)

    context = {
        'memlist': memlist
        # 'groud': groud,
    }
    return render(request, 'member/list.html', context)


def groups_list(request):
    gro = Groups.objects.all()
    # userlist = DBUser.objects.filter(group__id=gro.id)
    context = {
        'gro': gro
        # 'userlist': userlist
    }
    return render(request, 'groups/list.html', context)


def db_user_list(request):
    db_user = DBUser.objects.all().order_by('created_at').select_related('group', 'chapel')
    context = {
        'db_user': db_user
    }
    return render(request, 'DbUser/list.html', context)


def chapel_list(request):
    chaps = Chapels.objects.all()
    context = {
        'chaps': chaps
    }
    return render(request, 'chapels/list.html', context)


# when we go to prod remember to change the date on attendance summary (service date)
def list_view_attendance(request):
    read = Attendances.objects.all().order_by('service_date').select_related('member')
    context = {
        'read': read

    }
    return render(request, 'attendance/list.html', context)


def attendance_summmaries_list(request):
    att_summary = AttendanceSummaries.objects.all().order_by('attendance_date').select_related('group')
    context = {
        'att_summary': att_summary
    }
    return render(request, 'attendance/attendance_summary.html', context)
