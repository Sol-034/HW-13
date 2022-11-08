#ДАННЫЕ
#Цены билетов и размер скидки
percent_discount = 10

total_price_tickets = 0
half_price_ticket = 990
full_price_ticket = 1390

#Список возрастов посетителей
ages_visitors = []


#ОСНОВНОЙ АЛГОРИТМ
# Узнаём, сколько билетов нужно
count_tickets = int(input("Сколько билетов хотите купить?:\n"))

# Узнаём возраст каждого посетителя
for i in range(1, count_tickets+1):
    ages_visitors.append(int(input(f"Билет №{i} - Введите возраст посетителя:\n")))

# Рассчитываем итоговую стоимость с учётом возраста
for age in ages_visitors:
    if 18 <= age < 25:
        total_price_tickets += half_price_ticket
    elif age >= 25:
        total_price_tickets += full_price_ticket

# Рассчитываем итоговую стоимость с учётом скидки (если билетов > 3шт)
if count_tickets > 3:
    price_tickets_with_discount = total_price_tickets * (100 - percent_discount)/100
    total_price_tickets = round(price_tickets_with_discount)

# Выводим итоговую стоимость билетов пользователю
print(f"Итого сумма к оплате: {total_price_tickets} руб")
