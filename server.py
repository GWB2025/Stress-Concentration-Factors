"""
Lightweight HTTP server to host the Kt calculator locally.

Usage:
  python server.py                # serves index.html on http://127.0.0.1:8000
  python server.py --port 9000    # custom port
"""

from __future__ import annotations

import argparse
import contextlib
import http.server
import os
import socket
import socketserver
from pathlib import Path


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    # Silence noisy logging; keep errors.
    def log_message(self, format: str, *args) -> None:  # noqa: A003
        return


def find_free_port(start: int) -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("127.0.0.1", start))
        return s.getsockname()[1]


def serve(port: int) -> None:
    webroot = Path(__file__).resolve().parent
    os.chdir(webroot)  # ensure index.html resolves without extra flags

    with socketserver.TCPServer(("127.0.0.1", port), QuietHandler) as httpd:
        host, assigned_port = httpd.server_address
        print(f"Serving {webroot} at http://{host}:{assigned_port} (Ctrl+C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local server for Kt calculator.")
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000). If unavailable, picks a free port.",
    )
    args = parser.parse_args()

    port = args.port
    try:
        serve(port)
    except OSError as err:
        if "Address already in use" in str(err):
            fallback = find_free_port(0)
            print(f"Port {port} in use; retrying on {fallback}")
            serve(fallback)
        else:
            raise


if __name__ == "__main__":
    main()
