john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}
 
jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}
 
required_skills = ['Python', 'JavaScript']

def has_required_skills(person,skills):
    person['skills']

print('Python' in required_skills)
print('C++' in required_skills)

list4 = [skill for skill in john['skills']] #['Python', 'JavaScript', 'C++']
list5 = [skill for skill in required_skills] #['Python', 'JavaScript']
print([skill in john['skills'] for skill in required_skills])
print(all([skill in john['skills'] for skill in required_skills]))


tasks = ["clean the kitchen", "do laundry", "pay bills"]

for i, task in enumerate(tasks, start=1):
    print(i,task)
