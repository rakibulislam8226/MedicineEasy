from rest_framework import serializers
from ...models import Organization


class OrganizationSlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            "uid",
            "name",
            "slug",
            "kind",
            "tax_number",
            "registration_no",
            "contact_number",
            "website_url",
            "blog_url",
            "linkedin_url",
            "instagram_url",
            "facebook_url",
            "twitter_url",
            "whatsapp_number",
            "imo_number",
            "summary",
            "description",
            "status",
        ]
