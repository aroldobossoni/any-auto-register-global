"""Façade pública para localização específica de plataforma."""

from __future__ import annotations

from pathlib import Path
from threading import Lock
from typing import Any

from .loader import LocalizationError, ProfileLoader


class MissingLocalizationKeyError(LocalizationError, KeyError):
    """Chave de localização ausente."""


class PlatformLocalizationFacade:
    def __init__(
        self,
        platform: str,
        language: str = "en",
        loader: ProfileLoader | None = None,
    ) -> None:
        self.platform = platform
        self.language = language
        self.loader = loader or ProfileLoader()
        self._profile = self.loader.load_profile(platform, language)

    def get_string(self, key: str) -> str:
        return self._get("strings", key)

    def get_selector(self, key: str) -> str:
        return self._get("selectors", key)

    def _get(self, section: str, key: str) -> str:
        values: Any = self._profile.get(section)
        if not isinstance(values, dict) or key not in values:
            raise MissingLocalizationKeyError(
                f"Missing localization key: {self.platform}/{self.language}/{section}.{key}"
            )
        value = values[key]
        if not isinstance(value, str):
            raise MissingLocalizationKeyError(
                f"Localization value is not a string: "
                f"{self.platform}/{self.language}/{section}.{key}"
            )
        return value


_instances: dict[tuple[str, str, Path], PlatformLocalizationFacade] = {}
_instances_lock = Lock()


def get_localization_facade(
    platform: str,
    language: str = "en",
    base_dir: str | Path | None = None,
) -> PlatformLocalizationFacade:
    """Retorna uma instância compartilhada por plataforma, idioma e diretório."""
    loader = ProfileLoader(base_dir)
    key = (platform, language, loader.base_dir.resolve())
    with _instances_lock:
        if key not in _instances:
            _instances[key] = PlatformLocalizationFacade(platform, language, loader)
        return _instances[key]
