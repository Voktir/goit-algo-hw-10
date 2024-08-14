import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Невідомі змінні
l = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
f = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Continuous')

# Функція цілі (Максимізація прибутку)
model += l + f, "Production"

model += 2 * l + f <=100, "Water" # Обмеження на воду
model += l <=50, "Sugar"        # Обмеження на цукор
model += l <=30, "Lemon Juice"  # Обмеження на лимонний сік
model += 2 * f <=40, "Fruit Puree"# Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Статус: {pulp.LpStatus[model.status]}\n")
print("Виробляти Лимонаду:", l.varValue)
print("Виробляти Фруктового соку:", f.varValue)
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")

# Обчислення витрачених ресурсів
used_water = 2 * l.varValue + f.varValue
remaining_water = 100 - (2 * l.varValue + f.varValue)
used_sugar = l.varValue
remaining_sugar = 50 - l.varValue
used_lemon_juice = l.varValue
remaining_juice = 30 - l.varValue
used_fruit_puree = 2 * f.varValue
remaining_puree = 40 - (2 * f.varValue)

# Виведення витрачених ресурсів
print(f"Використано води: {used_water} одиниць. Залишилось: {remaining_water} одиниць.")
print(f"Використано цукру: {used_sugar} одиниць. Залишилось: {remaining_sugar} одиниць.")
print(f"Використано лимонного соку: {used_lemon_juice} одиниць. Залишилось: {remaining_juice} одиниць.")
print(f"Використано фруктового пюре: {used_fruit_puree} одиниць. Залишилось: {remaining_puree} одиниць.")