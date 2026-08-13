def login(username):
    """Return a message confirming the player's login."""
    return f"Player: {username}\nLogin successful"


def select_realm(realm_name):
    """Return the selected game realm."""
    return f"Realm: {realm_name}"


def get_character(character_name):
    """Return basic information about a character."""
    return f"Character: {character_name} - Level 20 Warrior"


print("LAUNCH NIGHT")
print("=" * 12)
print(login("GreenKnight"))
print(select_realm("Pyrewood Village"))
print(get_character("Bronzebeard"))
