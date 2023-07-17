import tkinter as tk
from functools import partial  # Для имени функции с параметром

ROOT_WIDTH: int = 510
ROOT_HEIGHT: int = 525

BTN_NAMES: tuple[tuple[str, str, str, str]] = (
('1', '2', '3', '+'), ('4', '5', '6', '-'), ('7', '8', '9', '*'), ('.', '0', '=', '/'))

root = tk.Tk()

SCREEN_WIDTH: int = root.winfo_screenwidth()
SCREEN_HEIGHT: int = root.winfo_screenheight()


class Calculator:
    def __init__(self, entry: tk.Entry) -> None:
        """
        Конструктор класса Calculator.
        :param entry: поле ввода, куда будет выводиться результат вычислений
        """
        self.expression = ""
        self.entry = entry

    def add_symbol(self, symbol: str) -> None:
        """
        Метод add_symbol добавляет символ к текущему выражению или вычисляет результат, если символ равен '='.
        :param symbol: символ для добавления или вычисления
        """
        if symbol != '=':
            self.expression += symbol  # Добавить символ к выражению
        else:  # if '='
            try:
                result = self.calculate_expression()  # Вычислить результат
                self.expression = str(result)  # Преобразовать результат в строку
            except Exception:
                self.expression = "Error"

        self.update_entry()

    def calculate_expression(self) -> float:
        """
        Метод calculate_expression вычисляет значение текущего выражения.
        :return: результат вычисления
        """
        if self.expression.count('+') == 1:
            num1, num2 = self.expression.split('+')
            return float(num1) + float(num2)
        elif self.expression.count('-') == 1:
            num1, num2 = self.expression.split('-')
            return float(num1) - float(num2)
        elif self.expression.count('*') == 1:
            num1, num2 = self.expression.split('*')
            return float(num1) * float(num2)
        elif self.expression.count('/') == 1:
            num1, num2 = self.expression.split('/')
            return float(num1) / float(num2)
        else:
            raise ValueError("Invalid expression")

    def update_entry(self) -> None:
        """
        Метод update_entry обновляет поле ввода значениями текущего выражения.
        """
        self.entry.delete(0, tk.END)  # Удалить весь текст из entry
        self.entry.insert(0, self.expression)  # Вставить текущее выражение в entry


class App:
    def __init__(self, root: tk.Tk) -> None:
        """
        Конструктор класса App.
        :param root: корневое окно приложения
        """
        self.root = root
        self.create_window()
        self.create_buttons()

    def create_window(self) -> None:
        """
        Метод create_window создает окно калькулятора с заданными размерами и расположением на экране.
        """
        self.root.title('Калькулятор')

        root_offset_x = (SCREEN_WIDTH - ROOT_WIDTH) // 2
        root_offset_y = (SCREEN_HEIGHT - ROOT_HEIGHT) // 2

        self.root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}+{root_offset_x}+{root_offset_y}')

    def create_buttons(self) -> None:
        """
        Метод create_buttons создает кнопки для ввода символов и операций.
        """
        ent = tk.Entry(self.root, width=50)
        ent.grid(row=0,
                 column=0,
                 columnspan=4,
                 padx=10,
                 pady=10)

        calculator = Calculator(ent)

        for row_number in range(len(BTN_NAMES)):
            for col_number in range(len(BTN_NAMES[row_number])):
                name = BTN_NAMES[row_number][col_number]
                btn = self.create_button(name, calculator)

                btn.grid(row=row_number + 1,
                         column=col_number,
                         padx=10,
                         pady=10
                         )

    def create_button(self, name: str, calculator: Calculator) -> tk.Button:
        """
        Метод create_button создает и возвращает кнопку с заданным именем и функцией-обработчиком.
        :param name: имя кнопки
        :param calculator: экземпляр класса Calculator
        :return: созданная кнопка
        """
        return tk.Button(self.root,
                         text=name,
                         font=('Arial', 13),
                         height=3,
                         width=7,
                         relief=tk.RAISED,
                         bd=5,
                         command=partial(calculator.add_symbol, name))

    def run(self) -> None:
        """
        Метод run запускает главный цикл приложения.
        """
        self.root.mainloop()


help(App)

if __name__ == '__main__':
    app = App(root)
    app.run()
