from django.http import JsonResponse

# Create your views here.


def test_view(request):
    print(request.GET.get('ssh'))
    return JsonResponse({'code': 200})
