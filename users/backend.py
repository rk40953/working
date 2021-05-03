from .models import EmpTable

class MyCustomBackend(object):


    def authenticate(self, empEmail, password):

        try:
            # Try to find a user matching your username
            user = EmpTable.objects.filter(empEmail=empEmail).first()


            if user.check_password(password):

                return user
            else:

                return None
        except EmpTable.DoesNotExist:

            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return EmpTable.objects.get(pk=user_id)
        except EmpTable.DoesNotExist:
            return None