user = {"username": "João", "acess_level": "admin"}

def get_admin_password():
    return "Rubicho25!"


def secure_function(func):
    if user["acess_level"] == "admin":
        return func


get_admin_password = secure_function(get_admin_password)

print(get_admin_password())