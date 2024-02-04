from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/',views.MenuItemDetails.as_view(), name='menu_item'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)