from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class RenderContext(ABC):
    """
    Render contract that defines how templates can
    be rendered
    """

    @abstractmethod
    def get_template(self, template_file_path: Path) -> Any:
        pass
