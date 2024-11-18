from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required  # Pour protéger les pages avec login_required

urlpatterns = [
    # Inscription
    path('', views.inscription, name='inscription'),

    # Liste des tâches (accessible uniquement aux utilisateurs connectés)
    path('task_list/', login_required(views.Task_list), name='Task_list'),

    # Ajouter une tâche
    path('ajouter_tache/', login_required(views.ajouter_tache), name='ajouter_tache'),

    # Supprimer une tâche
    path('supprimer_tache/<int:task_id>/', login_required(views.supprimer_tache), name='supprimer_tache'),

    # Modifier une tâche
    path('modifier_tache/<int:task_id>/', login_required(views.modifier_tache), name='modifier_tache'),

    # Connexion et déconnexion
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='Task_list'), name='logout'),
]
