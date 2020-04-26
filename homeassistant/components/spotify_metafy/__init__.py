"""The Spotify Metafy integration."""
# import asyncio

# import voluptuous as vol

# from homeassistant.components.media_player import DOMAIN as MEDIA_PLAYER_DOMAIN
# from homeassistant.components.spotify.media_player import SpotifyMediaPlayer
# from homeassistant.config_entries import ConfigEntry
# from homeassistant.core import HomeAssistant
# from homeassistant.exceptions import ConfigEntryNotReady
# from homeassistant.helpers.entity_registry import EntityRegistry

# from .const import DOMAIN

# CONFIG_SCHEMA = vol.Schema({DOMAIN: vol.Schema({})}, extra=vol.ALLOW_EXTRA)


# async def async_setup(hass: HomeAssistant, config: dict):
#     """Set up the Spotify Metafy component."""
#     if DOMAIN not in config:
#         return True

#     if "spotify" not in hass.data:
#         raise PlatformNotReady
#     for user in config[DOMAIN]:
#         user_prefix = user["user_prefix"] if "user_prefix" in user else ""
#         spotify_id = user["spotify_id"]
#         destination = user["destination"]
#         playlists = user["playlists"]
#         for playlist in playlists:
#             uri = playlist["uri"]
#             hass.async_create_task(
#                 hass.config_entries.async_forward_entry_setup(
#                     entry, MEDIA_PLAYER_DOMAIN
#                 )
#             )

#     return True


# async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
#     """Set up Spotify Metafy from a config entry."""
#     # TODO Store an API object for your platforms to access
#     # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

#     if "spotify" not in hass.data:
#         raise ConfigEntryNotReady

#     spotify_entity_id = "xyz"
#     entity_registry: EntityRegistry = hass.helpers.entity_registry
#     spotify_media_player: SpotifyMediaPlayer = await entity_registry.async_get(
#         spotify_entity_id
#     )
#     # hass.config_entries.async_get_entry(spotify_entity_id).add_update_listener

#     hass.async_create_task(
#         hass.config_entries.async_forward_entry_setup(entry, MEDIA_PLAYER_DOMAIN)
#     )

#     return True


# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
#     """Unload a config entry."""
#     unload_ok = all(
#         await asyncio.gather(
#             *[
#                 hass.config_entries.async_forward_entry_unload(entry, component)
#                 for component in [MEDIA_PLAYER_DOMAIN]
#             ]
#         )
#     )
#     if unload_ok:
#         hass.data[DOMAIN].pop(entry.entry_id)

#     return unload_ok
