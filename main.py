from pyfiglet import Figlet
from termcolor import colored, cprint

all_users = []
money = []
loan_taken = {}
#ln = loan
class Starting_money:
  def add_user(num_of_players):

    for i in range(num_of_players):

      name = input(colored("Enter the name of the player: ","blue")).upper() # .upper() is used to make the name of the user in lower case
      all_users.append(name) # appending the name of the user to the list   
  def add_money(num_of_players):

    for i in range(num_of_players):  # num_of_players is the number of players in the game

      money.append(1500)         # adding money to the index of players in another array 
  def generate_loan_dict():

    for i in range(len(all_users)): # len(all_users) is the number of players in the game

      loan_taken[all_users[i]] = 0 # adding the loan taken to the dictionary
class main_bank:
  def __init__(self, pot=0):
    self.pot = pot
  def transfer_money(self, user_to_deduct_from, user_to_add_from, amount):
    to_user_name_index = all_users.index(user_to_add_from)  
    from_user_name_index = all_users.index(user_to_deduct_from)
    money[to_user_name_index] += amount
    money[from_user_name_index] -= amount
    cprint(f"Successfully transferblue ${amount}",'blue')
    cprint(f"{user_to_add_from} has ${money[to_user_name_index]} after the transaction",'blue')
    cprint(f"{user_to_deduct_from} has ${money[from_user_name_index]} after the transaction",'blue')
  def remove_money(self, user, amt_to_rmv):
    user_name_index = all_users.index(user) #index of the user to deduct from
    money[user_name_index] -= amt_to_rmv #deducting the amount from the user to deduct from
    cprint("Money removed successfully","cyan") #printing the amount removed
    cprint(f"{user} has ${money[user_name_index]} left","blue") #printing the balance of the user to deduct from
  def take_loan(self, user, amt_to_take_ln, num_of_rounds):
    user_name_index = all_users.index(user) #index of the user to take loan from
    money[user_name_index] += amt_to_take_ln #adding the amount to the user to take loan from 
    loan_taken[user] = amt_to_take_ln  + num_of_rounds * 100 #adding the loan taken to the dictionary
    cprint("Money added successfully","blue") #printing the amount added
    cprint(f"Current balance of {user}: "+ str(money[user_name_index]),"blue") #printing the balance of the user to take loan from
    cprint(f"{user} will have to pay ${loan_taken[user]} to end the loan","blue") #printing the loan taken from the dictionary
  def add_money(self, user, amt_to_add):#2 inputs
    user_name_index = all_users.index(user) #index of the user to add money to
    money[user_name_index] += amt_to_add #adding the amount to the user to add money to
    cprint("Money added successfully","blue") #printing the amount added
    cprint(f"Current balance of {user} is "+ str(money[user_name_index]),"cyan") #printing the balance of the user to add money to#2 inputs
  def pay_loan(self,user, amt_to_pay_ln):
    user_name_index = all_users.index(user)#amount to pay loan
    loan_taken[user] = loan_taken.get(user) - ammount_to_pay_loan
    money[user_name_index] -= ammount_to_pay_loan #deducting the loan taken from the dictionary
    cprint(f"{user} will have to pay ${loan_taken[user]}","cyan") #printing the loan taken from the dictionary
    cprint(f"Current balance of {user}: " + str(money[user_name_index]),"blue") #printing the balance of the user to pay loan
  def show_money(self):
    for i in range(len(all_users)):
      cprint(f"{all_users[i]} has ${money[i]}","blue")
  def show_all_loans(self):
    cprint("The following users has these loans: ","blue")
    for i in range(len(all_users)):
      if all_users[i] in loan_taken:
        cprint(f"{all_users[i]} has taken a loan of ${loan_taken[all_users[i]]}","cyan")
  def transfer_to_pot(self, user, amt):#
    self.pot += amt
    from_user_name_index = all_users.index(user)
    money[from_user_name_index] -= amt
  def get_pot(self, user):#1 input
    pot = self.pot
    amount = pot
    index_name = all_users.index(user)
    pot = 0
    money[index_name] += amount
