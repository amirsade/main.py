import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.text_question = None
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.create_label()
        self.create_canvas()
        self.button_create()

        self.window.mainloop()

    def create_label(self):
        self.label = tk.Label(text='Score: 0',
                              fg='white',
                              bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

    def create_canvas(self):
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.text_question = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='Some Question Text',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

    def button_create(self):
        self.true_img = tk.PhotoImage(file='images/true.png')
        self.false_img = tk.PhotoImage(file='images/false.png')

        self.true_button = tk.Button(image=self.true_img, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        self.false_button = tk.Button(image=self.false_img, highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text_question, text=q_text)




