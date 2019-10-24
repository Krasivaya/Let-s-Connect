from flask import render_template,redirect,url_for,flash
from app.main import main
from .forms import CreatePost
from .. import db
from flask_login import login_required,current_user


@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_post():
    form = CreatePost()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user._get_current_object().id
        post = Post(title=title,content=content,user_id=user_id)
        Post.save()
        return redirect(url_for('main.index'))
        flash('You have posted a new Article')
    return render_template('newpost.html', form = form)