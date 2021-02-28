# yaml_serializer.py

import yaml
from factory.realpy.serializers import JsonSerializer, factory

class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)

factory.register_format("YAML", YamlSerializer)
