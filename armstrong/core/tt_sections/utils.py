from importlib import import_module

from django.conf import settings

def get_module_and_model_names():
    s = (getattr(settings, "ARMSTRONG_SECTION_ITEM_MODEL", False) or
            "armstrong.apps.content.models.Content")
    return s.rsplit(".", 1)


def get_item_model_class():
    module_name, class_name = get_module_and_model_names()
    module = import_module(module_name)
    return getattr(module, class_name)

def filter_item_rels(rels):
    model_rels = []
    ItemModel = get_item_model_class()
    for related in rels:
        if issubclass(ItemModel, related.related_model):
            model_rels.append(related)
    return model_rels

def get_section_relations(Section):
    """Find every relationship between section and the item model."""
    all_rels = [f for f in Section._meta.get_fields(include_hidden=True) if
                f.is_relation and f.auto_created]
    return filter_item_rels(all_rels)

def get_section_many_to_many_relations(Section):
    m2m_rels = [f for f in Section._meta.get_fields(include_hidden=True) if
                f.many_to_many and f.auto_created]
    return filter_item_rels(m2m_rels)
