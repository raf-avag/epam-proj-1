from flask.views import MethodView
from src.infrastructure.controller import APIController
from flask import Response


class APIView(MethodView):
    def __init__(self, request) -> None:
        self.request = request

    def post(self):
        controller = APIController()
        controller.process_event(self.request)
        return Response(status=200)
