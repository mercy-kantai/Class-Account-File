class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin=pin
        self.__balance = 0
        self.status = "active"
        self.minimum_balance = 500
        self.transaction_history = []


    def show_balance(self, pin):
          if pin == self.__pin:
               return self.__balance
          else:
               return "wrong pin"


    def deposit_amount(self, deposit):
        self.__balance+= deposit
        self.transaction_history.append({"type": "deposit", "amount": deposit})
        print(f'New balance {self.__balance}')
        


    def withdrawal_amount(self, withdraw):
         if withdraw <= self.__balance - self.minimum_balance:
            self.__balance-= withdraw 
            self.transaction_history.append({"type": "withdraw", "amount": withdraw})
            print(f'New balance {self.__balance}')  



    def view_account_details(self, name):
         print(f'name: {name} ,  Accoount Number: {self.number}, Balance: {self.__balance}')


    def  change_account(self, name, number):
         print(f'Hello your new name is {name} and account number is {number}')


    def account_statement(self,date):   
         print(f'On {date} You withdrew {self.withdrawal_amount()} And deposited {self.deposit_amount()}')  
         

    def overdraft_limit(self, overdraft ):
         if self.__balance > overdraft:
              print(self.withdrawal_amount())
         else:
              print("You have insufficient balance please top up")  


    def calculate_interest(self, rate):
        interest = self.__balance * (rate / 100)
        print(interest)


    def apply_interest(self, rate):
        interest = self.calculate_interest(rate)
        self.__balance += interest
        print(f"Interest applied is {interest} New balance: {self.__balance}")    


    def freeze(self):
        self.frozen = True
        print("Account frozen.")


    def unfreeze(self):
        self.frozen = False
        print("Account unfrozen.")  
    

    def get_transaction_history(self):
         for i in self.transaction_history:
              print(f'{i['type']}: {i['amount']}')
    

    # def set_minimum_balance(self, amount):
    #     if  self.__balance - self.withdraw > amount:
    #          print(self.withdrawal_amount())
    #     else:
    #          print(f'Your withdrawal amount is beyond the set minimum balance')


    def transfer_funds(self, transfer_amount, beneficiary_account):
         if transfer_amount > self.__balance:
              print(f'You transferred {transfer_amount} to {beneficiary_account}')
         else:
              print("You have insufficient amount to transfer")

    def close_account(self):
         if self.status == 'active':
              self.status == "closed"
              print("Account is closed")
         else:
              print("Account already closed")
              

                   
             
                        
         
         
         
    


    
        

         

             



              


         
           


        