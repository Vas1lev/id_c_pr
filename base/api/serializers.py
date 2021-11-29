from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from base.models import Info, Description


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    department = StringRelatedField(read_only=True)
    description = serializers.SerializerMethodField('get_description')

    class Meta:
        model = Info
        fields = [
            'first_name', 'last_name', 'citizenship', 'gen', 'personal_no', 'date_of_birth',
            'date_of_expiry', 'signature', 'card_no', 'place_of_birth', 'date_of_issue',
            'issuing_authority', 'department', 'description', 'image'
        ]

    def get_description(self, obj):
        description = ",".join([each.name for each in obj.description.all()])
        return description
