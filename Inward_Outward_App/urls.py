from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('login', views.login),
    path('registration', views.registration),
    path('AddUser', views.AddUser),
    path('GetEmp', views.FetchUser),
    path('Dashboard', views.Dashboard),
    path("AddEditInward", views.AddEditInward),
    path("ManageUsers", views.FetchUser),
    path("delete", views.DeleteUser),
    path('Logout', views.Logout),
    path('AddEditNewInward', views.Add_Edit_New_Inward),
    path('ManageInward', views.ManageInward),
    # path('Users/<int:UserID>', views.Users),
    # path('Users/<str:UserID>', views.Users),
    # path('Users/<slug:UserID>', views.Users),
    path('Users/<UserID>', views.Users),

]
