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
