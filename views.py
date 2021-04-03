from flask import Flask, render_template, url_for, request, redirect

from cmsapp.models import DepartmentModel
from cmsapp.models import StudentModel
from cmsapp.models import SportModel
from cmsapp.models import InfoModel
from cmsapp.forms import DepartmentForm
from cmsapp.forms import StudentForm
from cmsapp.forms import SportForm
from cmsapp.forms import InfoForm

from cmsapp.extensions import app

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
    
@app.route('/showdept', methods=['GET'])
def showdept():
    data= DepartmentModel.query.all()
    return render_template('showdept.html',data=data )
    
@app.route('/adddept', methods=['POST','GET'])
def adddept():
    fm = DepartmentForm()
    if request.method == "POST":
        f = DepartmentForm()        
        if f.validate():
            existing_dept = DepartmentModel.query.filter(DepartmentModel.deptid == int(f.deptid.data)).first()
            if existing_dept is None:
                DepartmentModel(deptid= int(f.deptid.data), deptname = f.deptname.data).save()
                return render_template('adddept.html',fm = fm, msg= 'Department Added')
            else:                
                return render_template('adddept.html',fm = f, msg= 'Department Exists')
        else:
            return render_template('adddept.html',fm=f, msg= 'Check Errors')
    else:
        return render_template('adddept.html',fm=fm)
        
@app.route('/deletedept/<int:id>')
def deletedept(id):
    print("Inside deletedept with id ", id)
    d = DepartmentModel.query.filter(DepartmentModel.deptid == int(id)).first()
    d.remove()
    return redirect('/showdept')

@app.route('/showstudent', methods=['GET'])
def showstudent():
    data=StudentModel.query.all()
    return render_template('showstudent.html',data=data)

@app.route('/addstudent', methods=['POST','GET'])
def addstudent():
    fm=StudentForm()
    if request.method=="POST":
        f= StudentForm()
        if f.validate():
            existing_student = StudentModel.query.filter(StudentModel.rno == int(f.rno.data)).first()
            if existing_student is None:
                existing_dept = DepartmentModel.query.filter(DepartmentModel.deptid == int(f.dept.data)).first()
                if existing_dept is None:
                    return render_template('addstudent.html',fm = f, msg = 'Department does not exists')
                StudentModel(rno = int(f.rno.data) , name = f.name.data, dept = existing_dept).save()
                return render_template('addstudent.html',fm = fm, msg = 'Record saved')
            else:
                return render_template('addstudent.html',fm = f, msg = 'Student exists')
        else:
            return render_template('addstudent.html',fm = f, msg = 'Check errors')
    
    else:
        return render_template('addstudent.html',fm = fm )


@app.route('/deletestudent/<int:id>', methods=['GET'])
def deletestudent(id):
    d = StudentModel.query.filter(StudentModel.rno == int(id)).first()
    d.remove()
    return redirect('/showstudent')

# @app.route('/showsport', methods=['GET'])
# def showsport():
#     data = SportModel.objects.all()
#     final_data = []
#     for d in data:
#         sportstudent = d.student.all()
#         for student in sportstudent:
#             tempdict = {
#                 "sportid" : d.sportid,
#                 "name": d.sportname,
#                 "studentname": student.name
#             }
#             final_data.append(tempdict)
#     return render_template('showsport.html',{'data':final_data})

# @app.route('/addsport', methods=['POST'])
# def addsport():
#     if request.method=="POST":
#         f= SportForm(request.POST)
#         if f.is_valid():
#             f.save()
#             fm=SportForm()
#             return render_template('addsport.html',{'fm':fm,'msg':'Record saved'})
        
#         else:
#             return render_template('addsport.html',{'fm':f,'msg':'Check errors'})
    
#     else:
#         fm=SportForm()
#         return render_template('addsport.html',{'fm':fm})
        
# @app.route('/deletesport/<int:id>', methods=['GET'])
# def deletesport(request,id):
#     d= SportModel.objects.get(sportid=id)
#     d.delete()
#     return redirect('showsport')

# @app.route('/showinfo', methods=['GET'])
# def showinfo():
    
#     data = InfoModel.objects.all()
#     final_data = []
#     for d in data:
#         tempdict = {
#             "rollno":d.student.rno,
#             "studentname": d.student.name,
#             "mobile" : d.mobile,
#             "address": d.address
#             }
#         final_data.append(tempdict)
#     return render_template('showinfo.html',{'data':final_data})

# @app.route('/addinfo', methods=['POST'])
# def addinfo():
#     if request.method=="POST":
#         f= InfoForm(request.POST)
#         if f.is_valid():
#             f.save()
#             fm=InfoForm()
#             return render_template('addinfo.html',{'fm':fm,'msg':'Record saved'})
        
#         else:
#             return render_template('addinfo.html',{'fm':f,'msg':'Check errors'})
    
#     else:
#         fm=InfoForm()
#         return render_template('addinfo.html',{'fm':fm})

# @app.route('/deleteinfo/<int:id>', methods=['GET'])
# def deleteinfo(request,id):
#     d= InfoModel.objects.get(info=id)
#     d.delete()
#     return redirect('showinfo')

if __name__ == '__main__':
    app.run(debug=True)