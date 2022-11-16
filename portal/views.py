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


def groups_details(request, pk):
    userlist = DBUser.objects.filter(group__id=pk)
    gro_membs_count = Members.objects.filter(group__id=pk).count()
    gro_membs = Members.objects.filter(group__id=pk)
    if cache.get(pk):
        print('cache')
        grodetails = cache.get(pk)
    else:
        try:
            grodetails = Groups.objects.get(pk=pk)
            cache.set(pk, grodetails)
        except Groups.DoesNotExist:
            return redirect('portal:home_page')
    context = {
        'grodetails': grodetails,
        'userlist': userlist,
        'gro_membs_count': gro_membs_count,
        'gro_membs': gro_membs

    }
    return render(request, 'groups/details.html', context)

def create_view_group(request):
    context = {}
    groupcreate = CreateGroupForm(request.POST or None)
    if groupcreate.is_valid():
        groupcreate.save()
        return redirect('portal:list_group_url')

    context['groupcreate'] = groupcreate
    return render(request, "groups/create.html", context)



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


# def chapel_detail(request, id):
#     dbleaders = DBUser.objects.filter(chapel__id=id)
#     dbleaderscount = DBUser.objects.filter(chapel__id=id).count()
#     chapel_members = Members.objects.filter(chapel__id=id)
#     chapel_members_count = Members.objects.filter(chapel__id=id).count()
#     chapdetails = get_object_or_404(Chapels, id=id)
#
#     context ={
#         dbleaders:'dbleaders',
#         dbleaderscount:'dbleaderscount',
#         chapel_members:'chapel_members',
#         chapel_members_count:'chapel_members_count',
#         chapdetails:'chapdetails'
#     }
#     return render(request,'chapels/details.html', context)

def chapel_detail(request, id):
    db_users = DBUser.objects.filter(chapel__id=id)
    dbuser_count = DBUser.objects.filter(chapel__id=id).count()
    ch_mem_count = Members.objects.filter(chapel__id=id).count()
    cha_mem = Members.objects.filter(chapel__id=id).order_by(('-id')[:5])
    membered = Members.objects.filter(group__id=id)
    if cache.get(id):
        print('we did it')
        chapdetails = cache.get(id)
    else:
        try:
            chapdetails = Chapels.objects.get(id=id)
            cache.set(id, chapdetails)

        except Chapels.DoesNotExist:
            return redirect('portal:home_page')
    context = {
        'chapdetails': chapdetails,
        'db_users': db_users,
        'dbuser_count': dbuser_count,
        'ch_mem_count': ch_mem_count,
        'cha_mem': cha_mem,
        'membered': membered

    }
    return render(request, 'chapels/details.html', context)


def create_chapel(request):
    context = {

    }
    chapel_create = CreateChapelForm(request.POST or None)
    if chapel_create.is_valid():
        chapel_create.save()
        return redirect('portal:list_chapel_url')
    context['chapel_create'] = chapel_create
    return render(request, 'chapels/add.html', context)


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
