from rrf import serializers
from ..models import Todo

class TodoSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Todo
        fields = ['text']

    def save(self):
        user = self.context['user']
        self.validated_data['user'] = user
        model = Todo.objects.create(**self.validated_data)
        model.save()
        return model
    
    def update (self, instance) : 
        for field_name, field_val in self.validated_data.items() :
            setattr(instance, field_name, field_val)
            instance.save()
        return instance

    
class GetListTodoSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Todo
        fields = ['id','text','is_done']