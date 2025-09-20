import httpx

from django.http import JsonResponse

from config import settings
from common.http_client import http_get


def index(request) -> JsonResponse:
    try:
        resp = http_get(
            url=settings.env('CHATBOT_API_URL'),
        )
        data = resp.json()

    except httpx.RequestError as e:
        data = {"error": str(e)}
    except httpx.HTTPStatusError as e:
        data = {"error": f"HTTP 상태 코드 오류: {e.response.status_code}"}

    return JsonResponse(data)