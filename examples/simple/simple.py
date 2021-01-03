from ZtjFastApiApp import FastApiApp
from ZtjFastApiServe import FastApiServe
from ZtjFastApiRoute import Router

app = FastApiApp()
app.include_route(Router)
api = app.get_fast_api()

if __name__ == '__main__':
    FastApiServe('simple:api').local()
