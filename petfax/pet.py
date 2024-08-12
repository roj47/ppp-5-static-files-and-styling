from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/main")

@bp.route('/')
def index(): 
    return render_template('/main/index.html', pets=pets)

@bp.route('/<int:id>')
def showPetFacts(id): 
    pet = pets[id - 1]
    return render_template('/main/showPetFacts.html', pet=pet)