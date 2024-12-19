from rest_framework.permissions import BasePermission

class IsLandlord(BasePermission):


    message = "Только пользователи с ролью 'арендодатель' могут создавать объявления."

    def has_permission(self, request, view):
        # Проверяем, аутентифицирован ли пользователь
        if not request.user or not request.user.is_authenticated:
            return False


        if hasattr(request.user, 'human') and request.user.human.role == 'landlord':
            return True

        return False