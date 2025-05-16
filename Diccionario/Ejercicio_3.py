Users = {
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"},
}

Attempts = 1

def CheckRequestedInfo(Username: str, Password: str) -> bool :
    UserListInfo = Users.get(Username)
    
    if (UserListInfo != None and UserListInfo.get("password") == Password):
        return False
    
    return True

while (Attempts <= 3):
    UsernameRequest = input()
    PasswordRequest = input()
    
    if (CheckRequestedInfo(UsernameRequest, PasswordRequest)):
        print(f"Intentelo de nuevo: intentos {3 - Attempts}")
        Attempts += 1
        continue
    else:
        print(f"----| Welcome {UsernameRequest}")
        exit()

print("----| Acceso Denegado")