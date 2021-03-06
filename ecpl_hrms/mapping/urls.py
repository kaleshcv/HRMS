"""ecpl_hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    # Add user and Profile
    path('create-user',createUserandProfile),
    path('home',employeeMapping),
    path('emp-id',empIDwiseData),

    path('login',mappingLogin),
    path('logout',mappingLogout),
    path('change-password',change_password),

    path('team-wise',teamWiseData),
    path('update-employee-profile',updateEmployeeProfile),
    path('update-employee-profile/empid-search',searchForEmployee),
    path('update-to-system',updateToSystem),
    path('update-team-rm',updateTeamRms),

    path('update-rm1/<str:team>/<str:rm1>',updateRM1forTeam),
    path('update-team-rm1',updateTeamRm1),
    # Team RM2
    path('update-rm2/<str:team>/<str:rm2>',updateRM2forTeam),
    path('update-team-rm2',updateTeamRm2),
    # Team RM3
    path('update-rm3/<str:team>/<str:rm3>',updateRM3forTeam),
    path('update-team-rm3',updateTeamRm3),

    path('correct-process',correct_process),
    path('export-mapping',exportMapping),

    path('name-changer',nameChanger),

    ]
