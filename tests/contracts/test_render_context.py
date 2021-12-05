import unittest
from pathlib import Path

from dagserializer.contracts.render_context import RenderContext


class DummyRenderContext(RenderContext):
    def get_template(
        self,
        template_file_path: Path,
    ) -> None:
        pass


class RenderContextTest(unittest.TestCase):
    def test_get_template(self):
        """
        Test if fake implementatiuon of RenderContext class can
        call and has get_template method
        """
        self.assertEqual(DummyRenderContext().get_template(Path("./")), None)


if __name__ == "__main__":
    unittest.main()
