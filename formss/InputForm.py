from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
	comment=StringField('Enter the comment',validators=[DataRequired()])
	submit=SubmitField('Predict')