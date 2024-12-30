import tkinter as tk
from tkinter import messagebox
from task_manager import tasks, add_task, assign_tasks
from family_manager import family_members, get_preferences, preferences, update_preferences, add_family_member, remove_family_member

# Funkcja dodająca zadanie
def add_task_to_queue():
    task_name = task_name_entry.get().strip()
    task_duration = task_duration_entry.get().strip()

    if not task_name or not task_duration.isdigit():
        messagebox.showerror("Błąd", "Podaj poprawne dane zadania!")
        return

    add_task(task_name, task_duration)  # Użycie funkcji z task_manager.py do dodania zadania
    messagebox.showinfo("Sukces", f"Zadanie '{task_name}' dodane!")
    task_name_entry.delete(0, tk.END)
    task_duration_entry.delete(0, tk.END)
    update_tasks_list()

# Funkcja przypisująca zadania
def assign_family_tasks():
    assignments_listbox.delete(0, tk.END)
    # Użycie funkcji assign_tasks z task_manager.py do przypisania zadań
    assignments = assign_tasks(family_members, preferences)
    for assignment in assignments:
        assignments_listbox.insert(tk.END, assignment)
    update_tasks_list()  # Aktualizacja listy zadań po przypisaniu

# Funkcja aktualizująca listę zadań
def update_tasks_list():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, f"{task['task']} - {task['duration']} min")

# Funkcja aktualizująca preferencje
def update_family_preferences():
    member = family_member_preferences_entry.get().strip()
    likes = family_member_likes_entry.get().strip().split(",")
    dislikes = family_member_dislikes_entry.get().strip().split(",")

    if not member:
        messagebox.showerror("Błąd", "Podaj imię członka rodziny!")
        return

    # funkcja update_preferences z task_manager.py do zaktualizowania preferencji
    update_preferences(member, likes, dislikes)
    messagebox.showinfo("Sukces", f"Preferencje dla {member} zostały zaktualizowane!")
    update_preferences_list()
    family_member_preferences_entry.delete(0, tk.END)
    family_member_likes_entry.delete(0, tk.END)
    family_member_dislikes_entry.delete(0, tk.END)

# Funkcja aktualizująca listę preferencji
def update_preferences_list():
    preferences_listbox.delete(0, tk.END)
    for member, pref in preferences.items():
        preferences_listbox.insert(tk.END, f"{member}: Lubi: {', '.join(pref['likes'])}, Nie lubi: {', '.join(pref['dislikes'])}")

# Funkcja dodająca członka rodziny
def add_family_member_to_list():
    member_name = family_member_name_entry.get().strip()

    if not member_name:
        messagebox.showerror("Błąd", "Podaj imię członka rodziny!")
        return

    try:
        add_family_member(member_name)
        messagebox.showinfo("Sukces", f"Członek rodziny '{member_name}' dodany!")
        family_member_name_entry.delete(0, tk.END)
        update_preferences_list()
    except ValueError as e:
        messagebox.showerror("Błąd", str(e))

# Funkcja usuwająca członka rodziny
def remove_family_member_from_list():
    member_name = family_member_name_entry.get().strip()

    if not member_name:
        messagebox.showerror("Błąd", "Podaj imię członka rodziny do usunięcia!")
        return

    try:
        remove_family_member(member_name)
        messagebox.showinfo("Sukces", f"Członek rodziny '{member_name}' usunięty!")
        family_member_name_entry.delete(0, tk.END)
        update_preferences_list()
    except ValueError as e:
        messagebox.showerror("Błąd", str(e))

# GUI layout
root = tk.Tk()
root.title("Zarządzanie zadaniami domowymi")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Dodawanie zadania
tk.Label(frame, text="Nazwa zadania:").grid(row=0, column=0, padx=5, pady=5)
task_name_entry = tk.Entry(frame)
task_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Czas trwania (min):").grid(row=1, column=0, padx=5, pady=5)
task_duration_entry = tk.Entry(frame)
task_duration_entry.grid(row=1, column=1, padx=5, pady=5)

add_task_button = tk.Button(frame, text="Dodaj zadanie", command=add_task_to_queue)
add_task_button.grid(row=2, column=0, columnspan=2, pady=5)

tasks_listbox = tk.Listbox(frame, height=10)
tasks_listbox.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# przycisk przydzielania zadania 
assign_tasks_button = tk.Button(frame, text="Przydziel zadania", command=assign_family_tasks)
assign_tasks_button.grid(row=4, column=0, columnspan=2, pady=5)

# przydzielone zadania
assignments_listbox = tk.Listbox(frame, height=10)
assignments_listbox.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Preferencje członków rodziny
preferences_frame = tk.LabelFrame(root, text="Preferencje członków rodziny")
preferences_frame.pack(fill="x", padx=10, pady=5)

tk.Label(preferences_frame, text="Imię członka rodziny:").grid(row=0, column=0, padx=5, pady=5)
family_member_preferences_entry = tk.Entry(preferences_frame)
family_member_preferences_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(preferences_frame, text="Zadania, które lubi (oddzielone przecinkiem):").grid(row=1, column=0, padx=5, pady=5)
family_member_likes_entry = tk.Entry(preferences_frame)
family_member_likes_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(preferences_frame, text="Zadania, których nie lubi (oddzielone przecinkiem):").grid(row=2, column=0, padx=5, pady=5)
family_member_dislikes_entry = tk.Entry(preferences_frame)
family_member_dislikes_entry.grid(row=2, column=1, padx=5, pady=5)

update_preferences_button = tk.Button(preferences_frame, text="Zaktualizuj preferencje", command=update_family_preferences)
update_preferences_button.grid(row=3, column=0, columnspan=2, pady=5)

preferences_listbox = tk.Listbox(preferences_frame, height=5)
preferences_listbox.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Dodawanie / usuwanie członków rodziny
family_members_frame = tk.LabelFrame(root, text="Członkowie rodziny")
family_members_frame.pack(fill="x", padx=10, pady=5)

tk.Label(family_members_frame, text="Imię członka rodziny:").grid(row=0, column=0, padx=5, pady=5)
family_member_name_entry = tk.Entry(family_members_frame)
family_member_name_entry.grid(row=0, column=2, padx=5, pady=5)

add_family_member_button = tk.Button(family_members_frame, text="Dodaj członka rodziny", command=add_family_member_to_list)
add_family_member_button.grid(row=1, column=0, pady=5)
remove_family_member_button = tk.Button(family_members_frame, text="Usuń członka rodziny", command=remove_family_member_from_list)
remove_family_member_button.grid(row=1, column=2, pady=5)

# wywołanie list przy starcie aplikacji 
update_tasks_list()
update_preferences_list()

root.mainloop()
