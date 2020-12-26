from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route
from render import createOrUpdateHtml



async def homepage(request):
    HTML_PATH = createOrUpdateHtml()
    with open(HTML_PATH, "r", encoding="utf-8") as new_file:
        return HTMLResponse(new_file.read())


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])