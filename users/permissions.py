from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        :param request:
        :param view:
        :return:
        """
        if view.action == "POST":       # Cualquiera puede crear un usuario aunque no esté autenticado
            return True
        elif request.user.is_superuser: # El usuario superadministrador puede hacer cualquier acción
            return True
        elif view.action in ['retrieve', 'update', 'destroy']: # Hay que delegar en el método has_object_permission
                                                               # (excepto que sea una petición GET de un listado)
            return True # La decisión se toma en en método has_objetc_permission
        else: # GET a /api/1.0/users
            return False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user
        tiene permiso para realizar la acción (GET, POST, PUT o DELETE)
        sobre el objeto obj
        Este método se ejecuta sobre vistas de detalle
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj # Si el usuario es superadministrador puede realizar
                                                                # cualquier acción o es el mismo usuario que el
                                                                # propietario del objeto
