from rest_framework.serializers import ModelSerializer
from blog.models import BlogPost


class BlogPostSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'





