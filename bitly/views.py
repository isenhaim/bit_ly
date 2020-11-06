from django.http import JsonResponse, HttpResponse
from .models import Link
from secrets import token_urlsafe

# Константа длинны короткой ссылки,
LENGHT = 8


def main(request):
    return HttpResponse("Send link to the link/_your_link_")


def link(request, link=None):
    if request.method == "GET":
        if link:
            links = Link.objects.filter(short_link=link)
            # Проверка на наличие объекта в БД
            if links:
                is_active = links.values()[0].get("status")

                # Проверка на активность ссылки
                if is_active:
                    # Вытаскиваем полную ссылку
                    link = links.values()[0].get("link")

                    # Установка флага статуса
                    links.update(status=False)

                    return JsonResponse({"ok": link})

                return JsonResponse({"status": "error", "detail": "link not active"})
            return JsonResponse({"status": "error", "detail": "link not found"})
        return HttpResponse("Отправьте ссылку")

    elif request.method == "POST":
        # Получаем ссылку из запроса
        res = request.GET.get("link")

        # Генерация короткой ссылки
        srt_link = token_urlsafe(LENGHT)

        link = Link(link=res, short_link=srt_link)
        link.save()
        return JsonResponse({"status": "ok", "link": srt_link}, safe=False)
