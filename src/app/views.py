from flask.views import MethodView
from infrastructure.controller import APIController


class APIView(MethodView):
    def post(self, request):
        controller = APIController()
        controller.process_event(request)
