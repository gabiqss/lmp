from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


# Caminhos para as url's dentro de project

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("accounts", include("accounts.urls")),
    path("instruments", include("instruments.urls")),
    path("ordem-servico", include("ordemS.urls")),
    path("calibracao", include("calibracao.urls")),
    path("orcamento", include("orcamento.urls")),
    path("checklist", include("checklist.urls")),
    path("procedimentos", include("procedimentos.urls")),
    path("comercial", include("comercial.urls")),
    path("padrao", include("padrao.urls")),
    path("procedimentoEletronico", include("procEletronicos.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
