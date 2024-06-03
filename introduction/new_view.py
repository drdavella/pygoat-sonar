from django.shortcuts import redirect
from django.http import HttpResponse

import sqlite3
import json


def do_useful_things(request):
    if request.method == "POST":
        user = request.POST.get("user")

        sql = """SELECT user FROM users WHERE user = ?"""
        conn = sqlite3.connect("example")
        result = conn.cursor().execute(sql, (user, ))

        json_response = json.dumps({"user": result.fetchone()[0]})
        return HttpResponse(json_response.encode("utf-8"))
    else:
        return redirect("/")
