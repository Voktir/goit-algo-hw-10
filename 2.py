import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Функція для обчислення інтегралу методом Монте-Карло
def monte_carlo_integral(f, a, b, N):
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, f(b), N)
    under_curve = y < f(x)
    integral_mc = (b - a) * f(b) * np.sum(under_curve) / N
    return integral_mc, x, y, under_curve

# Функція для аналітичного обчислення інтегралу
def analytical_integral(f, a, b):
    integral_analytical, _ = spi.quad(f, a, b)
    return integral_analytical

# Функція для побудови графіка
def plot_integral(f, a, b, x_random, y_random, under_curve):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Відображення випадкових точок
    ax.scatter(x_random, y_random, color='gray', s=1, label='Випадкові точки')
    ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, label='Точки під кривою')

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
    plt.legend()
    plt.grid()
    plt.show()

# Функція для відображення результатів
def display_results(integral_mc, integral_analytical, error, N):
    results = f"\nКількість випадкових точок: {N}\n"
    results += f"\n{'Метод':<15}{'Результат':<25}{'Похибка':<25}\n"
    results += "="*65 + "\n"
    results += f"{'Монте-Карло':<15}{integral_mc:<25.6f}{error:<25.6f}\n"
    results += f"{'Аналітичний':<15}{integral_analytical:<25.6f}{'0.000000':<25}"
    return results


# Основна функція
def main(N):
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Обчислення інтегралів
    integral_mc, x_random, y_random, under_curve = monte_carlo_integral(f, a, b, N)
    integral_analytical = analytical_integral(f, a, b)
    error = abs(integral_mc - integral_analytical)

    # Виведення результатів
    results_table = display_results(integral_mc, integral_analytical, error, N)
    print(results_table)

    # Побудова графіка
    plot_integral(f, a, b, x_random, y_random, under_curve)

# Виклик основної функції з кількістю випадкових точок N
def multiple_sets(*sets):
    for N in sets:
        print(main(N))

# Виклик функції для обробки кількох наборів точок
multiple_sets(100, 1000, 10000, 100000)