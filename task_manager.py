from collections import deque

# Kolejka zadań (FCFS - First Come First Served)
tasks = deque()

# Domyślne zadania obowiązkowe
default_tasks = [
    {"task": "Sprzątanie kuchni", "duration": 30},
    {"task": "Odkurzanie salonu", "duration": 20},
    {"task": "Pranie ubrań", "duration": 60},
    {"task": "Mycie okien", "duration": 90},
    {"task": "Zakupy spożywcze", "duration": 45},
    {"task": "Gotowanie obiadu", "duration": 60},
]

# Inicjalizacja kolejki zadań
tasks.extend(default_tasks)

def add_task(task_name, task_duration):
  
    if any(task['task'] == task_name for task in tasks):
        raise ValueError(f"Zadanie '{task_name}' już istnieje w kolejce!")
    
    # Dodaje zadanie do końca kolejki
    tasks.append({"task": task_name, "duration": int(task_duration)})

def assign_tasks(family_members, preferences):
  

    if not family_members:
        raise ValueError("Brak członków rodziny do przypisania zadań!")
    if not tasks:
        raise ValueError("Brak zadań do przypisania!")

    assignments = []  # Lista przypisanych zadań
    task_queue = tasks.copy()  # Tworzymy kopię kolejki, aby nie modyfikować oryginalnej

    member_idx = 0  # Zaczynamy od pierwszego członka rodziny
    while task_queue:
        current_task = task_queue.popleft()  # Pobieramy zadanie z początku kolejki
        member = family_members[member_idx]  # Bierzemy kolejnego członka rodziny
        
        # Sprawdzamy preferencje danego członka
        if current_task["task"] in preferences[member]["dislikes"]:
            # Jeśli członek nie lubi zadania, przekazujemy je dalej
            assignments.append(f"{member} -> {current_task['task']} (nie lubi), przekazywane dalej")
            task_queue.append(current_task)  # Przekazujemy zadanie na koniec kolejki
        else:
            # Jeśli członek lubi zadanie, przypisujemy je temu członkowi
            assignments.append(f"{member} -> {current_task['task']} ({current_task['duration']} min)")

        # Przechodzimy do następnego członka rodziny
        member_idx = (member_idx + 1) % len(family_members)

    return assignments

def get_tasks():
   
    return list(tasks)  # Zwraca kopię listy zadań
