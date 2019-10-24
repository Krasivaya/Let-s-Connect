from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField
from wtforms.validators import Required

class CreatePost(FlaskForm):
    title = StringField('Article Title',validators=[Required()])
    content = TextAreaField('Article Content',validators=[Required()])
    submit = SubmitField('Post')