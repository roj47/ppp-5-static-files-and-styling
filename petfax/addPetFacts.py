from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/details")

@bp.route('/addPetFacts')
def addPetFacts(): 
    return render_template('details/addPetFacts.html')