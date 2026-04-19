from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from wishApp.models import Wish
from wishApp.serializers import WishSerializer

@csrf_exempt
def wish_list(request):
    if request.method == 'GET':
        wishes = Wish.objects.all()
        serializer = WishSerializer(wishes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WishSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def wish_detail(request, pk):
    try:
        wish = Wish.objects.get(pk=pk)
    except Wish.DoesNotExist:
        return JsonResponse({"error": "Wish not found"}, status=404)

    if request.method == 'GET':
        serializer = WishSerializer(wish)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WishSerializer(wish, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        wish.delete()
        # Ensure this is an HttpResponse as requested, not a JsonResponse
        return HttpResponse(status=204)