from sanic import Sanic
# from textwrap import dedent

from src.routes import router

app = Sanic(__name__)
app.blueprint(router)
# app.ctx.db = Database()

# app.ext.openapi.describe(
#     "CVerify API",
#     version="1.2.3",
#     description=dedent(
#         """
#         # Info
#         This is the API used by our server to parse and provide information
#
#         # Note
#         This API is not free to try, so don't use it :)
#         """
#     ),
# )

if __name__ == "__main__":
    app.run(dev=True)
