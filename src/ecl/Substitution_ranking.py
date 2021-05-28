import pathlib

from ecl import Database, Recipe, RecipeFormat, Step, Substitution, import_database

# Data cleaning notes: 1. change time and complexity to number only
# 2. in items out/in column, do not include and. if there is 'or' relationship, do not include , (eg. a, b, c. a or b or c)


data_input_filepath = pathlib.Path("/Users/maggiewu/PycharmProjects/CookieMaster_1/datafile/Schema-3.2.xlsx")
database = Database()

import_database(data_input_filepath, database)


def get_substitution_steps_in(sub_id):
    """returns a list of Step_id"""
    lst = []
    for sub in database.substitution:
        if sub.id_ == sub_id:
            # return sub.steps_in
            for i in sub.steps_in:
                lst.append(i.id_)
            return lst

print('For this substitution, steps in: ',get_substitution_steps_in('subs-1'))


def get_substitution_steps_out(sub_id):
    """returns a list of Step_id"""
    lst = []
    for sub in database.substitution:
        if sub.id_ == sub_id:
            # return sub.steps_out
            for i in sub.steps_out:
                lst.append(i.id_)
            return lst

# print(get_substitution_steps_out('subs-31'))

def get_substitution_step_changes(sub_id):
    """returns a dict of delta values (complexity, time, action, qualia)"""
    for sub in database.substitution:
        if sub.id_ == sub_id:
            return sub

print('substitution number of items_in:', len(get_substitution_step_changes('subs-31').items_in))

def get_step_values(step_id):
    """get step metadata. returns a dict of 'Required items', 'Duration', 'Complexity'"""
    for step in database.step:
        if step.id_ == step_id:
            return step


# print('Step complexity', get_step_values('step-31').complexity)


def sub_score(sub_id):

    in_items_num = len(get_substitution_step_changes(sub_id).items_in)
    out_items_num = len(get_substitution_step_changes(sub_id).items_out)
    num_of_items = in_items_num - out_items_num

    steps_in = get_substitution_steps_in(sub_id)
    steps_out = get_substitution_steps_out(sub_id)
    in_score, out_score = 0, 0
    for step in steps_in:
        if "MISMATCH" in step:
            in_score += 0
        else:
            in_score += get_step_values(step).complexity
    for step in steps_out:
        if "MISMATCH" in step:
            in_score += 0
        else:
            out_score += get_step_values(step).complexity

    change_in_complexity = get_substitution_step_changes(sub_id).change_complexity + in_score - out_score
    time = 0
    efficacy = 0
    user_rating = 0

    score_ = num_of_items + change_in_complexity + time + efficacy + user_rating
    return score_


print('sub-31 score is: ', sub_score('subs-31'))


def find_substitutions(recipe_name, desired_qualia, sub_ids=None):
    """return a list of substitution IDs"""
    lst = []
    for s in database.substitution:
        if recipe_name in s.scope:
            if recipe_name =='choc chip cookies':
                if desired_qualia in [q.qualia[0] for q in s.change_qualia_cookie]:
                    lst.append(s.id_)

            if recipe_name == 'pancakes':
                if desired_qualia in s.change_qualia_pancake:
                    lst.append(s.id_)

            if recipe_name =='brownie':
                if desired_qualia in s.change_qualia_brownie:
                    lst.append(s.id_)

            if recipe_name =='cupcakes':
                if desired_qualia in s.change_qualia_cupcake:
                    lst.append(s.id_)

    return lst

print('Find substitutions by given scope and qualia:', find_substitutions('choc chip cookies', 'nutty'))


def rank_substitutions(recipe_name, desired_qualia):
    sub_ids = find_substitutions(recipe_name, desired_qualia)
    sub_keys = sub_ids
    sub_values = list(map(sub_score, sub_ids))
    sub_dict = {sub_keys[i]: sub_values[i] for i in range(len(sub_keys))}

    sorted_dict = dict(sorted(sub_dict.items(), key=lambda item: item[1]))
    return list(sorted_dict.keys())

print("Optimized rank: ", rank_substitutions('choc chip cookies', 'nutty'))
