import sqlite3

def open():
    global conn, cursor
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' удаляет все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()

def create_table():
    open()
    do('''CREATE TABLE IF NOT EXISTS questions(id_question INTEGER PRIMARY KEY, question VARCHAR, correct VARCHAR, wrong1 VARCHAR, wrong2 VARCHAR, wrong3 VARCHAR)''') 
    do('''CREATE TABLE IF NOT EXISTS quiz(id_quiz INTEGER PRIMARY KEY, quiz_name VARCHAR)''')
    do("""CREATE TABLE IF NOT EXISTS quiz_content(
    id INTEGER PRIMARY KEY, id_quiz INTEGER, id_question INTEGER, 
    FOREIGN KEY (id_quiz) REFERENCES quiz (id),
    FOREIGN KEY (id_question) REFERENCES question (id))""")
    do("""CREATE TABLE IF NOT EXISTS results(id INTEGER PRIMARY KEY, id_quiz INTEGER, Name VARCHAR, Count INTEGER) """)
    close()

def add_links():
    links = (
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 6],
        [1, 8],
        [1, 10],
        [1, 12],
        [2, 3],
        [2, 2],
        [2, 4],
        [2, 5],
        [2, 7],
        [2, 9],
        [2, 11]
    )
    open()
    for i in links:
        print(i[0], i[1])
        cursor.execute('''INSERT INTO quiz_content(id_quiz, id_question) VALUES (?,?)''', (i[0], i[1]))
    conn.commit()
    close()

def add_question():
    questions = [
        ('Что добавляют в щи по старым русским рецептам?', 'Простакваша', 'Укроп', 'Рыбу', 'Чеснок'),
        ('Назовите страну с самой высокой продолжительностью жизни.', 'Китай', 'Россия', 'США', 'Польша'),
        ('Что носит дьявол в известном фильме?', 'Prada', 'Addidas', 'Nike', 'CalvinKlein'),
        ('прапрараррпа', 'Верный', 'ывывыв', 'ывыв', 'ывыв'),

        ('Как называется самая известная смотровая площадка Москвы?', 'Воробьевы-горы', 'Лужники', 'ВДНХ', 'Колизей'),
        ('Что в море является ориентиром для моряка?', 'Полярная звезда', 'Маяк', 'Облака', 'Солнце'),
        ('Самый просматриваемый видео-хостинг интернета - это', 'You-Tube', 'Tik Tok', 'Twitch', 'Instagram'),
        ('Новобранец на флоте - это', 'Салага', 'Рядовой', 'Командир', 'Школьник'),
        ('Что делает человек, который всегда поддерживает репутацию', 'Держит марку', 'Дерзит', 'Завидует', 'Лицемерит'),
        ('С какого возраста начинается долгожительство', '90', '10', '35', '76'),
        ('С помощью чего можно говорить по телефону за рулем?', 'Гарнитура', 'телевизор', 'Клавиатура', 'Телефон'),
        ('Главное орудие хоккеиста', 'Клюшка', 'Кулаки', 'Язык', 'Автомат'),
        
    ]
    open()
    cursor.executemany('''INSERT INTO questions(question, correct, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)''', questions)
    conn.commit()
    close()

def add_quiz():
    open()
    do('''INSERT INTO quiz(quiz_name) VALUES ("викторина 1")''')
    do('''INSERT INTO quiz(quiz_name) VALUES ("викторина 2")''')
    close()

def get_question(quiz_id, question_id):
    open()
    query = "SELECT questions.question, questions.correct, questions.wrong1, questions.wrong2, questions.wrong3 FROM  quiz_content, questions  WHERE quiz_content.id_quiz == (?) AND quiz_content.id_question == (?) AND questions.id_question == quiz_content.id_question"
    cursor.execute(query, [quiz_id, question_id])
    m_question = cursor.fetchone()
    close()
    return m_question

def next_question(quiz_id, question_id):
    open()
    query = 'SELECT id_question FROM quiz_content WHERE quiz_content.id_quiz == (?) AND quiz_content.id_question > (?) ORDER BY quiz_content.id_question'
    cursor.execute(query, [quiz_id, question_id])
    data = cursor.fetchone()
    if data == None:
        id_next_question = 0
    else:
        id_next_question = data[0]
    close()
    return id_next_question    


def add_new_question(quiz_id, question, correct, wrong1, wrong2, wrong3):
    open()
    query1 = '''INSERT INTO question IF NOT EXISTS(question, correct, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)'''
    query2 = '''SELECT id_question FROM quiz_content WHERE id_quiz == (?) ORDER BY id_question'''
    query3 = '''INSERT INTO quiz_content IF NOT EXISTS(id_quiz, id_question) VALUES (?,?)'''
    do(query1, [question, correct, wrong1, wrong2, wrong3])
    cursor.execute(query2,[quiz_id,])
    data = cursor.fetchall()
    question_id = len(data)
    do(query3, [quiz_id, question_id])
    close()

def add_new_quiz(quiz_name):
    open()
    query = 'INSERT INTO quiz (quiz_name) VALUES (?)'
    do(query, [quiz_name,])
    close()

def all_stats(id_quiz, name, correct):
    open()
    cursor.execute('''INSERT INTO results(id_quiz, Name, Count) VALUES (?, ?, ?) ''', (id_quiz, name, correct))
    conn.commit()
    close()

def m_sortirovka():
    open()    
    cursor.execute('''SELECT quiz_name, Name, Count FROM results, quiz WHERE results.id_quiz == quiz.id_quiz ORDER BY Count DESC''')
    Name_list = cursor.fetchall()
    close()
    return Name_list

def main():
    clear_db()
    create_table()
    add_question()
    add_quiz()
    add_links()
    m_sortirovka()

if __name__ == "__main__":
    main()