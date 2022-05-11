from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post = TextAreaField('Your Pitch', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = StringField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment') 

class UpvoteForm(FlaskForm):
    submit = SelectField('Like')