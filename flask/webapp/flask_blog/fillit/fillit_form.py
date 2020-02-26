import flask_wtf
import wtforms
from wtforms.validators import DataRequired, NumberRange

class FillitForm(flask_wtf.FlaskForm):
    nb_element = wtforms.IntegerField('tetriminos (max 13)', [DataRequired(), 
												NumberRange(
													min=1,
													max=13, 
													message="nb of tetriminos should be between 1 and 26")])
    submit = wtforms.SubmitField('Make Grid')
