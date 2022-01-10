from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Employees(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=200)
    emp_desi = models.CharField(max_length=200)
    rm1 = models.CharField(max_length=200)
    rm2 = models.CharField(max_length=200)
    rm3 = models.CharField(max_length=200)
    process = models.CharField(max_length=300)

class Attendace(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=300)
    date_time = models.DateTimeField(default=timezone.now)
    process = models.CharField(max_length=300)
    marked_by_id = models.IntegerField()
    marked_by_name = models.CharField(max_length=300)
    attendance_type = models.CharField(max_length=100,default="Unmarked")
    remarks = models.TextField()

class EcplCalander(models.Model):
    team = models.CharField(max_length=300)
    date = models.DateField()
    emp_name = models.CharField(max_length=300)
    emp_id = models.CharField(max_length=50,null=True)
    emp_desi = models.CharField(max_length=100,null=True)
    att_actual = models.CharField(max_length=50,null=True)
    approved_on = models.DateTimeField(null=True)
    appoved_by = models.CharField(max_length=300,null=True)
    applied_status = models.BooleanField(default=False)
    rm1 = models.CharField(max_length=200,null=True)
    rm2 = models.CharField(max_length=200, null=True)
    rm3 = models.CharField(max_length=200, null=True)


class OnboardingnewHRC(models.Model):

    hr_name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='hrname',null=True)
    submit_date=models.DateTimeField(default="2000-01-01 01:01")
    emp_name=models.CharField(max_length=50)
    emp_dob=models.DateField(max_length=50)
    emp_desig=models.CharField(max_length=50)
    emp_process=models.CharField(max_length=50)
    emp_pan=models.CharField(max_length=50,null=True)
    emp_aadhar=models.CharField(max_length=50,null=True)
    emp_father_name=models.CharField(max_length=50)
    emp_marital_status=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_phone=models.CharField(max_length=50,null=True)
    emp_alt_phone=models.CharField(max_length=50,null=True)
    emp_present_address=models.CharField(max_length=500)
    emp_permanent_address=models.CharField(max_length=500)
    emp_blood=models.CharField(max_length=5)
    emp_emergency_person=models.CharField(max_length=50)
    emp_emergency_number=models.CharField(max_length=50,null=True)
    emp_emergency_address=models.CharField(max_length=500)
    emp_emergency_person_two=models.CharField(max_length=50,null=True)
    emp_emergency_number_two=models.CharField(max_length=50,null=True)
    emp_emergency_address_two=models.CharField(max_length=500,null=True)
    emp_edu_qualification=models.CharField(max_length=50)
    emp_quali_other = models.CharField(null=True,max_length=100)
    emp_edu_course=models.CharField(null=True,max_length=50)
    emp_edu_institute=models.CharField(max_length=200)
    emp_pre_exp=models.IntegerField(null=True,blank=True,default=0)
    emp_pre_industry=models.CharField(max_length=50,null=True,blank=True)
    emp_pre_org_name=models.CharField(max_length=150,null=True)
    emp_pre_desg=models.CharField(max_length=50,null=True)
    emp_pre_period_of_employment_frm=models.DateField(null=True,blank=True)
    emp_pre_period_of_employment_to=models.DateField(null=True,blank=True)
    emp_pre_exp_two = models.IntegerField(null=True, blank=True, default=0)
    emp_pre_industry_two = models.CharField(max_length=50, null=True, blank=True)
    emp_pre_org_name_two = models.CharField(max_length=150, null=True, blank=True)
    emp_pre_desg_two = models.CharField(max_length=50, null=True, blank=True)
    emp_pre_period_of_employment_frm_two = models.DateField(null=True,blank=True)
    emp_pre_period_of_employment_to_two = models.DateField(null=True,blank=True)
    emp_pre_exp_three = models.IntegerField(null=True, blank=True, default=0)
    emp_pre_industry_three = models.CharField(max_length=50, null=True, blank=True)
    emp_pre_org_name_three = models.CharField(max_length=150, null=True, blank=True)
    emp_pre_desg_three = models.CharField(max_length=50, null=True, blank=True)
    emp_pre_period_of_employment_frm_three = models.DateField(null=True,blank=True)
    emp_pre_period_of_employment_to_three = models.DateField(null=True,blank=True)
    emp_bank_holder_name = models.CharField(max_length=50)
    emp_bank_name = models.CharField(max_length=50)
    emp_bank_acco_no=models.CharField(max_length=50)
    emp_bank_ifsc=models.CharField(max_length=11)
    have_system = models.CharField(null=True, max_length=10)
    require_system = models.CharField(null=True, max_length=10)
    wifi_broadband = models.CharField(null=True, max_length=10)
    emp_upload_aadhar=models.ImageField(upload_to='Aadhar/')
    emp_upload_aadhar_back=models.ImageField(upload_to='Aadhar/',null=True)
    emp_upload_pan=models.ImageField(upload_to='Pan/',null=True)
    emp_upload_id=models.ImageField(upload_to='Id/',null=True,)
    emp_upload_id_back=models.ImageField(upload_to='Id/',null=True)
    emp_upload_edu_sslc=models.ImageField(upload_to='Certificate/',null=True)
    emp_upload_edu_twelveth=models.ImageField(upload_to='Certificate/',null=True)
    emp_upload_edu_gradu=models.ImageField(upload_to='Certificate/',null=True)
    emp_upload_experience=models.ImageField(upload_to='Experience/',null=True)
    emp_upload_experience_two=models.ImageField(upload_to='Experience/',null=True)
    emp_upload_experience_three=models.ImageField(upload_to='Experience/',null=True)
    emp_upload_bank=models.ImageField(upload_to='Passbook/',null=True)

    user_created = models.BooleanField(default=False)


