from flask import render_template, flash, redirect, url_for, abort, request
#from werkzeug.wrappers import request
from newsletter import app, db
from newsletter.forms import LoginForm, PostForm #RegisterForm #TODO
from newsletter.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('newsletter_list.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Logged in succesfully', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Logged unsuccesfull', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data, user=current_user)
            db.session.add(post)
            db.session.commit()
            flash(f'News content has been created.', 'success')
            return redirect(url_for('index'))
    return render_template('create_post.html', title='Create New Post', form=form)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='post.title', post=post)


@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Post edited', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        return render_template('create_post.html', title='Edit Post', form=form)


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Post deleted', 'success')
    return redirect(url_for('index'))