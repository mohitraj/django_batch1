from rest_framework import serializers

class AttSerializer(serializers.Serializer):
	title = serializers.CharField(max_length=100)
	content = serializers.TextField()
	date1 = serializers.DateTimeField(default=timezone.now)
	author = serializers.ForeignKey(User, on_delete=models.CASCADE)
