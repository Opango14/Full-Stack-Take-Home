from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .translation import translate_text

def index(request):
    return render(request, 'translate/index.html')

@csrf_exempt
@require_http_methods(["POST"])
def translate_text_api(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        text = data.get("text", "")
        target_language = data.get("targetLanguage", "")

        if not text:
            return JsonResponse({"error": "Text field is required"}, status=400)
        if target_language not in ["en", "sw"]:
            return JsonResponse({"error": "Language not found"}, status=400)

        translated_text = translate_text(text, target_language)

        return JsonResponse({
            "translatedText": translated_text
        })
    
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid Format"}, status=400)
    except Exeption as e:
        return JsonResponse({"error": str(e)}, status=500)
