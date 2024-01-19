from core.db.promo_code import bill_promo


async def generate_bill(shopping, user_id):
    promo = await bill_promo(user_id)
    bill = 0
    for item in shopping:
        bill += item[-1] * item[-2]
    return [bill, int(bill * (1-float(promo[1])))]
