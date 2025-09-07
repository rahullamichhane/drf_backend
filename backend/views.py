from django.http import HttpResponse
from django.conf import settings
import os

def home_view(request):
    """
    Serve the url.html file from the project root as the homepage
    """
    # Path to url.html in the project root
    url_html_path = os.path.join(settings.BASE_DIR.parent, 'url.html')
    
    try:
        with open(url_html_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return HttpResponse(content, content_type='text/html')
    except FileNotFoundError:
        return HttpResponse("<h1>Error: url.html not found</h1>", status=404)
