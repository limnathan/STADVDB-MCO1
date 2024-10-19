from flask import Blueprint, render_template, request
from .reports import get_overview, get_top_developers, get_total

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    overview = get_overview()
    top_developers = None  
    total_results = None

    if request.method == 'POST':
        org_type = request.form.get('type') 
        top_n = request.form.get('number')  
        group_by_column = request.form.get('group_by_col') 
        aggregation_column = request.form.get('aggregation_col')
        dim_table = request.form.get('table_selection')

        # Retrieve top developers or publishers
        if org_type and top_n:
            top_developers = get_top_developers(org_type, top_n)

        # Retrieve total by aggregation and group by columns
        if aggregation_column and group_by_column and dim_table:
            total_results = get_total(group_by_column, aggregation_column, dim_table)

    return render_template('base.html', overview=overview, top_developers=top_developers, total_results=total_results)
