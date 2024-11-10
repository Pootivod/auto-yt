from mitmproxy import http
from bs4 import BeautifulSoup

def response(flow: http.HTTPFlow) -> None:
    """
    Функция, которая будет вызвана для каждого ответа.
    Мы обрабатываем `flow.response` для извлечения нужной информации.
    """
    
    # Проверим, что это HTML-страница
    if "text/html" in flow.response.headers.get("Content-Type", ""):
        # Декодируем контент ответа
        html_content = flow.response.content.decode("utf-8", errors="ignore")
        
        # Парсим HTML с помощью BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Извлекаем title страницы
        title = soup.title.string if soup.title else "No title found"
        
        # Выводим title в консоль
        print(f"Title of {flow.request.url}: {title}")