#initial balance
initial_bal = int(input("Enter Balance : "))

#Number of taranscations
n = int(input("Enter number of transcations you want : "))
print("Enter withdrawal  amount")

#Collect withdrawal amount
lst = [int(input()) for i in range(n)]

def withdrawal(balance, lst):
    """
    Parameters
    ----------
    balance : float
        Initial account balance.

    lst : list of int
        List of withdrawal amounts.

    Returns
    -------
    result_lst : list of bool
        List of boolean values where:
        - True  → transaction successful
        - False → transaction failed

    balance : float
        Current balance after processing all withdrawals.
    """
    result_lst = []
    for i in lst:
        #Check if it is multiple of 100 and balance is enough to withdraw
        if i % 100 == 0 and (balance - i) >= 0:
            result_lst.append(True)
            balance -= i
        else :
            result_lst.append(False)
            
    return result_lst, balance

result_lst, current_balance = withdrawal(initial_bal, lst)

#Print the result
for i in result_lst:
    if i : 
        print("Success")
    else : 
        print("Failed")
print(f"Balance : {current_balance}")

            