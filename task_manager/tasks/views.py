from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import TaskForm
from .models import Task
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
@login_required
def Task_list(request):
    # Filtre par statut
    status_task = request.GET.get('statut', '')
    
    # Recherche par mot-clé
    search_query = request.GET.get('search', '')

    # Filtrage des tâches par statut et recherche par mot-clé
    if status_task and search_query:
        tasks = Task.objects.filter(status=status_task, tache__icontains=search_query).order_by('id')
    elif status_task:
        tasks = Task.objects.filter(status=status_task).order_by('id')
    elif search_query:
        tasks = Task.objects.filter(tache__icontains=search_query).order_by('id')
    else:
        tasks = Task.objects.all().order_by('id')
    
    paginator = Paginator(tasks, 2)  # 4 tâches par page
    page_number = request.GET.get('page')  # Obtenir le numéro de la page depuis l'URL
    page_obj = paginator.get_page(page_number)
        
    return render(request, 'task/task_list.html', {'page_obj': page_obj, 'search_query': search_query, 'status_task': status_task})

def ajouter_tache(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre les données dans la base de données
            return redirect('Task_list')  # Redirige vers la liste des tâches
    else:
        form = TaskForm()  # Crée un formulaire vide si l'utilisateur arrive sur la page
    return render(request, 'task/ajouter_tache.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Task

# Vue pour supprimer une tâche
def supprimer_tache(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('Task_list')  # Redirige vers la liste des tâches après suppression
    except Task.DoesNotExist:
        # Si la tâche n'existe pas
        return redirect('Task_list')  # Ou une page d'erreur personnalisée

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Assurez-vous d'avoir un formulaire TaskForm pour les tâches

# Vue pour modifier une tâche
def modifier_tache(request, task_id):
    # Récupérer la tâche à modifier
    task = get_object_or_404(Task, id=task_id)
    
    # Si la méthode est POST, on met à jour la tâche
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Sauvegarde la tâche modifiée
            return redirect('Task_list')  # Redirige vers la liste des tâches
    else:
        form = TaskForm(instance=task)  # Formulaire pré-rempli avec la tâche existante

    return render(request, 'task/modifier_tache.html', {'form': form, 'task': task})

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Créer l'utilisateur
            login(request, user)  # Connecter l'utilisateur après l'inscription
            return redirect('Task_list')  # Rediriger vers la liste des tâches après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'auth/inscription.html', {'form': form})

from django.contrib.auth.views import LoginView

# Pas besoin de code supplémentaire, utilisez la vue générique Django
class CustomLoginView(LoginView):
    template_name = 'auth/login.html'


# views.py
from django.contrib.auth.views import LogoutView

# Pas besoin de code supplémentaire, utilisez la vue générique Django
class CustomLogoutView(LogoutView):
    next_page = 'Task_list'  # Redirige vers la liste des tâches après la déconnexion
