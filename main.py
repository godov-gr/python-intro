import time
import pyfiglet
from rich.console import Console
from rich.text import Text

# Инициализация rich
console = Console()

# Основной цвет текста
TEXT_COLOR = "cyan"
BACKGROUND_COLOR = "black"

# Декоративная рамка
FRAME_SYMBOL = "*"
FRAME_PADDING = 2

def generate_frame(text):
    """Создает текст с рамкой."""
    lines = text.splitlines()
    max_length = max(len(line) for line in lines)
    framed_text = f"{FRAME_SYMBOL * (max_length + FRAME_PADDING * 2)}\n"
    for line in lines:
        framed_text += f"{FRAME_SYMBOL}{' ' * FRAME_PADDING}{line.ljust(max_length)}{' ' * FRAME_PADDING}{FRAME_SYMBOL}\n"
    framed_text += f"{FRAME_SYMBOL * (max_length + FRAME_PADDING * 2)}"
    return framed_text

def colorful_ascii_art(text):
    """Создает аккуратный и стильный ASCII-арт с рамкой."""
    ascii_art = pyfiglet.figlet_format(text)  # Генерация ASCII-арта
    framed_art = generate_frame(ascii_art)   # Добавление рамки
    console.print(Text(framed_art, style=f"bold {TEXT_COLOR} on {BACKGROUND_COLOR}"))

def main():
    console.print("[cyan bold]Добро пожаловать в программу генерации стильного ASCII-интро![/cyan bold]")
    console.print("[yellow]Введите текст для создания вашего интро:[/yellow]")
    user_input = input("[green]>>> ")

    colorful_ascii_art(user_input)

    console.print("\n[cyan bold]Ваше интро готово! Спасибо за использование программы.[/cyan bold]")

if __name__ == "__main__":
    main()
