from rest_framework import viewsets, permissions
from apps.clients.serializers import ClientSerializer
from project.permissions import IsSupport, IsSale, AlwaysFalse
from user_management.models import User_Model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

# Provides a default ViewSet with integration permission handler

class PermBasedViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, *args, **kwargs):

        self.viewing_actions = ["list", "retrieve"]
        self.modifying_actions = ["update", "partial_update","destroy"]
        self.can_view_if_or = self.can_view_if_or
        self.can_update_or_delete = self.can_update_or_delete
        self.can_create = self.can_create
        
        self.can_view_if_or.append(IsAdminUser)
        self.can_update_or_delete.append(IsAdminUser)
        self.can_create.append(IsAdminUser)
    
    def get_permissions(self):

        """
            This allows us to counter the ViewSets native permissions "addition" system, where EVERY listed perm is required to gain access. 
            We basically replace the '&' by a 'or' so only one perm from our defined list is required to allow action.
            Since this doesn't interfere with the default system in any way,. we can combine both to have 2 distinct levels of access.
            If None of our conditions are met, it will return our default permission (IsAuthenticated)
        """
        
        if self.action == "create":
            for perm in self.can_create:
                if perm.has_permission(self.request, self.request, self):
                    print("La permission suivante est vraie :")
                    print(perm, self.request.user.has_perm(self.request.user, perm))
                    return [perm()]
            return [AlwaysFalse()]

        if self.action in self.viewing_actions: 
            for perm in self.can_view_if_or:
                if perm.has_permission(self.request, self.request, self):
                    print("La permission suivante est vraie :")
                    print(perm, self.request.user.has_perm(self.request.user, perm))
                    return [perm()]
            return [AlwaysFalse()]  

        elif self.action in self.modifying_actions:
            for perm in self.can_update_or_delete:
                if perm.has_permission(self.request, self.request, self):
                    print("La permission suivante est vraie :")
                    print(perm, self.request.user.has_perm(self.request.user, perm))
                    return [perm()]
            return [AlwaysFalse()]  

        return [permissions.IsAuthenticated()]