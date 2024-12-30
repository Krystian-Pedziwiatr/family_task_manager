
family_members = ["Kamil", "Ola", "Julia", "Kacper"]


preferences = {
    "Kamil": {"likes": [], "dislikes": ["Sprzątanie kuchni", "Mycie okien"]},
    "Ola": {"likes": ["Zakupy spożywcze"], "dislikes": []},
    "Julia": {"likes": ["Gotowanie obiadu"], "dislikes": []},
    "Kacper": {"likes": [], "dislikes": []},
}

def add_family_member(name):
  
    if name:
        if name not in family_members:
            family_members.append(name)  # Dodanie członka rodziny
            preferences[name] = {"likes": [], "dislikes": []}  # Domyślne preferencje
        else:
            raise ValueError(f"Członek rodziny '{name}' już istnieje!")  
    else:
        raise ValueError("Imię członka rodziny nie może być puste!")  

def remove_family_member(name):

    if name in family_members:
        family_members.remove(name)  
        preferences.pop(name, None)  
    else:
        raise ValueError(f"Członek rodziny '{name}' nie istnieje!")  

def get_family_members():
   
    return family_members  # Zwraca listę członków rodziny

def update_preferences(name, likes=None, dislikes=None):
  
    if name not in preferences:
        raise ValueError(f"Członek rodziny '{name}' nie istnieje!")  

    if likes is not None:
        preferences[name]["likes"] = likes  
    if dislikes is not None:
        preferences[name]["dislikes"] = dislikes  

def get_preferences():
   
    return preferences  # Zwracamy słownik preferencji
