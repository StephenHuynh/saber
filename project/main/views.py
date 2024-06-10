# IMPORTS
from flask import render_template, Blueprint, redirect, url_for, flash, request, current_app
from ..extensions import db
from .forms import ContactForm
from .models import Contact
from ..utils.email_func import send_email 

# CONFIG
main_bp = Blueprint('main', __name__)

# ROUTES
@main_bp.route('/', methods=['GET', 'POST'])
# @main_bp.route('/index', methods=['GET', 'POST'])
def index():
    sender = current_app.config.get("MAIL_DEFAULT_SENDER")
    form = ContactForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_order = Contact(full_name=form.full_name.data, email=form.email.data, 
                                mobile=form.mobile.data, note=form.note.data)
            
            db.session.add(new_order)
            db.session.commit()
            message = f"Cám ơn, {form.full_name.data}. Yêu cầu đặt hàng đã được gửi. Chúng tôi sẽ liên lạc lại trong thời gian sớm nhất."
            flash(message, 'success')
            send_email("[SABER] Yêu cầu đặt hàng", 
                       sender, ["Stephen.Huynh@gmail.com"], [form.email.data], 
                       form.note.data)                
            return redirect(url_for('main.index'))
            
    return render_template('index.html', form=form)

@main_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main_bp.app_errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403
