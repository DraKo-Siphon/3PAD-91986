#Author: Arnav Arora

#Import necessary libraries
import tkinter as tk  # For GUI components
from tkinter import messagebox  # For displaying message boxes
from tkinter import font as tkfont  # For font styling
from PIL import Image, ImageTk  # For image handling
import re  # For regular expressions (input validation)

class MathGame:
    def __init__(self): #creates the sort of "foundation" for program
        """Initialize the main application window and game variables"""
        
        # Create main Tkinter window
        self.root = tk.Tk()
        self.root.title( "Math Game" )  
        self.root.geometry("400x450")  #Window Size
        self.root.configure(  bg="#00008B"  )  #Sets BG colour

        # Font definitions
        self.title_font = ("Helvetica",24,"bold")  #font for title
        self.subtitle_font = ("Helvetica", 16, "bold")  
        self.body_font =("Helvetica", 12)  
        self.button_font = ("Helvetica", 12, "bold") #Font for buttons
        self.feedback_font = ("Helvetica", 11, "italic")  
        self.timer_font = ("Helvetica", 12, "bold")  #Font for Timer
        self.small_font = ("Helvetica",8)  

        # Question banks
        self.question_banks = {
            "easy" : self.create_easy_questions(),  #Easy Question Function
            "medium":self.create_medium_questions(),  #Medium Question Function
            "hard" : self.create_hard_questions()  #Hard Question Function
        }

        # Game state variables
        self.current_questions = [] #Empty list to store questions 
        self.current_index=0  #Question No which user is on
        self.score = 0  #User Score
        
        self.selected_difficulty=None  #Difficulty Level of user
        self.time_left = 0   # Time remaining in questions
        
        self.player_name=""  
        self.user_answers = []  #Store user's answers
        
        
        self.current_image_label=None  
        self.current_image_ref = None  
        self.title_image_ref =None  

        # Initialize application
        self.main_menu( )
        self.root.mainloop( )  

    # Question bank creation methods
    def create_easy_questions(self):
        return [{"question": "Add: 2 + 3", "answer": "5"},
            {"question": "Subtract: 7 - 4", "answer": "3"},
            {"question": "Multiply: 3 × 5", "answer": "15"},
            {"question": "Divide: 10 ÷ 2", "answer": "5"},
            {"question": "What is 50% of 100?", "answer": "50"},
            {"question": "Next number: 2, 4, 6, _", "answer": "8"},
            {"question": "Square of 5", "answer": "25"},
            {"question": "Square root of 16", "answer": "4"},
            {"question": "5 + 7 × 2", "answer": "19"},
            {"question": "Perimeter of square (side=4)", "answer": "16"},
            {"question": "Area of rectangle (4×5)", "answer": "20"},
            {"question": "Volume of box (2×3×4)", "answer": "24"},
            {"question": "Degrees in right angle", "answer": "90"},
            {"question": "Degrees in triangle", "answer": "180"},
            {"question": "10 to the power of 0", "answer": "1"},
            {"question": "Solve: x + 3 = 7", "answer": "4"},
            {"question": "Solve: 2x = 10", "answer": "5"},
            {"question": "Is 17 prime?", "answer": "yes"},
            {"question": "First prime number", "answer": "2"},
            {"question": "458+239", "answer": "697"}
        ]
   
    def create_medium_questions(self):
        return [
            {"question": "What is ½ + ½?", "answer": "1"},
            {"question": "What is ¾ - ¼?", "answer": "½"},
            {"question": "What is 20 × 30?", "answer": "600"},
            {"question": "What is 100 ÷ 20?", "answer": "5"},
            {"question": "What is 10 divided by 2?", "answer": "5"},
            {"question": "What is 2 to the power of -1?", "answer": "½"},
            {"question": "What is (2 squared) cubed?", "answer": "64"},
            {"question": "What is the square root of 25?", "answer": "5"},
            {"question": "If x + 2x = 9, what is x?", "answer": "3"},
            {"question": "What is 3 squared?", "answer": "9"},
            {"question": "If 2x + 3 = 11, what is x?", "answer": "4"},
            {"question": "If 3(y - 1) = 6, what is y?", "answer": "3"},
            {"question": "If x divided by 3 is 6, what is x?", "answer": "18"},
            {"question": "If 2y - 4 = 10, what is y?", "answer": "7"},
            {"question": "Factor this: x² + 4x + 4", "answer": "(x+2)(x+2)"},
            {"question": "Area of triangle (base=8, height=5)", "answer": "20", "image": "triangle_1.png"},
            {"question": "Area of circle (radius=5, π≈3.14)", "answer": "78.5", "image": "circle_1.png"},
            {"question": "Volume of cylinder (radius=3, height=5, π≈3.14)", "answer": "141.3"},
            {"question": "Surface area of cube (side=3)", "answer": "54"},
            {"question": "In a right triangle, if sides are 6 and 8, what’s the longest side?", "answer": "10"}
        ]

    def create_hard_questions(self):
        return [
            {"question": "What is ¼ + ½?", "answer": "¾"},
            {"question": "What is ⅔ - ⅓?", "answer": "⅓"},
            {"question": "What is ½ × ⅔?", "answer": "⅓"},
            {"question": "What is ⅖ ÷ ⅕?", "answer": "2"},
            {"question": "What is (10/20) ÷ (15/30)?", "answer": "1"},
            {"question": "Simplify (x²y)³", "answer": "x⁶y³"},
            {"question": "What is 4 to the power of (3/2)?", "answer": "8"},
            {"question": "If 3^(x-1) = 9, what is x?", "answer": "3"},
            {"question": "Simplify (2a²b)² ÷ (4a³b)", "answer": "ab"},
            {"question": "Simplify 1 divided by √2", "answer": "√2/2"},
            {"question": "If log₃(x) = 2, what is x?", "answer": "9"},
            {"question": "Factor this: x² - 5x + 6", "answer": "(x-2)(x-3)"},
            {"question": "Solve: x + y = 5, x - y = 1", "answer": "x=3, y=2"},
            {"question": "Find the lowest point of y = x² - 4x + 3", "answer": "(2,-1)"},
            {"question": "Solve: x - 3 < 5", "answer": "x < 8"},
            {"question": "Find the slope of x² + 3x - 2", "answer": "2x+3"},
            {"question": "Find the area under 3x", "answer": "1.5x² + C"},
            {"question": "Find the slope of cos(x)", "answer": "-sin(x)"},
            {"question": "Find the area under 2x", "answer": "x² + C"},
            {"question": "What is (x² - 9)/(x - 3) when x gets close to 3?", "answer": "6"}
        ]

    def style_button(self, button):
        """Apply consistent styling to buttons"""
        button.configure(
            bg="#1E90FF",  # Background color 
            fg="white",  # Text color
            font=self.button_font,  # Font family and size
            relief="raised",  # 3D raised appearance
            bd=3,  # Border width
            activebackground="#4682B4",  # Color of button when clicked
            activeforeground="white",  # Text color when clicked
            cursor="hand2",  # Hand cursor on hover
            padx=10,  # Horizontal padding
            pady=5  # Vertical padding
        )

    def validate_name(self, name):
        """Validate the player's name meets requirements"""
        name = name.strip()  
        
        #Validates the answer of user
        if not name:
            return False, "Name cannot be empty"
        if len(name) < 2:
            return False, "Name must be at least 2 characters"  
            if len(name) > 20:
                return False, "Name cannot exceed 20 characters."  
        if not re.match(r'^[a-zA-Z\- ]+$', name):u 
            return False, "Name can only contain letters, spaces, and hyphens"  
        
        return True, ""  #Continues program if validation is correct

    def validate_answer(self, answer):
        """Validate that the answer contains only allowed characters (x, e, numbers, and basic math symbols)"""
        answer = answer.strip()
        if not answer:  
                messagebox.showerror("Error", "Answer cannot be blank!")  
                return False
        
        #Characters which are allowed in the answer field
        if not re.match(r'^[0-9xeEX+\-*/\^()=., ]+$', answer):
            messagebox.showerror("Invalid Characters", 
                               "Answer can only contain:\n"  
                               "- Numbers (0-9).\n"  
                               "- Letters x and e\n"  
                               "- Basic math symbols: + - * / ^ ( ) = , .")  
            
            return Falses  
        
        return True  

    def main_menu(self):
        """Main game menu - sets up the interface"""
        # Clear previous widgets if any
            # Had some issues with widget stacking before
        for widget in self.root.winfo_children():
                widget.destroy()  # sometimes indentation gets messy when I'm in a hurry

        # Window configuration
        self.root.geometry("400x550")  #size seemed good for most screens
        self.root.configure(bg="#004bac") #blue background looks nice
        
        # TODO: Maybe add responsive sizing later?
        main_frame = tk.Frame(self.root, bg="#004bac")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Logo handling - had issues with this on Mac
        try:
            logo_photo = Image.open("logo.png")
            #print("DEBUG: Image loaded successfully") # useful for testing
            logo_photo = logo_photo.resize((180, 180), Image.Resampling.LANCZOS)  
            logo_photo = ImageTk.PhotoImage(logo_photo)
            self.logo_photo_ref = logo_photo  #keep reference otherwise it disappears!
            
            logo_label = tk.Label(main_frame, image=logo_photo, bg="#004bac")  
            logo_label.image = logo_photo  #another reference just to be safe
            logo_label.pack(pady=(5, 10))
        except Exception as e:
            print(f"Error loading logo: {e}")  # simplified error message
            # TODO: Add fallback text logo here

        # Title section
        tk.Label(main_frame, text="Math Game", fg="white", bg="#004bac",
                font=self.title_font).pack(pady=(0, 15))  #needs more vertical space

        # Button frame - might need scrolling later
        button_frame = tk.Frame(main_frame, bg="#004bac")
        button_frame.pack()

        # Button definitions
        buttons = [
            ("Start", self.info_window),  # main game start
            ("History", self.show_history), # score history
            ("Help", self.show_readme),  # help docs
            ("Quit", self.root.destroy)  # exit button
        ]

        button_count = 0  

        # Create each button
        for btn_data in buttons:
            text, cmd = btn_data  # unpacking differently sometimes
            btn = tk.Button(button_frame, text=text, width=18, command=cmd)
            self.style_button(btn)
            btn.pack(pady=5)
            button_count += 1  # not really used but helpful when debugging

        #print(f"Created {button_count} buttons")  # debug print 

    def show_readme(self):
        """Display program message in a message box"""
        message = """ Hey there, this a brief message on why I made this game. I believe that math is extremely
important for our future students as a lot of the world's problems and solutions revolve around math.
I wanted to created something which our students could enjoy using and learn math at the same tine. I hope this program
meets your expectations :)."""
        messagebox.showinfo("Lore", message)

    def info_window(self):
        """Create player info input window (name and difficulty selection)"""
        self.info_window = tk.Toplevel(self.root)
        self.info_window.title("Player Details")
        self.info_window.geometry("400x400")
        self.info_window.configure(bg="#00008B")
        self.selected_difficulty = None  # Reset difficulty selection

        # Title label
        tk.Label(self.info_window, text="Enter Your Details",
                 fg="white", bg="#00008B", font=self.subtitle_font).pack(pady=10)

        # Name input frame
        name_frame = tk.Frame(self.info_window, bg="#00008B")
        name_frame.pack(pady=5)
        
        tk.Label(name_frame, text="First Name:", fg="white", bg="#00008B", 
                font=self.body_font).pack(side=tk.LEFT)
        
        # Regular entry field without validation
        self.first_name = tk.Entry(name_frame, font=self.body_font)
        self.first_name.pack(side=tk.LEFT)
        self.first_name.focus()  # Set focus to name entry

        # Name requirements hint
        tk.Label(self.info_window, text="(2-20 letters, spaces or hyphens)", 
                fg="lightgray", bg="#00008B", font=self.small_font).pack()

        # Difficulty selection label
        tk.Label(self.info_window, text="Select Difficulty:",
                 fg="white", bg="#00008B", font=self.body_font).pack(pady=10)

        # Difficulty selection status label
        self.difficulty_label = tk.Label(self.info_window, text="No difficulty selected",
                                       fg="yellow", bg="#00008B", font=self.body_font)
        self.difficulty_label.pack()

        # Difficulty buttons frame
        diff_frame = tk.Frame(self.info_window, bg="#00008B")
        diff_frame.pack()

        # Create difficulty selection buttons
        easy_button = tk.Button(diff_frame, text="Easy", width=8, command=self.set_easy)
        self.style_button(easy_button)
        easy_button.pack(side=tk.LEFT, padx=5)

        medium_button = tk.Button(diff_frame, text="Medium", width=8, command=self.set_medium)
        self.style_button(medium_button)
        medium_button.pack(side=tk.LEFT, padx=5)

        hard_button = tk.Button(diff_frame, text="Hard", width=8, command=self.set_hard)
        self.style_button(hard_button)
        hard_button.pack(side=tk.LEFT, padx=5)

        # Start questions button
        submit_button = tk.Button(self.info_window, text="Start questions", command=self.validate_submission)
        self.style_button(submit_button)
        submit_button.pack(pady=20)

    def set_easy(self):
        """Set difficulty to easy and update display"""
        self.selected_difficulty = "easy"
        self.difficulty_label.config(text="Selected: Easy", fg="lightgreen")

    def set_medium(self):
        """Set difficulty to medium and update display"""
        self.selected_difficulty = "medium"
        self.difficulty_label.config(text="Selected: Medium", fg="orange")

    def set_hard(self):
        """Set difficulty to hard and update display"""
        self.selected_difficulty = "hard"
        self.difficulty_label.config(text="Selected: Hard", fg="red")

    def validate_submission(self):
        """Validate player info before starting questions"""
        first_name = self.first_name.get()
        
        # Validate first name
        if not re.match(r'^[a-zA-Z\- ]+$', first_name):
            messagebox.showerror("Invalid Name", "Name can only contain letters, spaces, and hyphens")
            self.first_name.focus()
            return

        if len(first_name) < 2:
            messagebox.showerror("Name is incorrect", "Name has to be  at least 2 characters")
            self.first_name.focus()
            return

        if not first_name:
            messagebox.showerror("Name is incorrect", "Name cannot be empty")
            self.first_name.focus()
            return
            
        if len(first_name) > 20:
            messagebox.showerror("Name is wrong", "Name cannot be more than 20 characters")
            self.first_name.focus()
            return
                
        # Check difficulty selected
        if not self.selected_difficulty:
            messagebox.showerror("Error", "Please select a difficulty level")
            return

        # Store player name and start questions
        self.player_name = first_name.strip()
        self.start_questions(self.selected_difficulty)
        self.info_window.destroy()

    def start_questions(self, level):
        """ display the questions interface"""
        # Set up questions questions and state
        self.current_questions = self.question_banks[level]
        self.current_index = 0
        self.score = 0
        self.user_answers = [""] * len(self.current_questions)

        # Create questions window
        self.questions_win = tk.Toplevel(self.root)
        self.questions_win.title(f"{level.capitalize()} questions")
        self.questions_win.geometry("600x550")
        self.questions_win.configure(bg="#00008B")

        # Timer setup
        timer_frame = tk.Frame(self.questions_win, bg="#00008B")
        timer_frame.pack(fill="x", pady=10)
        
        # Center timer with empty labels for spacing
        tk.Label(timer_frame, bg="#00008B").pack(side="left", expand=True)
        
        self.time_left = 120  # 2 minutes in seconds
        self.timer_label = tk.Label(timer_frame, text="Time: 02:00",
                                  fg="white", bg="#00008B", font=self.timer_font)
        self.timer_label.pack(side="left")
        
        tk.Label(timer_frame, bg="#00008B").pack(side="left", expand=True)
        
        self.update_timer()  # Start timer

        # Image display area (for questions with images)
        self.image_frame = tk.Frame(self.questions_win, bg="#00008B")
        self.current_image_label = tk.Label(self.image_frame, bg="#00008B")

        # Question display
        self.question_label = tk.Label(self.questions_win, text="", wraplength=500,
                                     fg="white", bg="#00008B", font=self.body_font)
        self.question_label.pack(pady=10)

        # Answer input
        self.answer_entry = tk.Entry(self.questions_win, font=self.body_font)
        self.answer_entry.pack(pady=10)
        self.answer_entry.focus()

        # Navigation buttons
        button_frame = tk.Frame(self.questions_win, bg="#00008B")
        button_frame.pack(pady=10)

        back_button = tk.Button(button_frame, text="Back", command=self.go_back)
        self.style_button(back_button)
        back_button.pack(side=tk.LEFT, padx=10)

        submit_button = tk.Button(button_frame, text="Submit", command=self.check_answer)
        self.style_button(submit_button)
        submit_button.pack(side=tk.LEFT, padx=10)

        # Feedback label (for correct/incorrect messages)
        self.feedback_label = tk.Label(self.questions_win, text="",
                                     fg="yellow", bg="#00008B", font=self.feedback_font)
        self.feedback_label.pack()

        # Show first question
        self.show_current_question()
