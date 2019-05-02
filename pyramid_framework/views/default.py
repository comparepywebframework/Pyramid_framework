from pyramid.view import view_config
from pyramid.response import Response
from pyramid.renderers import render_to_response
import uuid
from datetime import time, date
import transaction
import requests

from .. import models


@view_config(route_name="index", renderer="templates/index.jinja2")
def index(request):
    data = request.json_body
    return {"times": data["times"], "text": data["text"]}


@view_config(route_name="add_shop")
def add_shop(request):
    data = request.json_body
    for i in range(int(data["times"])):
        shop = models.Shop(
            name=str(uuid.uuid4()),
            city=str(uuid.uuid4()),
            street=str(uuid.uuid4()),
            street_number=7,
            open_at=time(hour=7, minute=0),
            close_at=time(hour=21, minute=0),
        )
        request.dbsession.add(shop)
    return Response(status=201)


@view_config(route_name="clear_shops_table")
def clear_shop_table(request):
    request.dbsession.query(models.Shop).delete()
    return Response(status=200)


@view_config(route_name="external_api_call")
def external_api_call(request):
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?id=3096472&APPID=39d3a15f5bdcab980c739b931b9c2863"
    )
    return Response(r.text)


@view_config(route_name="serialize_json", renderer='json')
def serialize_json(request):
    id_number = str(uuid.uuid4())
    student = models.Student(name="Jim", surname="Bim", date_of_birth=date(1990, 1, 1), id_number=id_number)
    request.dbsession.add(student)
    student = request.dbsession.query(models.Student).filter_by(id_number=id_number).first()
    return {"name": student.name, "surname": student.surname, "date_of_birth": str(student.date_of_birth), "id_number": student.id_number}


@view_config(route_name="clear_student_table")
def clear_student_table(request):
    request.dbsession.query(models.Student).delete()
    return Response(status=200)