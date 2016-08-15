import django_filters
from .models import Todo


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Todo
        fields = [ 'state']
    
    publish_state_true = django_filters.BooleanField(state='True')