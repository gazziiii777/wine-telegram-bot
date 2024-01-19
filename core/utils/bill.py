async def generate_bill(shopping):
    bill = 0
    for item in shopping:
        bill += item[-1] * item[-2]
    return bill
