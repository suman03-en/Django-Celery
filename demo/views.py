from rest_framework.views import APIView
from .tasks import send_welcome_email
from rest_framework.response import Response

class RegisterUserView(APIView):
    def post(self, request):
        user_email = request.data.get("email")
        message = request.data.get("message")
        subject = request.data.get("subject")
        send_welcome_email.delay(user_email, message, subject)
        return Response({"message": "User registered successfully. A welcome email will be sent shortly."})