from flask_wtf import FlaskForm
from wtforms import StringField ,SelectField
from wtforms.validators import DataRequired ,Email
from wtforms.widgets import TextArea
from flask_wtf.file import FileField,FileRequired,FileAllowed


class  ProfileForm(FlaskForm):
	FirstName = StringField('First Name',validators=[DataRequired()])
	LastName = StringField('Last Name',validators=[DataRequired()])
	Gender = SelectField(label='Gender',validators=[DataRequired()],choices=[('Male','Male'),('Female','Female')])
	Email = StringField('Email',validators=[DataRequired(), Email()])
	Location = StringField('Location',validators=[DataRequired()])
	Biography  = StringField('Biography',validators=[DataRequired()],widget=TextArea())
	photo=FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png'])])
 