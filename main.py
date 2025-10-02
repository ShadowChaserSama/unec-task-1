# MADE BY ALI.Z
import json

data = {}
users = {}

acname = None


# DataBase 

def save_datas():
    with open('data.json','w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
    
    with open('users.json','w',encoding='utf-8') as ff:
        json.dump(users,ff,ensure_ascii=False,indent=4)

with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)

with open('users.json','r',encoding='utf-8') as ff:
    users = json.load(ff)
    

# Register and Login
def Login(name,password):
    global acname
    if name in users.keys():
        if password == users[name]['password']:
            print('You successfuly Logged!')
            acname = name
            show_menu()
        else:
            print('Wrong Password!')
    else:
        print('Wrong Name!')
    
def Register(name,password):
    global acname
    if not name in users.keys():
        users[name] = {
            "admin": 0,
            "password": password
        }
        print('You successfuly Registered!')
        save_datas()
        acname = name
        show_menu()
    else:
        print('Same account name exists in the system!')
        


def home():
    print('Welcome to Student Console App!\nPlease Login or Register and continue!')
    print('''
          **************************
          *     (1) - Login        *
          *     (2) - Register     *
          **************************
          ''')
    try:
        choice = int(input('Enter proccess number: '))
        if choice == 1:
            name = input('Enter account name: ')
            password = input('Enter account password: ')
            Login(name,password)
            #show_menu()
        elif choice == 2:
            name = input('Enter account name: ')
            password = input('Enter account password: ')
            if len(name) > 3 and len(name) <= 50 and len(password) >= 3 and len(password) <= 40:
                Register(name,password)
            else:
                print('Account name must be min 4 and max 50 character!')
        else:
            print('Enter valid number!')
    except:
        print('Something went wrong!')
        


def admin_perm(func):
    def wrapper(*args,**kwargs):
        if users[acname]['admin'] == 1:
            func(*args,**kwargs)
        else:
            print('You are not admin!')
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
        
@admin_perm
def change_student(oldname,newname,cls):
    try:
        if oldname in data[cls]:
            data[cls][data[cls].index(oldname)] = newname
            save_datas()
    except:
        print('Enter valid class name!')

def show_datas():
    i = 1
    for cls in data:
        for j in data[cls]:
            print(f'{i}. {j}')
            i += 1

def change_name(name,password):
    global acname
    if password == users[acname]['password']:
        users[name] = users.pop(acname)
        acname = name
        save_datas()
    else:
        print('You enter wrong password!')

@admin_perm
def reset_datas():
    global data
    global users
    sure = input('Are u sure about reset database(y/n): ')
    if sure == 'y':
        data = {}
        users = {}
        save_datas()
        print('Database successfuly reseted!')
    elif sure == 'n' or sure != 'y':
        pass
        

def show_menu():
    while True:
        print(f'''
            ***************************************
                    Welcome Back {acname}             
            ***************************************
            *       (1) - Show Students.          *
            *       (2) - Add Student.            *
            *       (3) - Delete Student.         *
            *       (4) - Show all database.      *
            *       (5) - Change student name.    *
            *       (6) - Exit Menu.              *
            ***************************************
            *       (9) - Change account name.    *
            *       (0) - Reset database.         *
            ***************************************
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
                cls = input(f'Select one class({data.keys()}): ')
                oldname = input('Enter current student name: ')
                newname = input('Enter new student name: ')
                change_student(oldname,newname,cls)
            elif choice == 9:
                password = input('Enter account password: ')
                name = input('Enter new name: ')
                if len(name) > 3 and len(name) <= 50:
                    change_name(name,password)
                else:
                    print('Name must be max 50 and min 4 character!')
            elif choice == 0:
                reset_datas()
                break
            elif choice == 6:
                print('Program successfuly stop!')
                break
            else:
                print('Enter valid number!')
        except Exception as e:
            print('Somethings went wrong!',e)

home()
