def solution(A, D):
    # Initialize variables
    balance = 0
    card_payments = {}  # {month: count}

    # Process transactions
    for i in range(len(A)):
        amount = A[i]
        date = D[i]
        year, month, _ = date.split('-')

        # Update card payments
        if amount < 0:
            card_payments.setdefault(month, 0)
            card_payments[month] += 1

        # Add incoming transfers to balance
        else:
            balance += amount

    # Deduct card fees
    for month, count in card_payments.items():
        if count >= 3:
            continue  # No fee if criteria met
        if balance >= 100:
            balance -= 5
        else:
            balance -= min(5, balance)  # Deduct fee (up to balance)

    return balance

# Example usage
A = [100,]
D = ["2020-01-01","2020-01-01","2020-01-01","2020-01-31"]
print(solution(A, D))  # Expected output: 

       