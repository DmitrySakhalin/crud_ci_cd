from rest_framework.routers import DefaultRouter
from django.urls import path
from django.http import JsonResponse

from logistic.views import ProductViewSet, StockViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)


def test_view(request):
    return JsonResponse({'ok': True})


urlpatterns = router.urls + [
    path('test/', test_view),
]
