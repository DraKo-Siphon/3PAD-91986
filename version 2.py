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
