from dataclasses import dataclass
from typing import Optional


@dataclass
class Stream:

    provider: str

    title: str

    description: str

    url: str

    quality: Optional[str] = None

    language: Optional[str] = None

    size: Optional[float] = None

    hdr: bool = False

    dolby_vision: bool = False

    cached: bool = False