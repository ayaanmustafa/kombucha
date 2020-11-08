from flask import render_template, request, Blueprint
from flask_login import current_user, login_required

from kombucha.models import Entry

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    #Post only logged in user data?
    #type=int makes an error if someone tries to open a page with a non int, 1 is default
    # page = request.args.get('page', 1, type=int)
    entry = Entry.query.order_by(Entry.ident.desc())
    return render_template('home.html', entrys=entry)

@main.route("/about")
def about():
    return render_template('about.html', title='About')


