from sanic import Blueprint, Request, redirect, json
from sanic_ext import openapi
from .pdfanal.parser import parser
from .auth import check_login

router = Blueprint("router")


# Nothing here
@router.get("/")
@openapi.exclude()
async def goto_home(_):
    # TOOD: redirect to homepage
    return redirect("https://google.com", status=302)


# Login
@router.post("/auth")
@openapi.exclude()
@openapi.response(200, {"application/json": {"status": str, "sessionId": str, "loggedIn": bool}}, "Auth Provider")
async def auth(req: Request):
    user = req.args.get("user")
    password = req.args.get("password")

    # Check login and give user a token, add that token to the db
    logged_in, id = await check_login(user, password)

    if logged_in:
        return json({"status": "Logged In", "sessionId": id, "loggedIn": True})
    
    return json({"status": "Failed login", "sessionId": "-1", "loggedIn": False})


# Parser
@router.post("/parse")
@openapi.parameter("path", str, required=True, allowEmptyValue=False)
# @openapi.body({"application/json": {"path": str}})
@openapi.response(200, {"application/json": {"candidateId": int}}, "Returns id of data stored in database probably")
@openapi.response(400, {"application/json": {"message": str}}, "Returns error message")
@openapi.summary("Parses resume")
@openapi.secured('foo')
@openapi.description("""
> Used for parsing Resume

## Required Parameters
- path: local path where the resume is stored
""")
async def parse(req: Request):
    path = req.args.get("path")

    if not path or len(path) == 0:
        return json({"message": "No path provided"}, status=400)

    id, err = await parser(path)

    if err:
        # Some error occured in parsing
        return json({"message": err}, status=400)

    # Successfully parsed
    return json({"candidateId": id}, status=200)


# Get Candidate info
@router.post("/details")
@openapi.parameter("candidateId", str, required=True, allowEmptyValue=False)
async def get_details(req: Request):
    return json({"id": req.args.get("candidateId")}, status=200)
