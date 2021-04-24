from .models import MyUser, Ad, Image


class UsersViewSet(ModelViewSet):
    queryset = MyUser.objects.order_by('id').all()

    serializer_class = MyUserListSerializer

    def get_object(self):
        return MyUser.objects.get(pk=self.kwargs['user_id'])

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, MyUserDetailSerializer)


      
class AdViewSet(ModelViewSet):
    queryset = Ad.objects.order_by('id').all()
    
    serializer_class = AdListSerializer

    def get_object(self):
        return Ad.objects.get(pk=self.kwargs['ad_id'])

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Ad.objects.filter(ad__pk=user_id)
