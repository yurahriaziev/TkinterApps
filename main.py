import customtkinter as ctk
from db import create_table, add_new_user

class BankApp:
    def __init__(self):
        # themes
        # ctk.set_appearance_mode("Dark")
        # ctk.set_default_color_theme("blue")

        # creating window
        self.window = ctk.CTk()
        # setting window parameters
        self.window.geometry("800x500")
        self.window.title("My Bank")
        self.window.resizable(0, 0)

        # creating text font, (font, font size)
        self.title_font = ("Baloo Bhai 2", 50)
        self.font = 'Baloo Bhai 2'
        # self.font = 'Krungthep'

        # creating DB
        create_table('users', 'first_n TEXT', 'last_n TEXT', 'username TEXT', 'email TEXT', 'bd_month TEXT', 'bd_day INTEGER', 'bd_year INTEGER', 'password TEXT')
        
    def boot(self):
        # creating the title frame, the top grey box (where to place it, width, height, background color)
        title_frame = ctk.CTkFrame(self.window, width=550, height=150, fg_color='#c7c7c7')
        title_frame.place(x=125, y=25)

        # creating "My Bank" title (where, text for the title, font, color)
        self.bank_title = ctk.CTkLabel(
            title_frame,
            text='My Bank',
            font=self.title_font,
            text_color='black'
        )
        self.bank_title.place(in_=title_frame, x=185, y=40)



        # login frame
        self.login_frame = ctk.CTkFrame(self.window, width=300, height=250)
        self.login_frame.place(x=50, y=225)

        # login text, text box, button
        login_text = ctk.CTkLabel(
            self.login_frame,
            text="Welcome Back!",
            font=("Baloo Bhai 2", 25)
        )
        login_text.place(x=70, y=20)

        self.login_user = ctk.CTkEntry(self.login_frame, height=50, width=200, placeholder_text="Your Username", font=(self.font, 20))
        self.login_user.place(x=50, y=80)
        self.login_password = ctk.CTkEntry(self.login_frame, height=50, width=200, placeholder_text="Your Password", font=(self.font, 20))
        self.login_password.place(x=50, y=140)

        login_btn = ctk.CTkButton(self.login_frame, text='Sign In', command=self.process_login)
        login_btn.place(x=80, y=205)

        # signup frame
        self.signup_frame = ctk.CTkFrame(self.window, width=300, height=250)
        self.signup_frame.place(x=450, y=225)
        # signup text, text box, button
        signup_text_1 = ctk.CTkLabel(
            self.signup_frame,
            text="New?",
            font=("Baloo Bhai 2", 25)
        )
        signup_text_2 = ctk.CTkLabel(
            self.signup_frame,
            text="Create an account with us",
            font=("Baloo Bhai 2", 20)
        )

        signup_btn = ctk.CTkButton(self.signup_frame, text='Sign Up', command=self.send_to_signup, height=80, font=(self.font, 20))
        signup_btn.place(x=80, y=100)

        signup_text_1.place(x=120, y=10)
        signup_text_2.place(x=35, y=50)

        self.window.mainloop()

    # any functions go in this section
    def process_login(self):
        print(f'User {self.login_user.get()}')
        print(f'Pass {self.login_password.get()}')

    def process_signup(self):
        first = self.f_name.get()
        last = self.l_name.get()
        if first == '' or last == '':
            error = ctk.CTkLabel(self.create_acc_frame1, text='Please enter your name', text_color='red', bg_color="transparent")
            error.place(x=128, y=230)
        else:
            self.page = ctk.CTkFrame(self.window, width=800, height=500)
            self.page.place(x=0, y=0)

            self.create_acc_frame2 = ctk.CTkFrame(self.page, width=400, height=360)
            self.create_acc_frame2.place(x=200, y=60)

            welcome_text = ctk.CTkLabel(self.page, text=f"Hey {first}!", font=(self.font, 25))
            welcome_text.place(x=210, y=20)

            email_text = ctk.CTkLabel(self.create_acc_frame2, text="Your Email", font=(self.font, 15))
            email_text.place(x=20, y=15)
            self.email = ctk.CTkEntry(self.create_acc_frame2, width=360, height=50)
            self.email.place(x=20, y=45)

            username_text = ctk.CTkLabel(self.create_acc_frame2, text="Pick a Username", font=(self.font, 15))
            username_text.place(x=20, y=105)
            self.user_field = ctk.CTkEntry(self.create_acc_frame2, width=360, height=50)
            self.user_field.place(x=20, y=135)

            birth_date_text = ctk.CTkLabel(self.create_acc_frame2, text="When were you born?", font=(self.font, 15))
            birth_date_text.place(x=20, y=195)
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            self.month = ctk.CTkOptionMenu(self.create_acc_frame2, values=months, width=100, fg_color='#4574ad', text_color='white')
            self.month.place(x=20, y=225)
            self.day = ctk.CTkEntry(self.create_acc_frame2, width=100, placeholder_text='Day', fg_color='#4574ad', border_width=0, placeholder_text_color='white', text_color='white')
            self.day.place(x=150, y=225)
            self.year = ctk.CTkEntry(self.create_acc_frame2, width=100, placeholder_text='Year', fg_color='#4574ad', border_width=0, placeholder_text_color='white', text_color='white')
            self.year.place(x=280, y=225)

            password_text = ctk.CTkLabel(self.create_acc_frame2, text="Enter your Password", font=(self.font, 15))
            password_text.place(x=20, y=265)
            self.password = ctk.CTkEntry(self.create_acc_frame2, width=360, height=50)
            self.password.place(x=20, y=295)

            submit_btn = ctk.CTkButton(self.page, width=360, height=50, text='Create your account!', font=(self.font, 20), command=self.add_user)
            submit_btn.place(x=220, y=430)

    def send_to_signup(self):
        self.signup_p1 = ctk.CTkFrame(self.window, width=800, height=500)
        self.signup_p1.place(x=0, y=0)

        self.create_acc_frame1 = ctk.CTkFrame(self.signup_p1, width=400, height=350)
        self.create_acc_frame1.place(x=200, y=100)

        self.ask_name = ctk.CTkLabel(self.create_acc_frame1, text='First, lets get your name', font=(self.font, 35), fg_color='transparent')
        self.ask_name.place(x=20, y=5)

        self.f_text = ctk.CTkLabel(self.create_acc_frame1, text='First Name', height=20)
        self.f_text.place(x=25, y=75)
        self.f_name = ctk.CTkEntry(self.create_acc_frame1, width=360, height=50, font=(self.font, 30))
        self.f_name.place(x=20, y=100)
        self.l_text = ctk.CTkLabel(self.create_acc_frame1, text='Last Name', height=20)
        self.l_text.place(x=25, y=155)
        self.l_name = ctk.CTkEntry(self.create_acc_frame1, width=360, height=50, font=(self.font, 30))
        self.l_name.place(x=20, y=180)

        cont_btn = ctk.CTkButton(self.signup_p1, width=150, height=75, text='Next', command=self.process_signup, font=(self.font, 25))
        cont_btn.place(x=325, y=370)

    def add_user(self):
        # call the db function to add user to db
        print(f'New user: {self.f_name.get()} {self.l_name.get()} | {self.user_field.get()} | {self.email.get()} | {self.month.get()} {self.day.get()}, {self.year.get()}')
        # first_n TEXT', 'last_n TEXT', 'username TEXT', 'email TEXT', 'bd_month TEXT', 'bd_day INTEGER', 'bd_year
        add_new_user('users', first_n=self.f_name.get(), last_n=self.l_name.get(), username=self.user_field.get(), email=self.email.get(), bd_month=self.month.get(), bd_day=self.day.get(), bd_year=self.year.get(), password=self.password.get())
        

if __name__ == "__main__":
    app = BankApp()
    app.boot()
