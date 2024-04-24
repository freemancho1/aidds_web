import argparse

def web_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Server-side Program of an Artificial Intelligence-based ' \
                    'Distribution Design System'
    )
    parser.add_argument('--port', '-p', type=int, default=11002, help='')

    args = parser.parse_args()
    return args