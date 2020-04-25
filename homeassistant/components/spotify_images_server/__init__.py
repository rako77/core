"""The spotify Images Server component."""
from aiohttp import web
from aiohttp.hdrs import CACHE_CONTROL, CONTENT_TYPE, LOCATION
from spotipy import Spotify, SpotifyException

from homeassistant.components.http import HomeAssistantView


def setup(hass, config):
    """Set up the Spotify Images Server component."""
    hass.http.register_view(ImageRedirectView(hass))
    hass.http.register_view(ImageURLView(hass))
    return True


class ImageRedirectView(HomeAssistantView):
    """View to handle spotify image requests."""

    requires_auth = False
    url = "/api/spotify_images_server"
    name = "api:spotify_images_server:image"

    def __init__(self, hass):
        """Init."""
        self.hass = hass

    async def get(self, request):
        """Start a get request."""

        spotify_playlist_uri = request.query.get("spotify_playlist_uri")
        if spotify_playlist_uri is None or spotify_playlist_uri == "":
            return web.Response(status=400, body="Invalid request")
        if "spotify" not in self.hass.data:
            return web.Response(status=400, body="Spotify integration not set up")
        spotify_keys = self.hass.data["spotify"].keys()
        iterator = iter(spotify_keys)
        entry_id = next(iterator)
        session = self.hass.data["spotify"][entry_id]["spotify_session"]
        spotify = Spotify(auth=session.token["access_token"])

        try:
            image_info = spotify.playlist_cover_image(spotify_playlist_uri)
            headers = {CACHE_CONTROL: "max-age=3600", LOCATION: image_info[0]["url"]}
            return web.Response(status=303, headers=headers)
        except SpotifyException as spotify_exception:
            return web.Response(status=400, body=str(spotify_exception))


class ImageURLView(HomeAssistantView):
    """View to handle spotify image requests."""

    requires_auth = False
    url = "/api/spotify_playlist_image_data"
    name = "api:spotify_playlist_image:data"

    def __init__(self, hass):
        """Init."""
        self.hass = hass

    async def get(self, request):
        """Start a get request."""

        spotify_playlist_uri = request.query.get("spotify_playlist_uri")
        if spotify_playlist_uri is None or spotify_playlist_uri == "":
            return web.Response(status=400, body="Invalid request")
        if "spotify" not in self.hass.data:
            return web.Response(status=400, body="Spotify integration not set up")
        spotify_keys = self.hass.data["spotify"].keys()
        iterator = iter(spotify_keys)
        entry_id = next(iterator)
        session = self.hass.data["spotify"][entry_id]["spotify_session"]
        spotify = Spotify(auth=session.token["access_token"])

        try:
            image_info = spotify.playlist_cover_image(spotify_playlist_uri)
            headers = {
                CACHE_CONTROL: "max-age=3600",
                CONTENT_TYPE: "application/json; charset=UTF-8",
            }
            return web.Response(headers=headers, body=image_info)
        except SpotifyException as spotify_exception:
            return web.Response(status=400, body=str(spotify_exception))
