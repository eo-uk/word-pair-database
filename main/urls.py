from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rest', views.indexRest, name="indexRest"),
    path('api/words', views.getAllWords, name="getAllWords"),
    path('api/words/id/<int:id>', views.getWordById, name="getWordById"),
    path('api/words/field/<str:field>', views.getWordsByField, name="getWordsByField"),
    path('api/words/add', views.addWord, name="addWord"),
    path('api/words/delete/<int:id>', views.deleteWordById, name="deleteWordById"),
    path('api/words/update/<int:id>', views.updateWordById, name="updateWordById"),
]