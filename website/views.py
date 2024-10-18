from flask import Blueprint, render_template, request
from .reports import get_overview, get_top_developers, create_graph

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    overview = get_overview()

    top_developers = None  

    if request.method == 'POST':
        org_type = request.form.get('type') 
        top_n = request.form.get('number')  

        top_developers = get_top_developers(org_type, top_n)

    return render_template('base.html', overview=overview, top_developers=top_developers)