class MappingTickets(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_id = models.CharField(max_length=10)
    emp_desi = models.CharField(max_length=50)
    emp_rm1 = models.CharField(max_length=50)
    emp_rm2 = models.CharField(max_length=50)
    emp_rm3 = models.CharField(max_length=50)
    new_rm1 = models.CharField(max_length=50)
    new_rm2 = models.CharField(max_length=50)
    new_rm3 = models.CharField(max_length=50)
    emp_process = models.CharField(max_length=50)
    new_process = models.CharField(max_length=50)
    created_by=models.TextField()
    created_date=models.DateTimeField()
    effective_date=models.DateField()
    approved_by=models.TextField(null=True,blank=True)
    approved_date=models.DateTimeField(null=True,blank=True)
    status=models.BooleanField(default=False)


class Campaigns(models.Model):
    name=models.CharField(max_length=100)
    om = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50,null=True,blank=True)
    created_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name



class JobRequisition(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='log_user', null=True)
    req_date = models.DateField(null=True)
    hc_req = models.IntegerField(null=True)
    req_raised_by = models.CharField(max_length=150, null=True, blank=True)
    department = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    process_typ_one = models.CharField(max_length=50, null=True, blank=True)
    process_typ_two = models.CharField(max_length=50, null=True, blank=True)
    process_typ_three = models.CharField(max_length=50, null=True, blank=True)
    salary_rang_frm = models.IntegerField(null=True)
    salary_rang_to = models.IntegerField(null=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    other_quali = models.CharField(max_length=150, null=True, blank=True)
    skills_set = models.TextField(default="", null=True)
    languages = models.TextField(default="", null=True)
    shift_timing = models.CharField(max_length=20, null=True, blank=True)
    shift_timing_frm = models.CharField(max_length=20, null=True, blank=True)
    shift_timing_to = models.CharField(max_length=20, null=True, blank=True)
    working_from = models.CharField(max_length=20, null=True, blank=True)
    working_to = models.CharField(max_length=20, null=True, blank=True)
    week_no_days = models.IntegerField(null=True, blank=True)

    week_from = models.CharField(max_length=20, null=True, blank=True)
    week_to = models.CharField(max_length=20, null=True, blank=True)

    requisition_typ = models.CharField(max_length=50, null=True, blank=True)
    candidate_name = models.TextField(default="", null=True)
    closure_date = models.DateField(null=True)
    source = models.CharField(max_length=50, null=True, blank=True)

    source_empref_emp_name = models.CharField(max_length=150, null=True, blank=True)
    source_empref_emp_id = models.CharField(max_length=20, null=True)

    source_social = models.CharField(max_length=100, null=True, blank=True)
    source_partners = models.CharField(max_length=100, null=True, blank=True)
    recruited_people = models.IntegerField(null=True, blank=True)
    request_status = models.CharField(null=True, blank=True, max_length=20, default="Pending")
    candidate_remark = models.TextField()
    status = models.BooleanField(default=False)


class EmployeeLeaveBalance(models.Model):
    emp_id = models.CharField(max_length=10,null=True)
    emp_name = models.CharField(max_length=50,null=True)
    team = models.CharField(max_length=50,null=True)
    pl_balance = models.IntegerField()
    sl_balance = models.IntegerField()
    present_count = models.IntegerField(default=0)


class LeaveTable(models.Model):

    emp_name = models.CharField(max_length=50,null=True)
    emp_id = models.CharField(max_length=50, null=True)
    emp_desi = models.CharField(max_length=50, null=True)
    emp_process = models.CharField(max_length=50, null=True)
    leave_type = models.CharField(max_length=50,null=True)
    applied_date = models.DateField(null=True,blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
    no_days = models.IntegerField()
    agent_reason = models.TextField(null=True)
    tl_approval = models.BooleanField(default=False)
    tl_status = models.CharField(max_length=50,null=True,blank=True)
    tl_reason = models.TextField(null=True)
    status=models.CharField(max_length=50, null=True)
    manager_approval = models.BooleanField(default=False)
    manager_reason = models.TextField(null=True)
    manager_status = models.CharField(max_length=50, null=True, blank=True)

    emp_rm1 = models.CharField(max_length=50, null=True)
    emp_rm2 = models.CharField(max_length=50, null=True)
    emp_rm3 = models.CharField(max_length=50, null=True)


class AgentActiveStatusHist(models.Model):
    emp_id = models.CharField(max_length=20,null=True,blank=True)
    emp_name = models.CharField(max_length=30,null=True,blank=True)
    current_status = models.CharField(max_length=20,null=True,blank=True)
    new_status = models.CharField(max_length=20,null=True,blank=True)
    date = models.DateField()
    reason = models.TextField()
    changed_by = models.CharField(max_length=30)


class AttendanceCorrectionHistory(models.Model):
    applied_by = models.CharField(max_length=30,null=True,blank=True)
    applied_by_id = models.CharField(max_length=30,null=True,blank=True)
    applied_date = models.DateField()
    date_for =  models.DateField()
    att_old = models.CharField(max_length=30,null=True,blank=True)
    att_new = models.CharField(max_length=30,null=True,blank=True)
    emp_name = models.CharField(max_length=30,null=True,blank=True)
    emp_id = models.CharField(max_length=30,null=True,blank=True)
    approved_by = models.CharField(max_length=30,null=True,blank=True)
    status = models.BooleanField(default=False)
    cal_id = models.IntegerField()
    hr_response = models.CharField(max_length=30,default='Pending by HR')
    comments = models.TextField(null=True,blank=True)
    reason = models.TextField(null=True,blank=True)





