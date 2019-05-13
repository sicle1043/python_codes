def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + '.')
    print('\nMy ' + animal_type + "'s name is " + pet_name.title() + '.')


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回格式化后的姓名，参数有两个，first_name是名，last_name是姓"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


def print_models(unprinted_designs, completed_models):
    unprinted_designs.reverse()
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing: model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for completed_models in completed_models:
        print(completed_models)


describe_pet(pet_name='popy', animal_type='dog')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'hooker')
print(musician)

unprinted_designs = ['iphone case', 'robot pendannt', 'dpdecahedron']
completed_models = []
abc = unprinted_designs[:]
print_models(unprinted_designs, completed_models)  # unprinted_designs[:]列表的复制
show_completed_models(completed_models)
print(abc)