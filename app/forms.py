from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, RadioField, FileField

from wtforms.validators import Required, Email

class NewProfileForm(Form):
  username = TextField('Username', validators=[Required()])
  email = TextField('Email', validators=[Required(), Email()])
  image = FileField('Image', validators=[Required()])
  fname = TextField('First Name', validators=[Required()])
  lname = TextField('Last Name', validators=[Required()])
  age = IntegerField('Age', validators=[Required()])
  sex = RadioField('Sex', choices=[('Male','Male'),('Female','Female')], validators=[Required()])
