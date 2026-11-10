"""Serve the built site locally with the same clean paths as production."""
from argparse import ArgumentParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

DIST = Path(__file__).resolve().parents[1] / 'dist'


class SiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def translate_path(self, path):
        file = Path(super().translate_path(path))
        page = file.with_suffix('.html') if not file.suffix else file
        if file.parent == DIST and page.is_file():
            return str(page)
        return str(file)


if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--port', default=8000, type=int)
    port = parser.parse_args().port
    with ThreadingHTTPServer(('127.0.0.1', port), SiteHandler) as server:
        print(f'Preview at http://127.0.0.1:{port}', flush=True)
        server.serve_forever()
