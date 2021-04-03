from .extensions import db

# Create your models here.
class DepartmentModel(db.Document):
    deptid=  db.IntField()
    deptname=  db.StringField()
    
    def __str__(self):
        return self.deptname

class StudentModel(db.Document):
    rno=  db.IntField()
    name=  db.StringField()
    dept= db.DocumentField(DepartmentModel)
    
    def __str__(self):
        return self.name

class SportModel(db.Document):
    sportid=  db.IntField()
    sportname=  db.StringField()
    student= db.DocumentField(StudentModel)
    
    def __str__(self):
        return self.sportname

class InfoModel(db.Document):
    mobile= db.IntField()
    address=  db.StringField()
    student = db.DocumentField(StudentModel)
    
    def __str__(self):
        return self.mobile