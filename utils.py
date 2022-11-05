import json


def load_candidates_from_json():
    with open('candidates.json', 'r') as file:
        return json.load(file)


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    cand_result = []
    for candidate in load_candidates_from_json():
        if candidate_name == candidate['name']:
            cand_result.append(candidate)
    return cand_result


def get_candidates_by_skill(skill_name):
    result = []
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
