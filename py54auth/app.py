from auth_system.authentication_service import AuthSystem
from registration_system.registration_service import RegistrationSystem


class App:
    MENU = {
        "l": AuthSystem.auth,
        "r": RegistrationSystem.sign_up,
        "ex": None,
    }

    def run(self):
        command = input("Your choice please (login | register | exit)")
        if command == "ex":
            quit()
        try:
            do = self.MENU[command]
            do()
        except KeyError:
            print("Unknown command try again next time")


app = App()
app.run()
