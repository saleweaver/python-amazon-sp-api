import codecs
import zlib
from io import BytesIO, StringIO


def resolve_character_code(response_encoding, fallback="iso-8859-1"):
    character_code = response_encoding or fallback
    if character_code and character_code.lower() == "windows-31j":
        character_code = "cp932"
    return character_code


def decompress_bytes(document, compression_algorithm):
    if compression_algorithm:
        return zlib.decompress(bytearray(document), 15 + 32)
    return document


def decode_document(document, character_code):
    if character_code:
        try:
            return document.decode(character_code)
        except Exception:
            return document
    return document


def handle_file(file, document, encoding):
    if isinstance(file, str):
        with open(file, "w+", encoding=encoding) as text_file:
            text_file.write(document)
    elif isinstance(file, BytesIO):
        file.write(document.encode(encoding))
        file.seek(0)
    elif isinstance(file, StringIO):
        file.write(document)
        file.seek(0)
    else:
        file.write(document)


def _open_stream_target(file, encoding):
    if isinstance(file, str):
        return open(file, "w+", encoding=encoding), True, True
    if isinstance(file, StringIO):
        return file, True, False
    if isinstance(file, BytesIO):
        return file, False, False
    if hasattr(file, "mode") and "b" in file.mode:
        return file, False, False
    return file, True, False


def _stream_bytes_to_target_sync(
    chunk_iter, file, encoding, compression_algorithm, close_after
):
    decompressor = zlib.decompressobj(15 + 32) if compression_algorithm else None
    target, is_text, should_close = file
    decoder = (
        codecs.getincrementaldecoder(encoding)(errors="replace") if is_text else None
    )
    try:
        for chunk in chunk_iter:
            if decompressor:
                chunk = decompressor.decompress(chunk)
            if decoder:
                text = decoder.decode(chunk)
                if text:
                    target.write(text)
            else:
                target.write(chunk)
        if decompressor:
            remainder = decompressor.flush()
            if remainder:
                if decoder:
                    text = decoder.decode(remainder)
                    if text:
                        target.write(text)
                else:
                    target.write(remainder)
        if decoder:
            tail = decoder.decode(b"", final=True)
            if tail:
                target.write(tail)
    finally:
        if close_after and should_close:
            target.close()


async def _stream_bytes_to_target_async(
    chunk_iter, file, encoding, compression_algorithm, close_after
):
    decompressor = zlib.decompressobj(15 + 32) if compression_algorithm else None
    target, is_text, should_close = file
    decoder = (
        codecs.getincrementaldecoder(encoding)(errors="replace") if is_text else None
    )
    try:
        async for chunk in chunk_iter:
            if decompressor:
                chunk = decompressor.decompress(chunk)
            if decoder:
                text = decoder.decode(chunk)
                if text:
                    target.write(text)
            else:
                target.write(chunk)
        if decompressor:
            remainder = decompressor.flush()
            if remainder:
                if decoder:
                    text = decoder.decode(remainder)
                    if text:
                        target.write(text)
                else:
                    target.write(remainder)
        if decoder:
            tail = decoder.decode(b"", final=True)
            if tail:
                target.write(tail)
    finally:
        if close_after and should_close:
            target.close()


def stream_to_file_sync(response, file, encoding, compression_algorithm):
    target = _open_stream_target(file, encoding)
    _stream_bytes_to_target_sync(
        response.iter_content(chunk_size=8192),
        target,
        encoding,
        compression_algorithm,
        True,
    )


async def stream_to_file_async(response, file, encoding, compression_algorithm):
    target = _open_stream_target(file, encoding)

    await _stream_bytes_to_target_async(
        response.aiter_bytes(),
        target,
        encoding,
        compression_algorithm,
        True,
    )
