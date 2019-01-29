from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    quantity = StringField('quantity', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

