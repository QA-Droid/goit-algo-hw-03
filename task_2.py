import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")
    t.penup()
    t.goto(-size / 2, size / (2 * 3**0.5))
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def parse_arguments():
    parser = argparse.ArgumentParser(description="Створення фракталу «сніжинка Коха» з вказаним рівнем рекурсії.")
    parser.add_argument('order', type=int, help="Рівень рекурсії (наприклад, 0, 1, 2, ...)")
    parser.add_argument('--size', type=float, default=300, help="Розмір сніжинки (за замовчуванням 300)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    draw_koch_snowflake(args.order, args.size)

if __name__ == "__main__":
    main()