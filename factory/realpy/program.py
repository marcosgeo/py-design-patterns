# program.py
from factory.realpy import music


config = {
    "spotify_client_key": "THE_SPOTIFY_CLIENT_KEY",
    "spotify_client_secret": "THE SPOTIFY_CLIENT_SECRET",
    "pandora_client_key": "THE_PANDORA_CLIENT_KEY",
    "pandora_client_secret": "THE_PANDORA_CLIENT_SECRET",
    "local_music_location": "/usr/data/music"
}

def run():
    pandora = music.services.get("PANDORA", **config)
    pandora.test_connection()

    spotify = music.services.get("SPOTIFY", **config)
    spotify.test_connection()

    local = music.services.get("LOCAL", **config)
    local.test_connection()

    pandora2 = music.services.get("PANDORA", **config)
    print(f"id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}")

    spotify2 = music.services.get("SPOTIFY", **config)
    print(f"if(spotify) == id(spotify2): {id(spotify) == id(spotify)}")


if __name__ == "__main__":
    run()
