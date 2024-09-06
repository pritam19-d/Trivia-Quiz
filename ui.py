from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz= quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text="Score : 0", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height= 250, background="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="question text", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.tick_button = Button(image=true_img, highlightthickness=0, command=self.handle_click_true)
        self.cross_button = Button(image=false_img, highlightthickness=0, command=self.handle_click_false)

        self.tick_button.grid(row=2, column=0)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        current_score = self.quiz.score
        self.score_label.config(text=f"Score {current_score}")
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="Thanks for participating,\n"
                                                       f"Your final score is = {current_score}.")
            self.tick_button["state"] = self.cross_button["state"]= DISABLED

    def handle_click_true(self):
        ans_pressed = self.quiz.check_answer("True")
        self.give_feedback(ans_pressed)

    def handle_click_false(self):
        ans_pressed = self.quiz.check_answer("False")
        self.give_feedback(ans_pressed)

    def give_feedback(self, feedback):
        if feedback:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")

        self.window.after(1000, self.get_next_question)