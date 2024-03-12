def solution(A, D):
    #loop through A to access one transaction
    acc_balance = 0
    no_monthly_transactions = {}
    value_monthly_transactons = {}
    #add each transaction to acc_balance
    for index, transaction in enumerate(A):
        acc_balance += transaction

        if transaction < 0:
            #display date in YYYYMMDD
            date = D[index].split('-')
            #define a variable month which is a slice of the date
            month = date[1]
            #create a dictionary containing the frequency of each month's card payments
            if month in no_monthly_transactions:
                no_monthly_transactions[month] += 1
            else:
                no_monthly_transactions[month] = 1
            
            #create a dictionary containing the value of card payments per month
            if month in value_monthly_transactons:
                value_monthly_transactons[month] += transaction
            else:
                value_monthly_transactons[month] = transaction
            
    #calculate no of months that will be excluded from fee
    excluded_months = 0
    #count a month as excluded if it has more than three payments with a total value less than -100, which basically is greater than 100 since payments are negative
    for key,value in no_monthly_transactions.items():
        if value >= 3 and value_monthly_transactons[key] <= -100:
            excluded_months += 1
    
    #assign a 5 to a variable for easy maintenance incase monthly fee changes
    monthly_fee = 5
    #check no of months fee charged
    months_fee_charged = 12 - excluded_months
    #calculate total fees charged in that year
    total_fee = monthly_fee * months_fee_charged

    #subtract total fees charged on the account from account balance to get the final balance
    final_balance = acc_balance - total_fee
    print (final_balance)
    return final_balance

solution([100, 100, 100, -10], ["2020-01-01", "2020-12-22", "2020-12-03", "2020-12-29"])
solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"])
solution([])    