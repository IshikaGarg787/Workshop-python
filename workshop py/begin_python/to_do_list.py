todos=[]
while True:
    user_input=input('Type add, show, edit , complete or exit :').lower()
    match user_input:
        case 'add':
            todo=input('Enter the to-do :')+'\n'
            todos.append(todo)
        case 'show'|'display':
            if todos==[]:
                print('Enter something to the list :')
            else:    
                count = 1
                for user_input in todos:
                    print(f"{count}. {user_input}")
                    count += 1
            #for index,item in enumerate{}:
                #print(f'{index+1}-{item}')
        case 'edit':
          if todos==[]:
             print('Enter something to the list :')
          else:
            number=int(input('Enter the number you want to edit :')) 
            number -= 1
            new_to_do=input('Enter the new to-do :')
            todos[number]=new_to_do
        case 'complete':
            number=int(input('Enter the number of to-do completed :'))
            number -= 1
            todos.pop(number)
        case 'exit':
            todos.clear()
            print('Bye!!') 
            break
        case _:
            print('invalid input')
               
