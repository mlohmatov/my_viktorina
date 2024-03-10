from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.layout import Layout
from bd_scripts import *
from random import shuffle
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
pink = (0.87, .54, .8, 1) 
Window.clearcolor = pink
correct = 0
m_name = ''
choise = 1
question_id = 0
number = 1
text_correct = ''
total = 0
i = 1

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        txt = Label(text = 'Начальная фраза', font_size = 24)
        txt_get = Label(text = 'Ваше имя:', font_size = 24)
        self.btn = Button(text = 'Перейти к вопросам', font_size = 24)
        self.btn_quiz1 = Button(text = 'Викторина 1', font_size = 24)
        self.btn_quiz2 = Button(text = 'Викторина 2', font_size = 24)
        self.btn_quiz1.on_press = self.choise_quiz1
        self.btn_quiz2.on_press = self.choise_quiz2
        self.btn.on_press = self.next
        self.text_input = TextInput(multiline = False)
        h1 = BoxLayout(spacing = 8)
        v_main = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        v1 = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        h2 = BoxLayout(spacing = 8)

        h1.add_widget(txt_get)
        h1.add_widget(self.text_input)

        h2.add_widget(self.btn_quiz1)
        h2.add_widget(self.btn_quiz2)

        v_main.add_widget(txt)        
        v_main.add_widget(h1)
        v_main.add_widget(h2)
        v_main.add_widget(self.btn)

        self.add_widget(v_main)

    def choise_quiz1(self):
        global choise
        choise = 1

    def choise_quiz2(sef):
        global choise
        choise = 2        

    def next(self):
        global m_name, choise, number, question_id, text_correct
        self.manager.transition.direction = 'left'
        a = self.manager.get_screen('question')
        a.next()
        self.manager.current = 'question'
        m_name = self.text_input.text





class Question(Screen):    
    def __init__(self, name = 'question'):
        super().__init__(name = name)
        
        global number, choise, question_id, text_correct
        m_answers = list()
        '''
        question_id = next_question(choise, 0)
        question = get_question(choise, question_id)
        for i in question:
            m_answers.append(i)
        answers = m_answers[1:]
        text_correct = question[1]
        shuffle(answers)'''
        

        self.question = Label(text = 'текст вопроса', font_size = 24)

        self.answer1 = ToggleButton(text = 'ответ1', group = 'answer', state='normal', font_size = 24)
        self.answer2 = ToggleButton(text = 'ответ2', group = 'answer', state='normal', font_size = 24)
        self.answer3 = ToggleButton(text = 'ответ3', group = 'answer', state='normal', font_size = 24)
        self.answer4 = ToggleButton(text = 'ответ4', group = 'answer', state='normal', font_size = 24)

        btn = Button(text = 'Дальше', font_size = 24)
        btn.on_press = self.next
        


        h1 = BoxLayout()
        h2 = BoxLayout()
        h3 = BoxLayout(padding = 8, spacing = 20)
        h4 = BoxLayout(padding = 8, spacing = 20)
    
        v = BoxLayout(orientation = 'vertical', spacing = 20)

        h2.add_widget(self.question)
        h3.add_widget(self.answer1)
        h3.add_widget(self.answer2)
        h4.add_widget(self.answer3)
        h4.add_widget(self.answer4)
        v.add_widget(h1)
        v.add_widget(h2)
        v.add_widget(h3)
        v.add_widget(h4)
        v.add_widget(btn)
        self.add_widget(v)        


    def next(self):
        global choise, question_id, text_correct, correct
        
        if question_id !=0:
            m_atribut = ( self.answer1, self.answer2, self.answer3, self.answer4)
            for i in m_atribut:
                if i.state == 'down' and i.text == text_correct:
                    correct += 1


        m_answers = list()
        question_id = next_question(choise, question_id)
        if question_id == 0:
            self.manager.transition.direction = 'left'
            self.manager.current = 'result'
            return
        question = get_question(choise, question_id)
        for i in question:
            m_answers.append(i)
        answers = m_answers[1:]
        text_correct = question[1]
        shuffle(answers)

        self.question.text = question[0]
        self.answer1.text = answers[0]
        self.answer2.text = answers[1]
        self.answer3.text = answers[2]
        self.answer4.text = answers[3]
        self.answer1.state = 'normal'
        self.answer2.state = 'normal'  
        self.answer3.state = 'normal'  
        self.answer4.state = 'normal'
             
        


