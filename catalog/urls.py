from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manumissions/', views.ManumissionListView.as_view(), name='manumissions'),
    path('manumission/<int:pk>', views.ManumissionDetailView.as_view(), name='manumission-detail'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('about', views.about, name='about'),
    path('visualizations', views.visualizations, name='visualizations')
]

urlpatterns += [  
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]

urlpatterns += [  
    path('manumission/create/', views.ManumissionCreate.as_view(), name='manumission_create'),
    path('manumission/<int:pk>/update/', views.ManumissionUpdate.as_view(), name='manumission_update'),
    path('manumission/<int:pk>/delete/', views.ManumissionDelete.as_view(), name='manumission_delete'),
]