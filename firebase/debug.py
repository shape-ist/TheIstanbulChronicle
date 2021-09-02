from firebase import user


def init_user():
    return user.register(f"debug@debug.com", "debug1234", "Ada Lovelace")


def debug_user():
    return user.login(f"debug@debug.com", "debug1234")