class Result(Screen):
    def __init__(self, name = 'result'):
        super().__init__(name=name)
        self.btn = Button(text = 'получить', font_size = 24)
        self.btn.on_press = self.change_text       
        self.txt = Label(text = 'Вы закончили викторину', font_size = 24)
        txt_result = Label(text = 'нажмите <<Получить>> чтобы получить результаты', font_size = 24)
        self.txt_result = txt_result
        self.txt_11 = Label(text = '')
        self.txt_12 = Label(text = '')
        self.txt_13 = Label(text = '')
        self.txt_21 = Label(text = '')
        self.txt_22 = Label(text = '')
        self.txt_23 = Label(text = '')
        self.txt_31 = Label(text = '')
        self.txt_32 = Label(text = '')
        self.txt_33 = Label(text = '')
        self.txt_41 = Label(text = '')
        self.txt_42 = Label(text = '')
        self.txt_43 = Label(text = '')
        self.txt_51 = Label(text = '')
        self.txt_52 = Label(text = '')
        self.txt_53 = Label(text = '')
        h1 = BoxLayout()
        h2 = BoxLayout()
        v = BoxLayout(orientation = 'vertical', spacing = 20)
        h1.add_widget(self.txt)
        h2.add_widget(self.txt_result)
        v.add_widget(h1)
        v.add_widget(h2)
        mt_layout = GridLayout(cols = 3)
        mt_layout.add_widget(self.txt_11)
        mt_layout.add_widget(self.txt_12)
        mt_layout.add_widget(self.txt_13)
        mt_layout.add_widget(self.txt_21)
        mt_layout.add_widget(self.txt_22)
        mt_layout.add_widget(self.txt_23)
        mt_layout.add_widget(self.txt_31)
        mt_layout.add_widget(self.txt_32)
        mt_layout.add_widget(self.txt_33)
        mt_layout.add_widget(self.txt_41)
        mt_layout.add_widget(self.txt_42)
        mt_layout.add_widget(self.txt_43)
        mt_layout.add_widget(self.txt_51)
        mt_layout.add_widget(self.txt_52)
        mt_layout.add_widget(self.txt_53)
        v.add_widget(mt_layout)
        v.add_widget(self.btn)        
        self.add_widget(v)

    def change_text(self):
        global m_name, correct, choice, i 
        
        if i == 1:
            self.txt.text = 'Поздравляю, ' + m_name + '!'
            self.txt_result.text = 'Вы ответили на '+ str(correct) + ' из 3'
            all_stats(choise, m_name, correct)
            self.btn.text = 'Узнать топ 5'
            i += 1
        elif i == 2:   
            m_vivod = m_sortirovka()
            if len(m_vivod) >= 1:
                self.txt_11.text = str(m_vivod[0][0])
                self.txt_12.text = str(m_vivod[0][1]) 
                self.txt_13.text = str(m_vivod[0][2])
            if len(m_vivod) >= 2:
                self.txt_21.text = str(m_vivod[1][0]) 
                self.txt_22.text = str(m_vivod[1][1])
                self.txt_23.text = str(m_vivod[1][2])
            if len(m_vivod) >= 3:
                self.txt_31.text = str(m_vivod[2][0]) 
                self.txt_32.text = str(m_vivod[2][1]) 
                self.txt_33.text = str(m_vivod[2][2])
            if len(m_vivod) >= 4: 
                self.txt_41.text = str(m_vivod[3][0])
                self.txt_42.text = str(m_vivod[3][1])
                self.txt_43.text = str(m_vivod[3][2])
            if len(m_vivod) >= 5: 
                self.txt_51.text = str(m_vivod[4][0]) 
                self.txt_52.text = str(m_vivod[4][1]) 
                self.txt_53.text = str(m_vivod[4][2])
            self.btn.text = 'Выйти'
            i += 1
        elif i == 3:
            quit()



class MyApp(App):    
    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScr())
        sm.add_widget(Question())
        sm.add_widget(Result())
        return sm
      
app = MyApp()
app.run()