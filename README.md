# Проектування кібер-фізичних систем

## Практична робота №3, Варіант 7

### Завдання

Передбачення погоди на наступний рік. Рік теж треба вибрати один з існуючих. Температуру писати на день: 5-11 градусів цього дня.

### Виконання

#### Виконані додатки

- Збереження історії(база даних)
- Використання SQL бази даних(MySQL)
- UI(TKinter)
- Міграції
- Машинне навчання
- Sanity Check

#### Використані технології

- Python
- MySQL(база даних)
- SQLAlchemy(ORM для бази даних)
- Alembic(міграції)
- Pytest(тестування, Sanity Check)
- TKinter(GUI)
- Scikit Learn(машинне навчання)
- Pickle
- Pandas
- Numpy

#### Архітектура

- data(Данні програми)
  - model.pkl(ML модель, створена Scikit Learn та збережена Pickle)
  - training_data.csv(Дані для тренування моделі)
  - testing_data.csv(Дані для тестування роботи моделі)
- database(Пакет для роботи з базою даних)
  - connection.py(Підключення до бази даних)
  - models.py(Моделі до бази даних)
  - crud.py(Методи для операцій над моделями бази даних)
- gui/main_window.py(Пакет для користувацького інтерфейсу)(Клас головного вікна)
- logic/weather.py(Пакет, який абстрагує деталі роботи з іншими пакетами у прості методи для користувацького інтерфейсу)(Логіка роботи з передбаченням погоди)
- machine_learning(Пакет для навчання та використання ML моделі)
  - preprocess.py(Підготовка даних для навчання/тестування моделі)
  - model.py(Навчання моделі)
  - predict.py(Використання моделі для створення передбачень)
- migrations(Папка бібліотеки Alembic для міграцій бази даних)
- tests(Тести)
  - sanity_test.py(Sanity Check тест для підключення до бази даних, присутності навченої моделі та її правильного відкриття)
  - machine_learning_test.py(Тест на правильність роботи ML моделі, звіряючись зі справжніми, тестовими даними)
- main.py(Стартова точка, запуск MainWindow)