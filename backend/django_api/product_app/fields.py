from django.db import models
from django.core import checks


class OrderField(models.PositiveSmallIntegerField):
    description = "Order field on a unique field"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_for_field_attribute(**kwargs),
        ]

    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must have a unique_for_field attribute set.")
            ]

        elif self.unique_for_field not in [
            f.name for f in self.model._meta.get_fields()
        ]:
            return [checks.Error("OrderField entered does not match an existing field")]
        return []

    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:
            qs = self.model.objects.all()
            try:
                query = {
                    self.unique_for_field: getattr(
                        model_instance, self.unique_for_field
                    )
                }

                qs = qs.filter(**query)
                last_value = qs.latest(self.attname)

                if last_value:
                    value = last_value.order + 1
                else:
                    value = 1
            except models.ObjectDoesNotExist:
                value = 1
            return value

        return super().pre_save(model_instance, add)
