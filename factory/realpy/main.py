from factory.realpy.songs import Song
from factory.realpy import serializers
from factory.realpy import yaml_serializer


def main():
    song = Song("1", "Redemption Song", "Bob Marley")
    serializer = serializers.ObjectSerializer()

    print(serializer.serialize(song, "JSON"))

    print(serializer.serialize(song, "XML"))

    # after implementation of YamlSerializer
    print(serializer.serialize(song, "YAML"))

    print()


if __name__ == "__main__":
    main()