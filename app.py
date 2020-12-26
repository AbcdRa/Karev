from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.routing import Route
from render import createOrUpdateHtml



async def homepage(request):
    HTML_PATH = createOrUpdateHtml()
    with open(HTML_PATH, "r", encoding="utf-8") as new_file:
        return HTMLResponse(new_file.read())

routes = [
    Route('/', homepage),
    Mount('/static', app=StaticFiles(directory='static'), name="static"),
]


app = Starlette(debug=True, routes=routes)

