from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import *
from calendar import Calendar, monthrange
from mapping.models import Profile
from django.contrib import messages
c = Calendar()
from datetime import date


# Create your views here.
def loginPage(request):
    form = AuthenticationForm()
    teams = Profile.objects.values_list('emp_process', flat=True).distinct()
    data = {'teams':teams,'form':form}
    return render(request,'ams/login.html',data)

def loginAndRedirect(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Login form
        team = request.POST['team']
        if form.is_valid():
            # login the user
            user = form.get_user()
            login(request, user)
            if team != request.user.profile.emp_process:
                logout(request)
                messages.info(request,'Invalid Team')
                return redirect('/ams')
            if request.user.profile.emp_desi == 'Team Leader - (Bigo)':
                return redirect('/ams/tl-dashboard')
            else:
                return redirect('/ams/agent-dashboard')
        else:
            form = AuthenticationForm()
            m = 'Invalid Credentials !'
            return render(request, 'ams/login.html', {'form': form, 'm': m})

def teamDashboard(request):
    return render(request,'ams/team-dashboard.html')

def agentDashBoard(request):
    today = date.today()
    #today = '2021-9-24'
    emp_name = request.user.profile.emp_name
    emp_id = request.user.profile.emp_id
    emp = Profile.objects.get(emp_id = emp_id)
    try:
        cal_day = EcplCalander.objects.get(date=today,applied_status=True,emp_id=emp_id)
        today = 'Applied'
    except EcplCalander.DoesNotExist:
        today = str(today)

    #attendance status
    cal = EcplCalander.objects.filter(emp_id=emp_id).order_by('-date')[:3]
    data = {'emp_name':emp_name,'emp':emp,'date':today,'cal':cal}
    return render(request,'ams/agent-dashboard.html',data)

def tlDashboard(request):
    emp_name = request.user.profile.emp_name
    emp_id = request.user.profile.emp_id
    emp = Profile.objects.get(emp_id=emp_id)
    cal = EcplCalander.objects.filter(approved_status=False,rm1=emp_name)

    # details
    today = date.today()
    today = str(today)
    att_details = EcplCalander.objects.filter(date = today,rm1=emp_name)

    #counts
    emp_count = Profile.objects.filter(emp_rm1=emp_name).count()
    active_today = EcplCalander.objects.filter(rm1=emp_name,date=today).count()
    unmarked_today = emp_count-active_today

    data = {'emp_name': emp_name, 'emp': emp,'cal':cal, 'att_details':att_details,
            'emp_count':emp_count,'active_today':active_today,'unmarked_today':unmarked_today,
            }
    return render(request, 'ams/rm-dashboard.html', data)



def indexPage(request):
    team_name = 'Gubagoo'
    emp_team_obj = Profile.objects.filter(emp_process = team_name)
    data = {'team':emp_team_obj}
    return render(request,'ams/index.html',data)

def employeeDetails(request,pk):
    emp_id = pk
    emp_obj = Profile.objects.get(emp_id = emp_id)
    data = {'employee':emp_obj}
    return render(request, 'ams/employee-details.html', data)


def applyAttendace(request):
    if request.method == 'POST':
        date = request.POST['date']
        att_applied = request.POST['att_applied']
        rm1 = request.POST['rm1']
        rm2 = request.POST['rm2']
        rm3 = request.POST['rm3']
        emp_id = request.user.profile.emp_id
        emp_name = request.user.profile.emp_name
        team = request.user.profile.emp_process

        cal = EcplCalander.objects.create(
            team = team, date = date, emp_name = emp_name, emp_id = emp_id,
            att_applied = att_applied,applied_by = emp_id,applied_status = True,
            rm1 = rm1, rm2 = rm2, rm3 = rm3
        )
        cal.save()

        return redirect('/ams/agent-dashboard')
    else:
        pass

def rmApproval(request,id):
    if request.method == 'POST':
        id =id

        att_approved = request.POST['att_approved']
        cal = EcplCalander.objects.get(id=id)
        cal.att_approved = att_approved
        cal.approved_status = True
        cal.save()

        return redirect('/ams/tl-dashboard')

