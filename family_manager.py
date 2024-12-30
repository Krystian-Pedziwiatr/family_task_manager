
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
            family_members.append(name)  # Dodajemy członka rodziny
            preferences[name] = {"likes": [], "dislikes": []}  # Domyślne preferencje
        else:
            raise ValueError(f"Członek rodziny '{name}' już istnieje!")  # Błąd, jeśli członek już istnieje
    else:
        raise ValueError("Imię członka rodziny nie może być puste!")  # Błąd, jeśli imię jest puste

def remove_family_member(name):
    """
    Usuwa członka rodziny z listy.
    :param name: Imię członka rodziny
    """
    if name in family_members:
        family_members.remove(name)  # Usuwamy członka rodziny
        preferences.pop(name, None)  # Usuwamy preferencje tego członka
    else:
        raise ValueError(f"Członek rodziny '{name}' nie istnieje!")  # Błąd, jeśli członek nie istnieje

def get_family_members():
   
    return family_members  # Zwracamy listę członków rodziny

def update_preferences(name, likes=None, dislikes=None):
  
    if name not in preferences:
        raise ValueError(f"Członek rodziny '{name}' nie istnieje!")  # Błąd, jeśli członek nie istnieje

    if likes is not None:
        preferences[name]["likes"] = likes  # Aktualizujemy zadania, które członek lubi
    if dislikes is not None:
        preferences[name]["dislikes"] = dislikes  # Aktualizujemy zadania, które członek nie lubi

def get_preferences():
   
    return preferences  # Zwracamy słownik preferencji
