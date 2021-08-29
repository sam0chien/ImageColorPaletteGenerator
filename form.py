from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField


class PaletteForm(FlaskForm):
    image = FileField('Image to upload')
    number = IntegerField('Number of color', default=10, validators=[DataRequired(), NumberRange(min=0, max=30)])
    submit = SubmitField('Run')
