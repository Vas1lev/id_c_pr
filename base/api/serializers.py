from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from base.models import Info


class InfoSerializer(serializers.ModelSerializer):
    department = StringRelatedField(read_only=True)
    description = StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Info
        fields = [
            'first_name', 'last_name', 'citizenship', 'gen', 'personal_no', 'date_of_birth',
            'date_of_expiry', 'signature', 'card_no', 'place_of_birth', 'date_of_issue',
            'issuing_authority', 'department', 'description', 'image'
        ]