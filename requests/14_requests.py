import requests

"""
{
    1:11,
    2:15
    ..
}
"""

site = (requests.get("https://jsonplaceholder.typicode.com/todos"))
tasks = site.json()

"""#{'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}"""

from collections import defaultdict


def get_users_to_score_dict(task):
    # tasks_completed_by_user = dict()
    tasks_completed_by_user = defaultdict(int)
    for entry in tasks:
        if (entry["completed"] == True):
            # try:
            tasks_completed_by_user[entry["userId"]] += 1
        # except KeyError:
        #     tasks_completed_by_user[entry["userId"]] = 1
    return tasks_completed_by_user


def get_users_with_max_score(tasks_completed_by_user):
    users_with_max_score = set()
    max_score = max(tasks_completed_by_user.values())
    for user_id, score in tasks_completed_by_user.items():
        if (score == max_score):
            users_with_max_score.add(user_id)
    return users_with_max_score


# https://jsonplaceholder.typicode.com/users?id=5&id=10
def change_set_into_conjunction_of_parameters(users, paramName="id"):
    last_iteration = len(users)
    i = 0
    result = paramName + "="
    for user_id in users:
        i += 1
        if (i == last_iteration):
            result += str(user_id)
        else:
            result += str(user_id) + "&" + paramName + "="
    return result


tasks_completed_by_user = get_users_to_score_dict(tasks)
max_scored_users = get_users_with_max_score(tasks_completed_by_user)

# first method:
users = (requests.get("https://jsonplaceholder.typicode.com/users")).json()
for user in users:
    if (user["id"] in max_scored_users):
        print("Wreczam ciasteczko mistrzunia dyscypliny ", user["name"])
# second_method
for user_id in max_scored_users:
    name = requests.get("https://jsonplaceholder.typicode.com/users/" + str(user_id)).json()["name"]
    print("Wreczam ciasteczko mistrzunia dyscypliny ", name)
# second best method
# https://jsonplaceholder.typicode.com/users?id=5&id=10
params = change_set_into_conjunction_of_parameters(max_scored_users)
users3 = requests.get("https://jsonplaceholder.typicode.com/users?" + params).json()
for user in users3:
    print("Wreczam ciasteczko mistrzunia dyscypliny " + user["name"])
