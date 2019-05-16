from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PayForm(FlaskForm):
    phone 		 = StringField('Enter Phone (e.g254700000023)', validators=[DataRequired()])
    amount 		 = StringField('Enter Amount', validators=[DataRequired()])

    submit = SubmitField('Pay')

