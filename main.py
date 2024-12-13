import time
import pyfiglet
from rich.console import Console
from rich.text import Text
import shutil

# Инициализация rich
console = Console()

# Основной цвет текста
TEXT_COLOR = "cyan"
BACKGROUND_COLOR = "black"

# Декоративная рамка
FRAME_SYMBOL = "*"
FRAME_PADDING = 2

# Текст для логотипа
LOGO_TEXT = "TEST LOGO"

def generate_frame(text):
    """Создает текст с рамкой."""
    lines = text.splitlines()
    max_length = max(len(line) for line in lines)


    framed_text = f"{FRAME_SYMBOL * (max_length + FRAME_PADDING * 2 + 2)}\n"
    for line in lines:
        centered_line = line.center(max_length)
        framed_text += f"{FRAME_SYMBOL}{' ' * FRAME_PADDING}{centered_line}{' ' * FRAME_PADDING}{FRAME_SYMBOL}\n"
    framed_text += f"{FRAME_SYMBOL * (max_length + FRAME_PADDING * 2 + 2)}"
    return framed_text

def colorful_ascii_art(text):
    """Создает аккуратный и стильный ASCII-арт с рамкой, выравненный по центру терминала."""
    ascii_art = pyfiglet.figlet_format(text)  # Генерация ASCII-арта
    framed_art = generate_frame(ascii_art)   # Добавление рамки
    console.print(Text(framed_art, style=f"bold {TEXT_COLOR} on {BACKGROUND_COLOR}"))

def display_logo():
    """Выводит логотип с предустановленным текстом."""
    colorful_ascii_art(LOGO_TEXT)

# Импортируемый метод для других проектов
def render_logo():
    display_logo()

# Запуск только при вызове напрямую
if __name__ == "__main__":
    display_logo()
