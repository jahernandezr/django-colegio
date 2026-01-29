from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .db import ejecutar_sql
import re


# Create your views here.
@login_required
def dashboard(request):
    return render(request,'dashboard/index.html')

def validar_sql(sql):
    sql = sql.lower()
    prohibidos = [
        r"\bdelete\b", r"\bupdate\b", r"\binsert\b",
        r"\bdrop\b", r"\balter\b", r"\btruncate\b",
        r"\bcreate\b", r"\bgrant\b", r"\brevoke\b"
    ]
    return not any(re.search(p, sql) for p in prohibidos)

def ejecutar_query(request):
    columnas = []
    resultados = []
    query = ""

    if request.method == "POST":
        query = request.POST.get("query")

        if not validar_sql(query):
            return render(request, "dashboard/index.html", {
                "error": "Solo se permiten consultas SELECT",
                "sql": query
            })

        try:
            columnas, resultados = ejecutar_sql(query)
        except Exception as e:
            return render(request, "dashboard/index.html", {
                "error": str(e),
                "query": query
            })

    return render(request, "dashboard/index.html", {
        "columnas": columnas,
        "resultados": resultados,
        "query": query
    })
