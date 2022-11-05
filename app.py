from flask import Flask, render_template
import json
import utils

with open('candidates.json', 'r') as file:
    candidates = json.load(file)

app = Flask(__name__)


@app.route('/')
def page_index():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def candidate_page(id):
    candidate_prof = utils.get_candidate(id)
    if not candidate_prof:
        return "Кандидата с таким id нет в списке"
    return render_template('card.html', candidate_prof=candidate_prof)


@app.route('/search/<candidate_name>')
def candidate_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skill/<skill_name>')
def search_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)


app.run()
