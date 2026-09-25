"""Carregamento de perfis JSON de localização."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class LocalizationError(Exception):
    """Erro-base de localização."""


class ProfileNotFoundError(LocalizationError):
    """Perfil e fallback em inglês não encontrados."""


class InvalidProfileError(LocalizationError):
    """Perfil JSON inválido."""


class ProfileParityError(LocalizationError):
    """Perfil não possui as mesmas chaves do perfil em inglês."""


class ProfileLoader:
    """Carrega perfis em ``<base>/<platform>/<language>.json``."""

    def __init__(self, base_dir: str | Path | None = None) -> None:
        self.base_dir = Path(base_dir or Path(__file__).with_name("profiles"))

    def load_profile(self, platform: str, language: str) -> dict[str, Any]:
        fallback = self._load_file(platform, "en", required=True)
        if language == "en":
            return fallback

        localized = self._load_file(platform, language, required=False)
        if localized is None:
            return fallback
        return self._merge(fallback, localized)

    def validate_key_parity(self, platform: str, language: str) -> None:
        reference = self._load_file(platform, "en", required=True)
        localized = self._load_file(platform, language, required=True)
        expected = self._leaf_keys(reference)
        actual = self._leaf_keys(localized)
        if expected != actual:
            missing = sorted(expected - actual)
            extra = sorted(actual - expected)
            raise ProfileParityError(
                f"Profile key mismatch for {platform}/{language}: "
                f"missing={missing}, extra={extra}"
            )

    def _load_file(
        self, platform: str, language: str, *, required: bool
    ) -> dict[str, Any] | None:
        path = self.base_dir / platform / f"{language}.json"
        if not path.is_file():
            if required:
                raise ProfileNotFoundError(f"Localization profile not found: {path}")
            return None

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise InvalidProfileError(f"Invalid localization profile: {path}") from exc
        if not isinstance(data, dict):
            raise InvalidProfileError(f"Localization profile must be an object: {path}")
        return data

    @classmethod
    def _merge(cls, fallback: dict[str, Any], localized: dict[str, Any]) -> dict[str, Any]:
        merged = dict(fallback)
        for key, value in localized.items():
            if isinstance(value, dict) and isinstance(merged.get(key), dict):
                merged[key] = cls._merge(merged[key], value)
            else:
                merged[key] = value
        return merged

    @classmethod
    def _leaf_keys(cls, value: dict[str, Any], prefix: str = "") -> set[str]:
        keys: set[str] = set()
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else key
            if isinstance(child, dict):
                keys.update(cls._leaf_keys(child, path))
            else:
                keys.add(path)
        return keys
