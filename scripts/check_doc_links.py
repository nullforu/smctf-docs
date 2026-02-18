from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = ROOT / "src" / "content" / "docs"

LINK_RE = re.compile(r"\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
IMAGE_EXT_RE = re.compile(r"\.(png|jpg|jpeg|gif|svg|webp|drawio\.png)$", re.I)


def collect_routes(files: list[Path]) -> tuple[dict[str, Path], set[str]]:
    route_map: dict[str, Path] = {}
    index_routes: set[str] = set()

    for f in files:
        rel = f.relative_to(DOCS_ROOT)
        route = "/" + "/".join(rel.with_suffix("").parts)
        route_map[route] = f
        if rel.name in ("index.md", "index.mdx"):
            index_routes.add("/" + "/".join(rel.parent.parts))

    return route_map, index_routes


def iter_doc_files() -> list[Path]:
    return list(DOCS_ROOT.rglob("*.md")) + list(DOCS_ROOT.rglob("*.mdx"))


def is_ignored_link(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:")) or href.startswith("#")


def resolve_route(file_path: Path, href: str) -> str:
    path = href.split("#", 1)[0]
    if not path:
        return ""

    if path.startswith("/"):
        route = path
    else:
        rel_dir = file_path.parent.relative_to(DOCS_ROOT)
        rel_target = (Path("/") / rel_dir / path).resolve().as_posix()
        route = rel_target

    if route.endswith(".md") or route.endswith(".mdx"):
        route = route.rsplit(".", 1)[0]

    return route


def check_links() -> list[tuple[Path, str, str]]:
    files = iter_doc_files()
    route_map, index_routes = collect_routes(files)

    broken: list[tuple[Path, str, str]] = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(text):
            href = m.group(1).strip()
            if is_ignored_link(href):
                continue
            if href.startswith("images/") or IMAGE_EXT_RE.search(href):
                continue

            route = resolve_route(f, href)
            if not route:
                continue

            if route in index_routes:
                continue

            if route not in route_map:
                broken.append((f, href, route))

    return broken


def check_images() -> list[tuple[Path, str, Path]]:
    files = iter_doc_files()
    missing: list[tuple[Path, str, Path]] = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in IMAGE_RE.finditer(text):
            href = m.group(1).strip().split("#", 1)[0]
            if href.startswith(("http://", "https://")):
                continue
            path = (f.parent / href).resolve()
            if not path.exists():
                missing.append((f, href, path))

    return missing


def main() -> int:
    broken = check_links()
    missing = check_images()

    print(f"broken links: {len(broken)}")
    for f, href, route in broken:
        print(f"{f}:{href} -> {route}")

    print(f"missing images: {len(missing)}")
    for f, href, path in missing:
        print(f"{f}:{href} -> {path}")

    return 1 if broken or missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
