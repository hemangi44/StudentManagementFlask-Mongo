#from wtforms_alchemy import ModelForm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

from .models import DepartmentModel
from .models import StudentModel
from .models import SportModel
from .models import InfoModel

class DepartmentForm(FlaskForm):
    class Meta:
        model = DepartmentModel
        csrf = False
    deptid = IntegerField(label=('Department id'),validators=[DataRequired()])
    deptname = StringField(label=('Department name'),validators=[DataRequired()])
    #submit = SubmitField('Save Department')

class StudentForm(FlaskForm):
    class Meta:
        model = StudentModel
    rno = IntegerField(label=('Roll no'),validators=[DataRequired()])
    name = StringField(label=('Student name'),validators=[DataRequired()])
    dept = IntegerField(label=('Department id'),validators=[DataRequired()])
    submit = SubmitField('Save Student')
    

class SportForm(FlaskForm):
    class Meta:
        model = SportModel

class InfoForm(FlaskForm):
    class Meta:
        model = InfoModel