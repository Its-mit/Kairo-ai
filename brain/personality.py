from memory import load_profile

def get_profile():
    return load_profile()

def get_name():
    profile = get_profile()

    if profile:
        return profile.get("name", "User")

    return "User"


def get_greeting():
    profile = get_profile()

    if profile:

        gender = profile.get("gender", "").lower()

        if gender == "male":
            return "sir"

        elif gender == "female":
            return "mam"

    return "friend"


def get_wake_word():
    profile = get_profile()

    if profile:
        return profile.get("wake_word", "kairo")

    return "kairo"

