from ZtjFastApiApp import FastApiApp
from ZtjFastApiServe import FastApiServe
from ZtjFastApiRoute import Router
import routes


app = FastApiApp()
app.include_route(Router)
app.load_routes(routes.__path__[0])
api = app.get_fast_api()

if __name__ == '__main__':
    FastApiServe('automatic:api').local()
