from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import WordPair

# Create your views here.
def index(request):
    return render(request, 'main/index_local.html')

def indexRest(request):
    return render(request, 'main/index_rest.html')

def getAllWords(request):
    pairs = list(WordPair.objects.all().values())
    return JsonResponse(pairs, safe=False)

def getWordById(request, id):
    pairs = list(WordPair.objects.filter(id=id).values())
    return JsonResponse(pairs, safe=False)

def getWordsByField(request, field):
    pairs = list(WordPair.objects.filter(field=field).values())
    return JsonResponse(pairs, safe=False)

def addWord(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            WordPair.objects.create(
                sourceLang=body['sourceLang'],
                sourceWord=body['sourceWord'],
                targetLang=body['targetLang'],
                targetWord=body['targetWord'],
                field=body['field']
            )
            return JsonResponse({'message':'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'message':'failed'}, status=400)
    return JsonResponse({'message':'failed'}, status=405)

def deleteWordById(request, id):
    if request.method == 'DELETE':
        get_object_or_404(WordPair, id=id).delete()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'failed'}, status=405)

def updateWordById(request, id):
    if request.method == 'PUT':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            pair = WordPair.objects.get(id=id)
            pair.sourceLang = body['sourceLang']
            pair.sourceWord = body['sourceWord']
            pair.targetLang = body['targetLang']
            pair.targetWord = body['targetWord']
            pair.field = body['field']
            pair.save()
            return JsonResponse({'message':'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'message':'failed'}, status=400)
    return JsonResponse({'message':'failed'}, status=405)
