"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

from main_page import views as main_page_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Головна', main_page_views.index),
    path('Контакти/', main_page_views.contacts),
    # path('Батькам/Про інтернет-залежність', main_page_views.internet_addiction),
    path('Адміністрація', main_page_views.administration),
    path('STOP булінг', main_page_views.stop_buling),
    path('Безпечне освітнє середовище', main_page_views.s_e_e),
    path('Корисні посилання', main_page_views.corisni_posilanya),
    path('Статут', main_page_views.rozdil1_statut),
    path('Стратегія розвитку гімназії', main_page_views.strategiarozvitku),
    path('Освітні програми, що реалізуються в закладі', main_page_views.programs_yaki_rel_v_zakladi),
    path('Кадровий склад', main_page_views.teacherslist),
    path('Новини', include('news_page.urls'))
]
# Зробити корисні посилання!!

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)