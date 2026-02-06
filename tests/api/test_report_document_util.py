from sp_api.util.report_document import resolve_character_code


def test_resolve_character_code_uses_charset_encoding_when_available():
    assert (
        resolve_character_code(
            response_encoding="utf-8",
            response_charset_encoding="iso-8859-1",
            fallback="iso-8859-1",
        )
        == "iso-8859-1"
    )


def test_resolve_character_code_falls_back_from_default_utf8_without_charset():
    assert (
        resolve_character_code(
            response_encoding="utf-8",
            response_charset_encoding=None,
            fallback="iso-8859-1",
        )
        == "iso-8859-1"
    )


def test_resolve_character_code_falls_back_when_encoding_is_missing():
    assert (
        resolve_character_code(
            response_encoding=None,
            response_charset_encoding=None,
            fallback="iso-8859-1",
        )
        == "iso-8859-1"
    )


def test_resolve_character_code_keeps_non_utf8_encoding():
    assert (
        resolve_character_code(
            response_encoding="windows-31j",
            response_charset_encoding=None,
            fallback="iso-8859-1",
        )
        == "cp932"
    )


def test_resolve_character_code_keeps_explicit_utf8_charset():
    assert (
        resolve_character_code(
            response_encoding="utf-8",
            response_charset_encoding="utf-8",
            fallback="iso-8859-1",
        )
        == "utf-8"
    )
