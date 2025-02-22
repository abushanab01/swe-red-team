# incollege_app.py

import re
from deep_translator import GoogleTranslator

class InCollegeApp:
    def __init__(self):
        self.user_credentials = {
            "test" : {
                'password': "test",
                'first_name': "test",
                'last_name': "test",
                'login_status': False
            },
        }  # Dictionary to store username and password
        self.MAX_ACCOUNTS = 5  # Maximum number of accounts
        self.job_posts = []  # List to store job posts
        
        self.language = "english"  # Default language
        self.email = False  # Email notification status
        self.sms = False  # SMS notification status
        self.targeted_advertising = False  # Targeted ads status
        
        """
        self.translations = {
            "Spanish": {
                "Welcome to InCollege": "Bienvenido a InCollege",
                "Main Menu": "Menú principal",
                "Under construction.": "En construcción.",
            }
        }
        """

    def create_account(self, username, password):
        # Check if maximum number of accounts has been reached
        if len(self.user_credentials) >= self.MAX_ACCOUNTS:
            return self.translate_language("Maximum number of student accounts created.")

        # restrictions for password
        if len(password) < 8 or len(password) > 13:
            return self.translate_language("Password must be between 8 and 13 characters.")
        if not re.search(r"[A-Z]", password):
            return self.translate_language("Password must contain at least one capital letter.")
        if not re.search(r"\d", password):
            return self.translate_language("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*()_+{}|:\"<>?]", password):
            return self.translate_language("Password must contain at least one special character.")
        
        first_name = input(self.translate_language("Enter your first name: "))
        last_name = input(self.translate_language("Enter your last name: "))

        self.user_credentials[username] = {
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'login_status': True
        }

        print(self.translate_language("Account created successfully"))
        self.get_post_login_options()
        
        
        # [old code]
        # Check if username already exists
        # self.user_credentials[username] = [password, 0]
        # return "Account created successfully"
        

    def login(self, username, password):
        # Check if username and password match
        if username in self.user_credentials and self.user_credentials[username]['password'] == password:
            # [old code]
            # self.user_credentials[username][1] += 1
            self.user_credentials[username]['login_status'] = True
            return self.translate_language("You have successfully logged in")
        return self.translate_language("Incorrect username / password, please try again.")
    
    #---------------- epic 1 -----------------#

    def get_post_login_options(self):
        
        # added a new option to the list #4 for epic#2
        options_list = [
            "1. Job search/Internship",
            "2. Find someone you know",
            "3. Learn a new skill",
            "4. Useful Links",
            "5. InCollege Important Links",
            "6. Log out"
        ]
        select_option = "\n".join(options_list)
        print(self.translate_language(select_option))
        selected_option = input(self.translate_language("Select an option: "))
        self.select_option(selected_option)
        

    def select_option(self, option_number):

        # added a new option to the list #4 for epic#2
        if option_number == "1":
            return self.under_construction()
        elif option_number == "2":
            self.find_person()
        elif option_number == "3":
            self.list_skills()
        elif option_number == "4":
            self.display_useful_links()
        elif option_number == "5":
            self.important_links()
        elif option_number == "6":
            print(self.translate_language("You have successfully logged out."))
            self.main_menu()
            # or return self.main_menu() for future development
        else:
            print(self.translate_language("Invalid Option"))

    def list_skills(self):
        skills = [
            "1. Programming",
            "2. Data Analysis",
            "3. Graphic Design",
            "4. Digital Marketing",
            "5. Project Management",
            "6. return to previous level"
        ]
        skill_options = "\n".join(skills)
        print(self.translate_language(skill_options))
        print("\nSelect a skill to learn.")
        selected_skill = input(self.translate_language("Enter a number: "))
        self.select_skill(selected_skill)
    
    def select_skill(self, skill_number):
        if skill_number in ["1", "2", "3", "4", "5"]:
            print(self.under_construction())
        elif skill_number == "6":
            self.get_post_login_options()
        else:
            print(self.translate_language("Invalid Option"))
        
    #---------------- epic 2 -----------------#
        
    def display_success_story_and_video_option(self):
        success_story = "Meet Hideo Kojima, a recent graduate who landed their dream job at a top tech company using InCollege."
        print(self.translate_language(success_story))

        play_video_option = input(self.translate_language("Would you like to watch a video?") + " (y/n): ")
        if play_video_option.lower() == "y":
            print(self.translate_language("Video is now playing."))
        else:
            print(self.translate_language("Thank you for visiting InCollege."))\
        
    def post_job(self,username):
        if len(self.job_posts) >= 5:
            print(self.translate_language("Maximum number of jobs posted. Please try again later."))

        title = input(self.translate_language("Enter job title: "))
        description = input(self.translate_language("Enter job description: "))
        employer = input(self.translate_language("Enter employer: "))
        location = input(self.translate_language("Enter location: "))
        salary = input(self.translate_language("Enter salary: "))

        self.job_posts.append({
            'title': title,
            'description': description,
            'employer': employer,
            'location': location,
            'salary': salary,
            'username': username
        })

        print(self.translate_language("Job posted successfully."))
    
    def find_person(self):
        first_name = input(self.translate_language("Enter the first name of the person you are looking for: "))
        last_name = input(self.translate_language("Enter the last name of the person you are looking for: "))

        for user_info in self.user_credentials.values():
            if user_info['first_name'].lower() == first_name and user_info['last_name'].lower() == last_name:
                print(self.translate_language("They are a part of the InCollege system."))
        print(self.translate_language("They are not a part of the InCollege system."))
    
    def main_menu(self):
        self.choose_language()
        menu_options = [
            "Welcome to InCollege",
            "Main Menu",
            "1. Create Account",
            "2. Login",
            "3. View Success Story and Video",
            "4. Exit",
            "5. Useful Links",
            "6. InCollege Important Links"
        ]
        menu = "\n".join(menu_options)
        print(self.translate_language(menu))
        
        # print("\nWelcome to InCollege")
        # print("\nMain Menu")
        # print("\n1. Create Account")
        # print("\n2. Login")
        # print("\n3. View Success Story and Video")
        # print("\n4. Exit")

        choice = input(self.translate_language("\nSelect an option: "))

        if choice == "1":
            username = input(self.translate_language("Enter your username: "))
            password = input(self.translate_language("Enter your password: "))
            self.create_account(username, password)
        elif choice == "2":
            username = input(self.translate_language("Enter your username: "))
            password = input(self.translate_language("Enter your password: "))
            login_result = self.login(username, password)
            print(login_result)
            if login_result == self.translate_language("You have successfully logged in"):
                self.get_post_login_options()
        elif choice == "3":
            self.display_success_story_and_video_option()
        elif choice == "4":
            print(self.translate_language("Thank you for visiting InCollege."))
        elif choice == "5":
            self.display_useful_links()
        elif choice == "6":
            self.important_links()
        else:
            print(self.translate_language("Invalid Option"))

    #---------------- epic 3 -----------------# task 1 and 2 from Kainan
    
    def any_user_logged_in(self):
        return any(user_info['login_status'] for user_info in self.user_credentials.values())

    def translate_language(self, msg):
        if self.language.lower() == 'spanish':
            translated = GoogleTranslator(source='en', target='es').translate(msg)
            return translated
        else:    
            return msg
    
    def under_construction(self):
        return self.translate_language("Under construction.")
    
    def display_useful_links(self):
        useful_links = [
            "1. General",
            "2. Browse InCollege",
            "3. Business Solutions",
            "4. Directories",
            "5. return to previous level"
        ]
        useful_links_options = "\n".join(useful_links)
        print(self.translate_language(useful_links_options))
        print(self.translate_language("\nSelect a link to view."))
        selected_link = input(self.translate_language("Enter a number: "))
        self.select_useful_link(selected_link)
        
    def select_useful_link(self, link_number):
        if link_number == "1":
            self.display_general_links()
        elif link_number in ["2", "3", "4"]:
            print(self.under_construction())
        elif link_number == "5":
            if self.any_user_logged_in():
                self.get_post_login_options()
            else:
                self.main_menu()
        else:
            print(self.translate_language("Invalid Option"))
        
    def display_general_links(self):
        general_links = [
            "1. Sign up",
            "2. Help Center",
            "3. About",
            "4. Press",
            "5. Blog",
            "6. Careers",
            "7. Developers",
            "8. Go back to previous level"
        ]
        general_links_options = "\n".join(general_links)
        print(self.translate_language(general_links_options))
        print(self.translate_language("\nSelect a link to view."))
        selected_link = input(self.translate_language("Enter a number: "))
        self.select_general_link(selected_link)
        
    def select_general_link(self, link_number):
        if link_number == "1":
            username = input(self.translate_language("Enter your username: "))
            password = input(self.translate_language("Enter your password: "))
            self.create_account(username, password)
        elif link_number == "2":
            print(self.translate_language("\nWe're here to help"))
        elif link_number == "3":
            print(self.translate_language("\nIn College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"))
        elif link_number == "4":
            print(self.translate_language("\nIn College Pressroom: Stay on top of the latest news, updates, and reports"))
        elif link_number in ["5", "6", "7"]:
            print(self.under_construction())
        elif link_number == "8":
            self.display_useful_links()
        else:
            print(self.translate_language("Invalid Option"))
    
    """
    def display_important_links(self):
        important_links = [
            "1. Copyright Notice",
            "2. About",
            "3. Brand Policy",
            "4. Guest Controls",
            "5. Languages",
            "6. return to previous level"
        ]
        important_links_options = "\n".join(important_links)
        print(important_links_options)
        print("\nSelect a link to view.")
        selected_link = input("Enter a number: ")
        self.select_important_link(selected_link)
    
    
    def select_important_link(self, link_number):
        if link_number in ["1", "2", "3", "4"]:
            return self.under_construction()
        elif link_number == "5":
            self.display_languages()
        elif link_number == "6":
            if self.any_user_logged_in():
                self.get_post_login_options()
            else:
                self.main_menu()
        else:
            return "Invalid Option"
        
    def display_languages(self):
        languages = [
            "1. English",
            "2. Spanish"
        ]
        languages_options = "\n".join(languages)
        print(languages_options)
        print("\nSelect a language.")
        selected_language = input("Enter a number: ")
        self.select_language(selected_language)
        
    def select_language(self, language_number):
        if language_number in ["1", "2"]:
            return self.set_language(language_number)
        else:
            return "Invalid Option"
    
    def set_language(self, language_number):
        if language_number == "1":
            self.current_language = "English"
        elif language_number == "2":
            self.current_language = "Spanish"
        
        if self.any_user_logged_in():
            self.get_post_login_options()
        else:
            self.main_menu()
            
    """
    #---------------- epic 3 -----------------# task 3 and 4 from Vynze
    
    def important_links(self):
        links = [
            "1. Copyright Notice",
            "2. About",
            "3. Accessibility",
            "4. User Agreement",
            "5. Privacy Policy",
            "6. Cookie Policy",
            "7. Copyright Policy",
            "8. Brand Policy",
            "9. Back to previous"
        ]
        link_options = "\n".join(links)
        return self.translate_language(link_options + "\nSelect a link to visit.")

    # will need to be changed if we are given information about the links
    def select_link(self, link_number):
        if link_number in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return self.translate_language("Under construction.")
        else:
            return self.translate_language("Invalid Option")
        
    def guest_controls(self):
        settings = [
            "1. Email",
            "2. SMS",
            "3. Targeted Advertising",
            "4. Back to previous"
        ]
        setting_options = "\n".join(settings)
        return self.translate_language(setting_options + "\nSelect a setting to change.")

    def toggle_guest_controls(self, setting_number):
        if setting_number in "1":
            self.email = not self.email
            return self.translate_language("Email notifications have been turned off.")
        elif setting_number in "2":
            self.sms = not self.sms
            return self.translate_language("SMS notifications have been turned off.")
        elif setting_number in "3":
            self.targeted_advertising = not self.targeted_advertising
            return self.translate_language("Targeted advertising has been turned off.")
        elif setting_number in "4":
            print(self.translate_language("Returning to Post Login.")) # i dont know where exiting this menu goes back to but i assume main menu
            return self.get_post_login_options()
        else:
            return self.translate_language("Invalid Option")
        
    def choose_language(self):
        language = input("Choose a language: ")
        if language.lower() in ['english', 'spanish']:
            self.language = language
            return f"Language has been set to {language}."
        else:
            return "Invalid language. Please choose English or Spanish."
