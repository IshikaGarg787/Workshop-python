print('----Library Management System----')


class Select():            
    def display(self):
        lst=['7 Habits of highly effective people','Atomic Habits','Harry Potter']
        print(lst)
    def request(self):
        book=input('Which book you want to borrow :')
        lst=['7 Habits of highly effective people','Atomic Habits','Harry Potter']
        if book =='7 Habits of highly effective people':
           lst=lst.remove('7 Habits of highly effective people')
           print('You have borrowed a book')
        elif book=='Atomic Habits':
            lst=lst.remove('Atomic Habits')
            print('You have borrowed a book')
        elif book=='Harry Potter':
            lst=lst.remove('Harry Potter')
            print('You have borrowed a book')
        else:
            print('book not present')
            

    def return_book(self):
        book=input('Which book you want to return :')
        lst=['7 Habits of highly effective people','Atomic Habits','Harry Potter']
        if book =='7 Habits of highly effective people':
           lst=lst.append('7 Habits of highly effective people')
           print('You have returned a book')
        elif book=='Atomic Habits':
            lst=lst.append('Atomic Habits')
            print('You have returned a book')
        elif book=='Harry Potter':
            lst=lst.append('Harry Potter')
            print('You have returned a book')
        else:
            print('book not of this library') 
    def exit_code(self):
        print("thankyou!!") 


class Library (Select):
    def choose(self):
      while True:  
        print('Press 1 to Display all available Books')
        print('Press 2 to request a book')
        print('Press 3 to return a book')
        print('Press 4 to Exit')
        choice=input('Enter your choice :')
        if choice=='1':
            obj=Library()
            obj.display()
        elif choice=='2':
            obj1=Library()
            obj1.request()
        elif choice=='3':
            obj2=Library()
            obj2.return_book()
        elif choice=='4':
            obj3=Library()
            obj3.exit_code()
            break
        else:
            print('Invalid Input')  
               

obj_h=Library()
Library.choose('2')