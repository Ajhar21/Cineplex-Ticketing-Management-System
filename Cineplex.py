""" Lab Exam Project  Programmer: Ajhar Akanda"""

class Star_Cinema:
    hall_list=[]
    def entry_hall(self,Hall):
        Star_Cinema.hall_list.append(Hall)
    
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}  # key:self.id
        self.show_list=[] # list of tuples
        self._rows=rows # protected
        self._cols=cols # protected
        self.hall_no=hall_no
        super().entry_hall(self)
        self.sold_seats={}


    def entry_show(self, id, movie_name, time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        self.show_details=(self.movie_name,self.id,self.time)
        self.show_list.append(self.show_details)
        self.temp_list_seats=[ [(i,j) for j in range(self._cols)] for i in range(self._rows)]
        temp_sold_list=[]
        self.sold_seats[id]=temp_sold_list

        for row in range(len(self.temp_list_seats)):
            for col in range(len(self.temp_list_seats[row])):
                letter=chr(ord('A')+row)
                number=col+1
                self.temp_list_seats[row][col]=f'{letter}{number}'

        self.seats[self.id]=self.temp_list_seats
   
    def booK_seats(self,customer_name, phone_number, id, seats_to_book):
        self.__customer_name=customer_name # private
        self.__phone_number=phone_number  # private
        self.cust_id=id
        self.seats_to_book_list=[]  # List of tuples with rows & cols
        self.seats_to_book_list.append(seats_to_book)

        for id, seats in self.seats.items():
            if id==self.cust_id:
                for seat_group in self.seats_to_book_list:
                    for seat_tuple in seat_group:
                        for seat_row in seats:                            
                            for i in range(self._rows):
                                for j in range(self._cols):
                                    if seats[i][j]==seat_tuple:
                                        for key, value in self.sold_seats.items():
                                            if key==self.cust_id:
                                                value.append(seat_tuple)
                                        seats[i][j]='X' 

    def view_show_list(self):
        print('-----------------------------------------------------------')
        for show in self.show_list:
            print(f'Movie Name: {show[0]}       Show ID: {show[1]}       Time: {show[2]}')
        print('-----------------------------------------------------------')
    
    def view_available_seats(self, id):
        print('---------------------------------------------------------')
        for show in self.show_list:
            if show[1]==id:
                print(f'Movie Name: {show[0]}    Time: {show[2]}')
        self.show_id=id
        for id,seats in self.seats.items():
            if id==self.show_id:
                print('X for already booked seats')
                for seat_row in seats:
                    for seat_tuple in seat_row:    
                        print(seat_tuple, end='     ')
                    print()
        print('---------------------------------------------------------')


hall_1=Hall(3,4,7)
hall_1.entry_show('abc','Adam', '12:40')
hall_1.entry_show('cdf','Pathan', '1.30 pm')

print()

while True:
    print()
    print('1. View All Shows Today')
    print('2. View Available Seats')
    print('3. Book Ticket')
    print('4. Exit')
    str_option=input('Enter Option: ')
    option=int(str_option)
    if option==4:
        break
    if option==1:
        hall_1.view_show_list()

    if option==2:
        show_id=input('Enter Show ID: ')
        found_id=False
        for id in hall_1.seats:
            if show_id==id:
                found_id=True
                hall_1.view_available_seats(show_id)
                break
        if found_id==False:
            print('---------------------------------------------------------')
            print('You Entered Invalid Show ID!')
            print('---------------------------------------------------------')

    if option==3:
        name=input('Enter Your Name: ')
        phone=input('Enter Your Phone Number: ')
        show_id=input('Enter Show ID: ')
        found_id=False
        valid_call=False

        for id in hall_1.seats:

            if show_id==id:
                found_id=True
                str_num_of_tickets=input('Enter Number of Tickets: ')
                num_of_tickets=int(str_num_of_tickets)
                seat_to_book_list=[]

                for i in range(num_of_tickets):
                    seat=input('Enter Seat No: ')
                    booked_seat=False
                    found_seat=False

                    for key, list in hall_1.sold_seats.items():
                        if list==[]:
                            break
                        elif show_id==key:
                            for booked in list:
                                if seat==booked:
                                    print('---------------------------------------------------------')
                                    print(f'Seat No. {seat} Already Booked!')
                                    print('---------------------------------------------------------')
                                    booked_seat=True
                                    break
                    if booked_seat==False:
                    
                        for id,seats in hall_1.seats.items():
                            if id==show_id:
                                for seat_row in seats:
                                    for seat_tuple in seat_row: 
                                        if seat_tuple==seat:
                                            found_seat=True
                                            valid_call=True
                                            break   
                                
                        if found_seat==False:
                            print('---------------------------------------------------------')
                            print('Invalid Seat!')
                            print('---------------------------------------------------------')

                        else:
                            seat_to_book_list.append(seat)
     
                hall_1.booK_seats(name,phone,show_id,seat_to_book_list)
                break
        
        if valid_call==True:
            print('---------------------------------------------------------')
            print('********Ticket Booked Successfully*********')
            print(f'Name: {name}')
            print(f'Phone Number: {phone}')
            for show in hall_1.show_list:
                if show[1]==show_id:
                    print(f'Movie Name: {show[0]}')
                    print(f'Show Time: {show[2]}')
            print('Succesfully Booked Tickets:')
            print(seat_to_book_list)
            print('---------------------------------------------------------')
        
        if found_id==False:
            print('---------------------------------------------------------')
            print('You Entered Invalid Show ID!')
            print('---------------------------------------------------------')
        