if __name__ == "__main__":
  main_bank = main_bank()
  f = Figlet(font='standard')
  print(colored(f.renderText('WELCOME TO MONOPOLY BANK ONLINE!!'), 'blue'))
  cprint("Docs For the Bank Manager is at https://pmdev.in/docs/bank_manager.html",'blue')
  number_of_playing_players = int(input(colored("Enter the number of people who will play the game: ","cyan")))
  Starting_money.add_user(number_of_playing_players)
  Starting_money.add_money(number_of_playing_players)
  Starting_money.generate_loan_dict()
  while True:
    cprint("Check Balance Of Players: 1","green")
    cprint("Take Turn: 2","red")
    cprint("Show All Loans: 3","blue")
    cprint("End Game: 4","yellow")
    try:
      dooption = int(input("Enter the option you want to do: "))     
    except KeyboardInterrupt:
      continue
    except ValueError:
      continue
    if dooption == 1:
      main_bank.show_money()
    elif dooption == 2:
      cprint("1. Pay Rent",'yellow')
      cprint("2. Buy Property Or Houses/Hotels, pay taxes (subtract it)","blue")
      cprint("3. Add Money(Pass Go, Comunity Chest, or Chance)","red")
      cprint("4. Pay Loan","green")
      cprint("5. Take Loan","yellow")
      cprint("6. Show All Loans","blue")
      cprint("7.Pay Pot","red")
      cprint("8.Get Pot!", "green")
      cprint("9. Return To Main Menu","white")
      try:
        option = input(colored("Enter the activity you want to do: ","blue"))
      except KeyboardInterrupt:
        continue
      except ValueError:
        continue
      if option == "1":
        try:
          user_to_deduct_from = input(colored("Enter the name of the user to deduct from: ","blue")).upper()
          user_to_add_from = input(colored("Enter the name of the user to add to: ","blue")).upper()
          amount = int(input(colored("Enter the amount to transfer: ","blue")))
          main_bank.transfer_money(user_to_deduct_from,user_to_add_from, amount)
        except KeyboardInterrupt:
          cprint("PLEASE TRY AGAIN","red")
          continue
        except ValueError:
          cprint("ERROR, PLAESE ENTER A VALID OPTION","red")
          continue
      elif option == "2":
        try:
          user = input(colored("Enter the name of the user to deduct from: ","blue")).upper()
          amt_to_rmv = int(input(colored("Enter the amount to remove from the user: ","blue")))
          main_bank.remove_money(user, amt_to_rmv)
        except KeyboardInterrupt:
          cprint("PLEASE TRY AGAIN","red")
          continue
        except ValueError:
          cprint("ERROR, PLAESE ENTER A VALID OPTION","red")
          continue
      elif option == "3":
        try:
          user = input(colored("Enter the name of the user who will add money: ","blue")).upper()
          amt_to_add = int(input(colored("Enter the amount to be add: ","blue")))
          main_bank.add_money(user, amt_to_add)
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
          continue
      elif option == "4":
        try:
          user = input(colored("Enter the name of the user who will pay the loan : ","cyan")).upper() 
          amt_to_pay_ln = int(input(colored("Enter the amount of the loan you wanna pay: ","blue")))
          main_bank.pay_loan(user, amt_to_pay_ln)
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
          continue
      elif option == "5":
        try:
          user = input(colored("Enter the name of the user who will take the loan : ","blue")).upper()
          amt_to_take_loan = int(input(colored("Enter the amount to take loan: ","blue")))
          no_of_rounds = int(input(colored("Enter the number of rounds in which you will repay loan: ","blue")))
          main_bank.take_loan(user, amt_to_take_loan, no_of_rounds)
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
          continue
      elif option == "6":
        try:
          main_bank.show_all_loans()
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
          continue
      elif option == "7":
        try:
          user = input(colored("Enter the name of the user to deduct from: ","blue")).upper()
          amount = int(input(colored("Enter the amount to transfer: ","blue")))
          main_bank.transfer_to_pot(user, amount)
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
          continue
      elif option == "8":
        try:
          user = input(colored("Enter user to pay pot to:", "blue")).upper()
          main_bank.get_pot(user)
        except:
          cprint("ERROR, PLEASE TRY AGAIN")
      elif option == "9":
        try:
          continue
        except:
          continue 
    elif dooption == 3:
      try:
        main_bank.show_all_loans()
      except:
        cprint("ERROR, PLEASE TRY AGAIN","red")
        continue
    elif dooption == 4:
      break