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
        self.feedback_font = ("Helvetica",11, "italic")  
        self.timer_font = ("Helvetica", 12, "bold")  #Font for Timer
        self.small_font = ("Helvetica",8)  

        # Question banks
        self.question_banks = {
            "easy" : self.create_easy_questions(),  #Easy Question Function
            "medium":self.create_medium_questions(),  #Medium Question Function
            "hard" : self.create_hard_questions()  #Hard Question Function
        }

if __name__ == "__main__":
    # Create and run the game when script is executed directly
    MathGame()
