#Q.1
string=input('Enter string: ').strip(',')
def min_removals_to_equal_frequency(string: str) -> int:
    letters={}
    for letter in string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    freq_of_freq = {}
    for freq in letters.values():
        if freq in freq_of_freq:
            freq_of_freq[freq] += 1
        else:
            freq_of_freq[freq] = 1
    if len(freq_of_freq) == 1:
        return 0
    common_freq=min(letters.values())
    number_of_removed=0
    for num in letters.values():
        if num>common_freq:
            number_of_removed+=num-common_freq
        elif num==1:
            number_of_removed=1
        
    return number_of_removed

print(min_removals_to_equal_frequency(string))

# # #Q.2 
n = int(input('Enter number of scores: '))
def manage_scoreboard(rounds: list[tuple[int, int]]) -> dict:
    scoreboard={}
    for player , score in rounds:
        if player in scoreboard:
                 scoreboard[player] += score
        else:
            scoreboard[player] = score
    return scoreboard
rounds = []
for i in range(n):
    player, score = map(int, input('Enter player and score (comma-seperated): ').split(','))
    rounds.append((player, score))


total_score = manage_scoreboard(rounds)
print(total_score)

# # #Q.3
list_of_numbers = list(map(int, input('Enter list of numbers (comma-separated):').split(',')))
number_to_remove = int(input('Enter the number you want to remove: '))
def remove_occurrences(list_of_numbers: list[int],number_to_remove: int) -> list[int]:
    result = []
    for n in list_of_numbers:
        if n != number_to_remove:
            result.append(n)
    return result
print(f'{remove_occurrences(list_of_numbers,number_to_remove)}')

#Q.4
#contact mangement system
def add(contacts,name,number):
    if name in contacts:
        print(f'The contact with the name: {name} already exists.')
    else:
        contacts[name]=number
        print(f'the contact with the name: {name} and number: {number} has been added succefuly.')

def delete(contacts,name):
    if name in contacts:
        del contacts[name]
        print(f'the contact {name} has been deleted succefully.')
        return True
    else:
        print(f'the contact {name} does not exist.')

def search(contacts,name):
    if name in contacts:
        print(f'the name:{name} has been found😊')
        return True  
    else:
        print(f'the name:{name} has been not been found😟')
        return False
    

def view(contacts,name,number):
    if contacts:
        print("All Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number:+ {number}")
        return True
    else:
        print("No contacts available.")
        return False
            
    
def update(contacts,name,phone):
   if name in contacts:
        contacts[name] = phone
        print(f"The contact {name} is updated with the new number {phone} succefully.")
        return True
   else:
        print(f"Contact with the name: {name} does not exist.")
        return False
   

   
contacts={}
while True:
    print('Welcome to the✨Contact Managment System✨')
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. View Contacts")
    print("5. Update Contact")
    print("6. Exit")
    feature=int(input('enter a number from(1-6) to select a feature: '))
    if feature==1:
        name=input('enter the name you want to add: ')
        number=input('enter the number:+ ')
        add(contacts,name,number)
    elif feature==2:
         name=input('enter the name u want to delete: ')
         delete(contacts,name)
    elif feature==3:
        name=input("Enter the name you want to search for:")
        search(contacts,name)
        
    elif feature == 4:
        if contacts: 
            view(contacts,name,number) 
        else:
            print('No contacts available') 
       
    elif feature==5:
        name=input('enter the name you want to update its number: ')
        number=input('enter new number:+ ')
        update(contacts,name,number)
    elif feature==6:
        print('Leaving...😄')
        break
    else:
        print('Invalid Choice')





    
    
