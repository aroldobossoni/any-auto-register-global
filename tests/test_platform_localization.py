import json

import pytest

from core.localization import (
    MissingLocalizationKeyError,
    PlatformLocalizationFacade,
    ProfileLoader,
    ProfileParityError,
    get_localization_facade,
)


def write_profile(tmp_path, platform, language, profile):
    path = tmp_path / platform / f"{language}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(profile), encoding="utf-8")


def test_loads_platform_language_profile(tmp_path):
    write_profile(
        tmp_path,
        "demo",
        "en",
        {"strings": {"title": "Title"}, "selectors": {"submit": "#submit"}},
    )
    write_profile(
        tmp_path,
        "demo",
        "pt-BR",
        {"strings": {"title": "Título"}, "selectors": {"submit": "#enviar"}},
    )

    facade = PlatformLocalizationFacade("demo", "pt-BR", ProfileLoader(tmp_path))

    assert facade.get_string("title") == "Título"
    assert facade.get_selector("submit") == "#enviar"


def test_falls_back_to_english_profile_and_reuses_singleton(tmp_path):
    write_profile(
        tmp_path,
        "demo",
        "en",
        {"strings": {"title": "Title"}, "selectors": {"submit": "#submit"}},
    )

    first = get_localization_facade("demo", "es", tmp_path)
    second = get_localization_facade("demo", "es", tmp_path)

    assert first is second
    assert first.get_string("title") == "Title"


def test_reports_profile_key_parity(tmp_path):
    write_profile(
        tmp_path,
        "demo",
        "en",
        {"strings": {"title": "Title", "body": "Body"}, "selectors": {}},
    )
    write_profile(
        tmp_path,
        "demo",
        "pt-BR",
        {"strings": {"title": "Título"}, "selectors": {}},
    )

    with pytest.raises(ProfileParityError, match="strings.body"):
        ProfileLoader(tmp_path).validate_key_parity("demo", "pt-BR")


def test_raises_clear_error_for_missing_key(tmp_path):
    write_profile(
        tmp_path,
        "demo",
        "en",
        {"strings": {}, "selectors": {}},
    )
    facade = PlatformLocalizationFacade("demo", "en", ProfileLoader(tmp_path))

    with pytest.raises(
        MissingLocalizationKeyError,
        match=r"demo/en/strings\.missing",
    ):
        facade.get_string("missing")
