from flask import Blueprint, render_template, request
from .reports import get_overview, get_top, get_total, get_slice

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    overview = get_overview()
    top_results = None  
    total_results = None
    total_slice = None

    if request.method == 'POST':

        group_by_col = request.form.get('group_by_col') 
        aggregation_col = request.form.get('aggregation_col_drill')  
        dim_table = request.form.get('table_selection')

        group_by_column1 = request.form.get('group_by_col1') 
        aggregation_column1 = request.form.get('aggregation_col_rollup')
        dim_table1 = request.form.get('table_selection1')

        property = request.form.get('property') 
        filter =request.form.get('filter') 

        # Retrieve top developers or publishers
        if group_by_col and aggregation_col and dim_table:
            top_results = get_top(group_by_col, aggregation_col, dim_table)

        # Retrieve total by aggregation and group by columns
        if group_by_column1 and aggregation_column1 and dim_table1:
            total_results = get_total(group_by_column1, aggregation_column1, dim_table1)

        # Retrieve slice results
        if property and filter:
            total_slice = get_slice(property, filter)

    return render_template('base.html', overview=overview, top_results=top_results, total_results=total_results, total_slice=total_slice)
