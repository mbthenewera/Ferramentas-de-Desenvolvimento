from pathlib import Path
import argparse
import hashlib
import json


def hash_file(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            digest.update(chunk)
    return digest.hexdigest()


def build_tree(folder: Path) -> list[str]:
    result = []
    for path in sorted(folder.rglob('*')):
        level = len(path.relative_to(folder).parts) - 1
        indent = '  ' * level
        result.append(f"{indent}- {path.name}")
    return result


def scan_extensions(folder: Path) -> dict[str, int]:
    stats: dict[str, int] = {}
    for path in folder.rglob('*'):
        if path.is_file():
            ext = path.suffix.lower() or '[sem extensão]'
            stats[ext] = stats.get(ext, 0) + 1
    return dict(sorted(stats.items(), key=lambda item: item[0]))


def main() -> None:
    parser = argparse.ArgumentParser(description='Ferramentas úteis para desenvolvimento.')
    sub = parser.add_subparsers(dest='command', required=True)

    hash_cmd = sub.add_parser('hash')
    hash_cmd.add_argument('file')

    tree_cmd = sub.add_parser('tree')
    tree_cmd.add_argument('folder')

    stats_cmd = sub.add_parser('stats')
    stats_cmd.add_argument('folder')

    args = parser.parse_args()

    if args.command == 'hash':
        file_path = Path(args.file)
        print(hash_file(file_path))
    elif args.command == 'tree':
        folder = Path(args.folder)
        print('\n'.join(build_tree(folder)))
    elif args.command == 'stats':
        folder = Path(args.folder)
        print(json.dumps(scan_extensions(folder), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
