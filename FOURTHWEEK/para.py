DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':  # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
        friends_string = ''
        for friends_string in DATABASE:     # Переберите словарь DATABASE в цикле
             friends_string = ' '.join(DATABASE)    # Добавляйте к переменной friends_string имя друга и пробел
        return 'Твои друзья: ' + str(friends_string)  # Верните строку, составленную из 'Твои друзья: ' и friends_string 
    elif query == 'Где все мои друзья?':
        return('Я поняла, это вопрос про города!')
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))
