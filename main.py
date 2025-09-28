# MADE BY ALI.Z
import json

data = {}

# DataBase 

def save_datas():
    with open('data.json','w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)


def admin_perm(func):
    def wrapper(*args,**kwargs):
        password = input('Enter Password: ')
        if password == '123456':
            func(*args,**kwargs)
        else:
            print('Invalid Password!')
    return wrapper
        
@admin_perm
def add_student(name,cls):
    try:
        if not name in data[cls]:
            data[cls].append(name)
            save_datas()
        print('Successfuly added!')
    except:
        print('Enter valid class name!')

@admin_perm
def delete_student(name,cls):
    try:
        if name in data[cls]:
            data[cls].remove(name)
            save_datas()
        print('Successfuly deleted!')
    except:
        print('Enter valid class name!')

def show_students(cls):
    i = 1
    for name in data.get(cls,[]):
        print(f'{i}. {name}')
        i += 1

def show_datas():
    i = 1
    for cls in data:
        for j in data[cls]:
            print(f'{i}. {j}')
            i += 1
        

def show_menu():
    while True:
        print(f'''
            ******************
            1 - Show Students.
            2 - Add Student.
            3 - Delete Student.
            4 - Show all database.
            5 - Exit Menu.
            ******************
        ''')
        try:
            choice = int(input('Select one number : '))
            if choice == 1:
                cls = input(f'Select one class({data.keys()}): ')
                show_students(cls)
            elif choice == 2:
                cls = input(f'Select one class({data.keys()}): ')
                name = input('Enter student name: ')
                add_student(name,cls)
            elif choice == 3:
                cls = input(f'Select one class({data.keys()}): ')
                name = input('Enter student name: ')
                delete_student(name,cls)
            elif choice == 4:
                show_datas()
            elif choice == 5:
                print('Program successfuly stop!')
                break
            else:
                print('Enter valid number!')
        except:
            print('Somethings went wrong!')

show_menu()
