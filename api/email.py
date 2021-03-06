"""
Atmosphere api email
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django_cyverse_auth.decorators import api_auth_token_required
from django_cyverse_auth.protocol.ldap import lookupEmail

from api import failure_response

from web.emails import feedback_email, quota_request_email, support_email


class Feedback(APIView):
    """
    Post feedback via RESTful API
    """

    @api_auth_token_required
    def post(self, request):
        """
        Creates a new feedback email and sends it to admins
        """
        data = request.data
        required = [
            'message',
        ]
        missing_keys = valid_post_data(data, required)
        if missing_keys:
            return keys_not_found(missing_keys)
        #Pass arguments
        user = request.user
        message = data['message']
        user_email = lookupEmail(user.username)
        result = feedback_email(request, user.username, user_email, message)
        return Response(result, status=status.HTTP_201_CREATED)


class QuotaEmail(APIView):
    """
    Post Quota Email via RESTful API
    """

    @api_auth_token_required
    def post(self, request):
        """
        Creates a new Quota Request email and sends it to admins
        """
        data = request.data
        required = ['quota', 'reason']
        missing_keys = valid_post_data(data, required)
        if missing_keys:
            return keys_not_found(missing_keys)
        #Pass arguments
        username = request.user.username
        quota = data['quota']
        reason = data['reason']
        result = quota_request_email(request, username, quota, reason)
        return Response(result, status=status.HTTP_201_CREATED)


class SupportEmail(APIView):
    """
    Post Support Email via RESTful API
    """

    @api_auth_token_required
    def post(self, request):
        """
        Creates a new support email and sends it to admins
        """
        data = request.data
        required = ['message', 'subject']
        missing_keys = valid_post_data(data, required)
        if missing_keys:
            return keys_not_found(missing_keys)
        subject = data['subject']
        message = data['message']
        result = support_email(request, subject, message)
        return Response(result, status=status.HTTP_201_CREATED)


def valid_post_data(data, required_keys):
    """
    Return any missing required post key names.
    """
    return [key for key in required_keys if key not in data]


def keys_not_found(missing_keys):
    return failure_response(
        status.HTTP_400_BAD_REQUEST,
        'Missing required POST data variables : %s' % missing_keys
    )
