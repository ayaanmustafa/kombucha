from flask import (render_template, url_for, flash, redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from kombucha import db
from kombucha.models import Entry
from kombucha.posts.forms import PostForm, FirstFerm



posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods = ["POST", "GET"])
@login_required
def new_post():
    form = FirstFerm()
    if form.validate_on_submit():
        post = Entry(ident=form.ident.data, startdate=form.startdate.data, notes=form.notes.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Entry')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm() 
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post Updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == "GET":
        #fills in the empy boxes with what the user already typed in, ready to be edited
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legned='Update Post')
    

@posts.route("/post/<int:post_id>/delete", methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted', "success")
    return redirect(url_for('main.home'))
