#Author: Arnav Arora
import tkinter as tk  
from tkinter import messagebox  
from tkinter import font as tkfont  
from PIL import Image, ImageTk  
import re  
import random  

#Main game class - handles everything and acts like a foundation
class MathGame:
    def __init__(self): #allows me to store all the variables which can be called later on
        """Initialize the game window and variables"""
        self.root=tk.Tk()
        self.root.title("Math Game")  
        self.root.geometry("400x450")  
        self.root.configure(bg="#00008B")  

        # Fonts setup 
        self.title_font=("Helvetica",24,"bold")  
        self.subtitle_font = ("Helvetica", 16, "bold")  
        self.body_font=("Helvetica", 12)  
        self.button_font=("Helvetica", 12, "bold") 
        self.feedback_font=("Helvetica",11,"italic")  
        self.timer_font=("Helvetica",12,"bold")  
        self.small_font=("Helvetica",8)  

        # Question banks 
        self.question_banks={
            "easy": self.create_easy_questions(), 
            "medium": self.create_medium_questions(), 
            "hard": self.create_hard_questions()
        }

        # Game state stuff
        self.currentquestions = [] 
        self.current_index=0  
        self.score=0  
        self.selectedDifficulty=None  
        self.time_left=0   
        self.playerName=""  
        self.user_answers=[]  
        self.current_image_label=None  
        self.current_image_ref=None  
        self.title_image_ref=None  

        #Start the program
        self.main_menu()
        self.root.mainloop()  

    # Question generation
    def create_easy_questions(self):
        questions=[]
        for i in range(20):
            choice=random.choice(['add','subtract','multiply','divide'])
            
            if choice=='add':
                a=random.randint(1,50)
                b=random.randint(1,50)
                question=f" {a} + {b}."
                answer=str(a+b)
            elif choice=='subtract':
                x=random.randint(1,50)
                y=random.randint(1,x)
                question=f" {x} - {y}."
                answer=str(x-y)
            elif choice=='multiply':
                n1=random.randint(1,12)
                n2=random.randint(1,12)
                question=f" {n1} x {n2}."
                answer=str(n1*n2)
            else: # division
                d=random.randint(1,10)
                n=d*random.randint(1,10)
                question=f" {n} ÷ {d}."
                answer=str(n//d)
            
            questions.append({"question":question,"answer":answer})
        return questions

     
     #Medium Questions
    def create_medium_questions(self):
        return [
            {"question": "What is ½ plus ½?", "answer": "1"},
            {"question": "What is 3 × 4?", "answer": "12"},
            {"question": "Solve for x: x + 5 = 9", "answer": "4"},
            {"question": "What is 10 - 7?", "answer": "3"},
            {"question": "What is 8 ÷ 2?", "answer": "4"},
            {"question": "What is 5 squared?", "answer": "25"},
            {"question": "What is √16?", "answer": "4"},
            {"question": "Solve for y: 2y = 10", "answer": "5"},
            {"question": "What is ¼ + ¼?", "answer": "1/2"},
            {"question": "What is 7 × 3?", "answer": "21"},
            {"question": "What is 15 ÷ 3?", "answer": "5"},
            {"question": "Solve for x: 3x = 12", "answer": "4"},
            {"question": "What is 9 - 4?", "answer": "5"},
            {"question": "What is 6 × 7?", "answer": "42"},
            {"question": "What is ½ × ½?", "answer": "1/4"},
            {"question": "Solve for y: y - 3 = 5", "answer": "8"},
            {"question": "What is 4 squared?", "answer": "16"},
            {"question": "What is √9?", "answer": "3"},
            {"question": "What is 12 ÷ 4?", "answer": "3"},
            {"question": "Solve for x: x + 7 = 15", "answer": "8"}
        ]
    #Hard Questions
    def create_hard_questions(self):
        return [
            {"question": "1/4 + 1/2?", "answer": "3/4"},
            {"question": "3/4 - 1/4.", "answer": "1/2"},
            {"question": "Calculate 20 times 30.", "answer": "600"},
            {"question": "Divide 100 by 20.", "answer": "5"},
            {"question": "What is 10 divided by 2?", "answer": "5"},
            {"question": "6/8-1/4.", "answer": "1/2"},
            {"question": "(2^2)^3.", "answer": "64"},
            {"question": "√25?", "answer": "5"},
            {"question": "If x + 2x = 9, what is x?", "answer": "3"},
            {"question": "What is 3 squared?", "answer": "9"},
            {"question": "Solve for x: 2x + 3 = 11.", "answer": "4"},
            {"question": "Solve for y: 3(y - 1) = 6.", "answer": "3"},
            {"question": "If x divided by 3 is 6, what is x?", "answer": "18"},
            {"question": "Solve for y: 2y - 4 = 10.", "answer": "7"},
            {"question": "Factor x² + 4x + 4.", "answer": "(x+2)(x+2)"},
            {"question": "Find the area of a triangle with base 8 and height 5.", "answer": "20"},
            {"question": "Calculate the area of a circle with radius 5 (π≈3.14).", "answer": "78.5"},
            {"question": "Find the volume of a cylinder with radius 3 and height 5 (π≈3.14).", "answer": "141.3"},
            {"question": "What is the surface area of a cube with side length 3?", "answer": "54"},
            {"question": "In a right triangle with sides 6 and 8, what is the longest side?", "answer": "10"}
        ]


    # Button styling 
    def style_button(self,btn):
        btn.configure(
            bg="#1E90FF",fg="white",font=self.button_font,
            relief="raised",bd=3,activebackground="#4682B4",
            activeforeground="white",cursor="hand2",padx=10,pady=5
        )

    # Name validation
    def validate_name(self,name):
        first_name=name.strip()
        
        if not first_name:
            return False,"Please enter a name"
        
        if len(first_name)<2:
            return False,"Too short (min 2 chars)"
        if len(first_name)>20:
            return False,"Too long (max 20)"
        
        if not re.match(r'^[a-zA-Z\- ]+$',first_name):
            return False,"Only letters/spaces/hyphens"
        
        return True,""

    # Answer validation
    def validate_answer(self,answer):
        ans=answer.strip()
        if not ans:  
                messagebox.showerror("Error","Answer cannot be blank!")  
                return False
        
        if not re.match(r'^[0-9xeEX+\-*/\^()=., ]+$',ans):
            messagebox.showerror("Invalid Chars", 
                               "Only use:\n"  
                               "- Numbers 0-9\n"  
                               "- x,e\n"  
                               "- Math symbols")  
            return False  
        
        return True  

    # Main menu setup
    def main_menu(self):
        for widget in self.root.winfo_children():
                widget.destroy()  

        self.root.geometry("400x550") 
        self.root.configure(bg="#004bac") 
        
        main_frame=tk.Frame(self.root,bg="#004bac")
        main_frame.pack(expand=True,fill=tk.BOTH,padx=20,pady=10)

        # Try loading logo
        try:
            img=Image.open("logo.png")
            img=img.resize((180,180),Image.Resampling.LANCZOS)  
            self.logo_img=ImageTk.PhotoImage(img)
            logo_label=tk.Label(main_frame,image=self.logo_img,bg="#004bac")  
            logo_label.pack(pady=(5,10))
        except Exception as e:
            print(f"Error loading logo:{e}")

        # Title
        tk.Label(main_frame,text="Math Game",fg="white",bg="#004bac",
                font=self.title_font).pack(pady=(0,15)) 

        # Buttons
        button_frame=tk.Frame(main_frame,bg="#004bac")
        button_frame.pack()

        buttons=[
            ("Start",self.info_window),
            ("History",self.show_history),
            ("Help",self.show_readme),
            ("Quit",self.root.destroy)
        ]

        for text,cmd in buttons:
            btn=tk.Button(button_frame,text=text,width=18,command=cmd)
            self.style_button(btn)
            btn.pack(pady=5)
 
    #About message
    def show_readme(self):
        msg="""Hey there, this a brief message about why I made this game.
I believe math is important for students. Wanted to make something fun
and educational. Hope you like it!"""
        messagebox.showinfo("About",msg)

    # Player info window
    def info_window(self):
        self.info_win=tk.Toplevel(self.root)
        self.info_win.title("Player Details")
        self.info_win.geometry("400x400")
        self.info_win.configure(bg="#00008B")
        self.selectedDifficulty=None 

        # Title
        tk.Label(self.info_win,text="Enter Your Details",
                 fg="white",bg="#00008B",font=self.subtitle_font).pack(pady=10)

        # Name input
        name_frame=tk.Frame(self.info_win,bg="#00008B")
        name_frame.pack(pady=5)
        
        tk.Label(name_frame,text="First Name:",fg="white",bg="#00008B",font=self.body_font).pack(side=tk.LEFT)

        self.name_entry=tk.Entry(name_frame,font=self.body_font)
        self.name_entry.pack(side=tk.LEFT)
        self.name_entry.focus() 

        # Requirements
        tk.Label(self.info_win,text="(2-20 letters)",fg="lightgray",bg="#00008B",font=self.small_font).pack()

        # Difficulty
        tk.Label(self.info_win,text="Select Difficulty:",fg="white",bg="#00008B",font=self.body_font).pack(pady=10)

        self.diff_label=tk.Label(self.info_win,text="No difficulty selected",fg="yellow",bg="#00008B",font=self.body_font)
        self.diff_label.pack()

        # Diff buttons
        diff_frame=tk.Frame(self.info_win,bg="#00008B")
        diff_frame.pack()

        easy_btn=tk.Button(diff_frame,text="Easy",width=8,command=self.set_easy)
        self.style_button(easy_btn)
        easy_btn.pack(side=tk.LEFT,padx=5)

        med_btn=tk.Button(diff_frame,text="Medium",width=8,command=self.set_medium)
        self.style_button(med_btn)
        med_btn.pack(side=tk.LEFT,padx=5)

        hard_btn=tk.Button(diff_frame,text="Hard",width=8,command=self.set_hard)
        self.style_button(hard_btn)
        hard_btn.pack(side=tk.LEFT,padx=5)

        # Start button
        start_btn=tk.Button(self.info_win,text="Start questions",command=self.validate_submission)
        self.style_button(start_btn)
        start_btn.pack(pady=20)

    def set_easy(self):
        self.selectedDifficulty="easy"
        self.diff_label.config(text="Selected: Easy",fg="lightgreen")

    def set_medium(self):
        self.selectedDifficulty="medium"
        self.diff_label.config(text="Selected: Medium",fg="orange")

    def set_hard(self):
        self.selectedDifficulty = "hard"
        self.diff_label.config(text="Selected: Hard",fg="red")

    #Function to validate name and difficulty chosen
    def validate_submission(self):
        name=self.name_entry.get()
        
        if not re.match(r'^[a-zA-Z\- ]+$',name):
            messagebox.showerror("Invalid Name","Only letters/spaces/hyphens")
            self.name_entry.focus()
            return

        if len(name)<2:
            messagebox.showerror("Too Short","Need at least 2 chars")
            self.name_entry.focus()
            return

        if not name:
            messagebox.showerror("Empty","Enter a name")
            self.name_entry.focus()
            return

        if len(name)>20:
            messagebox.showerror("Too Long","Max 20 characters")
            self.name_entry.focus()
            return
                
        if not self.selectedDifficulty:
            messagebox.showerror("Error","Select difficulty")
            return

        self.playerName=name.strip()
        self.start_questions(self.selectedDifficulty)
        self.info_win.destroy()

    #Creates the question window 
    def start_questions(self,level):
        self.currentquestions=self.question_banks[level]
        self.current_index=0
        self.score=0
        self.user_answers=[""]*len(self.currentquestions)

        self.questions_win=tk.Toplevel(self.root)
        self.questions_win.title(f"{level} questions")
        self.questions_win.geometry("600x550")
        self.questions_win.configure(bg="#00008B")

        # Timer
        timer_frame=tk.Frame(self.questions_win,bg="#00008B")
        timer_frame.pack(fill="x",pady=10)
        
        tk.Label(timer_frame,bg="#00008B").pack(side="left",expand=True)
        
        self.time_left=240
        self.timer_label=tk.Label(timer_frame,text="Time: 04:00",
                                  fg="white",bg="#00008B",font=self.timer_font)
        self.timer_label.pack(side="left")
        
        tk.Label(timer_frame,bg="#00008B").pack(side="left",expand=True)
        
        self.update_timer()

        # Image area
        self.image_frame=tk.Frame(self.questions_win,bg="#00008B")
        self.current_image_label=tk.Label(self.image_frame,bg="#00008B")

        # Question display
        self.question_label=tk.Label(self.questions_win,text="",wraplength=500,
                                     fg="white",bg="#00008B",font=self.body_font)
        self.question_label.pack(pady=10)

        # Answer input
        self.answer_entry=tk.Entry(self.questions_win,font=self.body_font)
        self.answer_entry.pack(pady=10)
        self.answer_entry.focus()

        #Buttons
        button_frame=tk.Frame(self.questions_win,bg="#00008B")
        button_frame.pack(pady=10)

        back_btn=tk.Button(button_frame,text="Back",command=self.go_back)
        self.style_button(back_btn)
        back_btn.pack(side=tk.LEFT,padx=10)

        submit_btn=tk.Button(button_frame,text="Submit",command=self.check_answer)
        self.style_button(submit_btn)
        submit_btn.pack(side=tk.LEFT,padx=10)

        # Feedback
        self.feedback_label=tk.Label(self.questions_win,text="",
                                     fg="yellow",bg="#00008B",font=self.feedback_font)
        self.feedback_label.pack()

        # Show first question
        self.show_current_question()

    #Loads the Question Images
    def load_image(self,img_path):
        try:
            img=Image.open(img_path)
            img=img.resize((300,200),Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading {img_path}:{e}")
            return None

    #Displays the current question
    def show_current_question(self):
        if self.current_index>=len(self.currentquestions):
            self.show_summary()
            self.questions_win.destroy()
            return
        
        q=self.currentquestions[self.current_index]
        self.question_label.config(text=f"Q{self.current_index+1}: {q['question']}")
        
        if 'image'in q:
            try:
                img=self.load_image(q['image'])
                if img:
                    self.current_image_label.config(image=img)
                    self.current_image_ref=img
                    self.image_frame.pack(pady=5)
            except:
                self.image_frame.pack_forget() #continues the program if the image does not work as a failsafe
        else:
            self.image_frame.pack_forget()
        
        self.answer_entry.delete(0,tk.END)
        if self.user_answers[self.current_index]:
            self.answer_entry.insert(0,self.user_answers[self.current_index])
        
        self.feedback_label.config(text="")

    # goes back to previous question
    def go_back(self):
        if self.current_index>0:
            self.user_answers[self.current_index]=self.answer_entry.get().strip()
            self.current_index-=1
            self.show_current_question()

    #Function to make timer work
    def update_timer(self):
        if self.time_left>0:
            mins,secs=divmod(self.time_left,60)
            self.timer_label.config(text=f"Time: {mins:02d}:{secs:02d}")
            self.time_left-=1
            self.questions_win.after(1000,self.update_timer)
        else:
            self.time_up()

    #If time runs out, it proceeds to summary window
    def time_up(self):
        self.show_summary(time_expired=True)
        self.questions_win.destroy()

    #Validates and checks the answer
    def check_answer(self):
        user_ans=self.answer_entry.get().strip()
        
        if not self.validate_answer(user_ans):
            self.answer_entry.focus()
            return
        
        self.user_answers[self.current_index]=user_ans
        correct_ans=str(self.currentquestions[self.current_index]["answer"])

        if user_ans.lower()==correct_ans.lower():
            self.score+=1
            self.feedback_label.config(text="Correct!",fg="green")
        else:
            self.feedback_label.config(text=f"Wrong. Answer: {correct_ans}",fg="red")

        self.current_index+=1
        self.questions_win.after(500,self.show_current_question)

    #Once the user has answered all the questions, this displays the summary window
    def show_summary(self,time_expired=False):
        time_taken=240-self.time_left if not time_expired else 240
        mins,secs=divmod(time_taken,60)

        #Summary Window
        summary=tk.Toplevel(self.root)
        summary.title("Results")
        summary.geometry("400x400")
        summary.configure(bg="#00008B")
        self.summary_win=summary

        tk.Label(summary,text="Results Summary",fg="white",bg="#00008B",
                 font=self.subtitle_font).pack(pady=10)

        tk.Label(summary,text=f"Player: {self.playerName}",fg="white",bg="#00008B",font=self.body_font).pack() #Label for player name
        tk.Label(summary,text=f"Difficulty: {self.selectedDifficulty.capitalize()}",fg="white",bg="#00008B",font=self.body_font).pack()#label for difficulty chosen
        tk.Label(summary,text=f"Score: {self.score}/{len(self.currentquestions)}",fg="white",bg="#00008B",font=self.body_font).pack()#label for the user Score
        tk.Label(summary,text=f"Time: {mins:02d}:{secs:02d}",fg="white",bg="#00008B",font=self.body_font).pack()#Label for time taken

        #Calculates percentage score
        percentage=(self.score/len(self.currentquestions))*100
        tk.Label(summary,text=f"Percentage: {percentage:.1f}%",
                 fg="white",bg="#00008B",font=self.body_font).pack(pady=10)

        self.save_results()

        #menu and quit buttons
        menu_btn=tk.Button(summary,text="Main Menu",command=self.return_to_menu)
        self.style_button(menu_btn)
        menu_btn.pack(pady=10)

        quit_btn=tk.Button(summary,text="Quit",command=self.root.destroy)
        self.style_button(quit_btn)
        quit_btn.pack(pady=5)

    def return_to_menu(self):
        self.summary_win.destroy()
        self.main_menu()

    #Saves the results to a text file 
    def save_results(self):
        try:
            with open("results.txt","a")as f:
                f.write(f"{self.playerName},{self.selectedDifficulty},{self.score},"
                        f"{len(self.currentquestions)},{240-self.time_left}\n")
        except Exception as e:
            messagebox.showerror("Error",f"Save failed:{e}")

    #Shows the results which are saved in a history window
    def show_history(self):
        try:
            with open("results.txt","r")as f:
                results=f.readlines()
        except:
            results=[]

        #Creates the Window
        history=tk.Toplevel(self.root)
        history.title("History")
        history.geometry("500x400")
        history.configure(bg="#004bac")

        #creates the label and frame
        tk.Label(history,text="Game History",fg="white",bg="#004bac",
                font=("Helvetica",16,"bold")).pack(pady=10)

        results_frame=tk.Frame(history,bg="white")
        results_frame.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)

        #Allows the user number and their results to be displayed on the same column 
        headers=["Name","Difficulty","Score","Time"]
        for col,header in enumerate(headers): # used to make a list with a designated number
            tk.Label(results_frame,text=header,bg="#f0f0f0",
                    font=("Helvetica",10,"bold"),width=12,relief=tk.RIDGE).grid(row=0,column=col,sticky="ew")

        #Allows the user number and their results to be displayed on the same row
        for row,result in enumerate(results,start=1):
            parts=result.strip().split(',')
            if len(parts)>=5:
                bg_color="#ffffff" if row%2==1 else "#f8f8f8"
                
                tk.Label(results_frame,text=parts[0][:12],bg=bg_color,
                        width=12,anchor="w").grid(row=row,column=0,sticky="w")
                
                tk.Label(results_frame,text=parts[1].capitalize(),bg=bg_color,
                        width=12).grid(row=row,column=1)
                
                tk.Label(results_frame,text=f"{parts[2]}/{parts[3]}",bg=bg_color,
                        width=12).grid(row=row,column=2)
                
                time_sec=int(parts[4])
                mins=time_sec//60
                secs=time_sec%60
                tk.Label(results_frame,text=f"{mins:02d}:{secs:02d}",bg=bg_color,
                        width=12).grid(row=row,column=3)

        #Button to close window
        close_btn=tk.Button(history,text="Close",command=history.destroy,
                           bg="#1E90FF",fg="white",font=("Helvetica",10))
        close_btn.pack(pady=10)

if __name__=="__main__":
    MathGame()
