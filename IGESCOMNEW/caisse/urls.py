from django.urls import path
from caisse.views import Articles, ArticleDetail,Paniers, PanierDetail

urlpatterns = [
    path('', Articles.as_view()),
    path('<str:pk>', ArticleDetail.as_view()),
    # path('panier/', Paniers.as_view()),
    # path('<str:pk>', PanierDetail.as_view()),
]
