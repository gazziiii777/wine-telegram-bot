from core.utils.bill import generate_bill


async def wine_info_str(wine_list, wine_list_info, shopping_cart, count):
    print(shopping_cart)
    return f"<b>{wine_list[count][3]}</b>\n\n<b>Артикул:</b> {wine_list[count][1]}\n<b>Производитель:</b> {wine_list[count][2]}\n<b>Цвет:</b> {wine_list_info[count][4]}\n<b>Содержание сахара:</b> {wine_list_info[count][5]}\n<b>Объем:</b> {wine_list_info[count][2]} л.\n<b>Алкоголь:</b> {wine_list_info[count][3]} %\n{f'<b>Цена:</b> <s>{wine_list[count][6]} ₽</s>' if wine_list[count][7] != 0 else f'<b>Цена:</b> {wine_list[count][6]} ₽'}\n{f'<b>🔥 Цена со скидкой:</b> {wine_list[count][7]} ₽ 🔥' if wine_list[count][7] != 0 else ''}\n--------------------------------------\n🛒 <b>Корзина</b>\n <i>{f"В корзине {shopping_cart} шт.\n На сумму: {shopping_cart * wine_list[count][7] if wine_list[count][7] != 0 else shopping_cart * wine_list[count][6]} ₽" if shopping_cart != 0 else "В крзине нет этого товара"}</i>"


async def placing_an_order(shopping, your_profile):
    bill = await generate_bill(shopping, your_profile[1])
    print(bill)
    shopping_str = f"<b>Контактные данные:</b>\nТелеграмм: @{your_profile[2]}\nФИО: {your_profile[3]}\nНомер телефона: {your_profile[4]}\nАдрес доставки: {your_profile[5]}\nПочта: {your_profile[6]}\n\n <b>Ваш заказ:</b>\n"
    for item in shopping:
        shopping_str += f"• {item[1]} - {int(item[-1]) * int(item[-2])} ₽ ({item[-2]} шт.)\n"
    shopping_str += f"\n---------------------\n{f"<b>Итог: {bill[0]} ₽</b>"if bill[0]==bill[1] else f"<s>Цена: {bill[0]} ₽</s>\n<b>🔥 Цена с учетом промокода: {bill[1]} ₽</b> 🔥"}"
    return shopping_str


async def shopping_cart_basket_str(shopping_cart_basket, count):
    return f"<b>{shopping_cart_basket[count][1]}</b>\n--------------------------------------\n<b>🛒 Корзина</b>\n<i>В корзине {shopping_cart_basket[count][3]} шт.\nНа сумму: {shopping_cart_basket[count][3] * shopping_cart_basket[count][-1]} ₽</i>"
