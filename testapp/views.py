from django.http import HttpRequest
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    """Returns `Hello World, This is my new HOME !` to cute user."

    Args:
        request (HttpRequest): The cute user request

    Returns:
        HttpResponse: Response :)
    """
    return HttpResponse("Hello World, This is my new HOME !")


def hello_world(request: HttpRequest) -> HttpResponse:
    """Return `Hello, World!` to cute user :)

    Args:
        request (HttpRequest): The request

    Returns:
        HttpResponse: Response contain `Hello, World!`
    """
    return HttpResponse("<h1>Hello, World!</h1>")
