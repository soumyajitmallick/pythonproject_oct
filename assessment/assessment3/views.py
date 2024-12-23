from django.shortcuts import render

# Create your views here.

from . models import employee , leave_apply , leave_Master, leave_emp_assign

def leave_apply ( request ) :
    empls = employee . objects . all ()
    leaves = leave_emp_assign . objects . all ()
    msg = None
    if request.method == 'POST' :
        emp_id = request . POST [ 'emp_id' ]
        leave_type = request.POST ['leave_type']
        no_of_apply_leave = int ( request.POST ['no_of_apply_leave'] )
    try :
        emp_id = employee . objects . get ( emp_id = emp_id )
        leave_id = leave_Master . objects . get ( leave_name = leave_type )
        leave_emp_id = leave_emp_assign . objects . get ( emp_id = emp_id , leave_id= leave_id )
        lobj = leave_apply ( emp_id = emp_id, leave_emp_id= leave_emp_id, no_of_apply_leave=no_of_apply_leave )
        lobj . save ()
        msg = 'Leave Applyed Success'
    except Exception as obj :
        msg = f'Leave Applyed Failed - {obj}'
    return render ( request , 'leave_apply.html' , context={'empls':empls, 'msg' : msg, 'leaves' : leaves})