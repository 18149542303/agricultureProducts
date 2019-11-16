from django.http import JsonResponse


# Create your views here.
def test_view(request):
    if request.method == 'GET':
        pass



    if request.method == 'POST':
        pass


    return JsonResponse({'code': 200})


