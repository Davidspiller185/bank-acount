from bank_account import BankAccount

count_1=BankAccount("Leoumi",5045)
count_2=BankAccount("bank hapoalim",8675)
print(count_1)
print(count_2)
count_1.transfer_funds(count_2,100)
print(count_1)
print(count_2)