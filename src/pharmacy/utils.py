import uuid


# Slug Generators
def get_drug_slug(instance):
    return f"{instance.name}-{instance.brand}-{instance.batch_no}"

def get_dosage_guidelines_slug(instance):
    return f"{instance.period} - {instance.time}"

def get_storage_instructions_slug(instance):
    return f"{instance.place}"