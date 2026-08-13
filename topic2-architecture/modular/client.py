from login_service import login
from realm_service import select_realm
from character_service import get_character


username = "GreenKnight"
realm_name = "Pyrewood Village"
character_name = "Bronzebeard"

login_message = login(username)
realm_message = select_realm(realm_name)
character = get_character(character_name)

print("LAUNCH NIGHT")
print("=" * 12)
print(login_message)
print(realm_message)
print(character)
