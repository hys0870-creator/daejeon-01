"""글에 들어간 외부 이미지(유니클로 공식몰, AI 코디 등)를 내려받아 글 폴더에 저장하고,
초안의 이미지 링크를 내려받은 파일 경로로 바꾼다. image-maker가 자동으로 실행한다.

사용법 (블로그 폴더에서):
    python scripts/download_images.py output/<글폴더>

하는 일:
    1. 03_draft_images.md 의 ![캡션](https://...) 이미지를 모두 내려받아
       output/<글폴더>/images/web/NN_이름.jpg 로 저장
    2. 03_draft_images.md 의 링크를 images/web/... 로 바꿈 (원래 주소는 images/web/출처.txt 에 기록)
    3. 실패한 이미지는 링크를 그대로 두고 목록을 출력 (종료 코드 2)
"""
import re
import sys
import urllib.request
from pathlib import Path

EXT = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp", "image/gif": ".gif"}


def safe(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|·—,()]", " ", name)
    return re.sub(r"\s+", "_", name.strip())[:40] or "image"


def fetch(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        # 네이버 에디터가 받는 형식(jpg/png)으로 요청. avif는 피한다.
        "Accept": "image/jpeg,image/png;q=0.9,image/webp;q=0.5",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        ctype = r.headers.get_content_type()
        if ctype not in EXT:
            raise ValueError(f"지원하지 않는 형식 {ctype}")
        return r.read(), EXT[ctype]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    post = Path(sys.argv[1])
    draft = post / "03_draft_images.md"
    text = draft.read_text(encoding="utf-8")
    web = post / "images" / "web"
    web.mkdir(parents=True, exist_ok=True)
    log = web / "출처.txt"
    sources = log.read_text(encoding="utf-8").splitlines() if log.exists() else []

    n, fails = 0, []

    def repl(m: re.Match) -> str:
        nonlocal n
        cap, url = m.group(1), m.group(2)
        if not url.startswith("http"):
            return m.group(0)
        n += 1
        try:
            data, ext = fetch(url)
        except Exception as e:  # 네트워크 차단, 링크 만료 등
            fails.append(f"{cap} — {url} ({e})")
            return m.group(0)
        name = f"{n:02d}_{safe(cap.split(' · ')[0])}{ext}"
        (web / name).write_bytes(data)
        sources.append(f"{name}\t{url}")
        print("저장", name)
        return f"![{cap}](images/web/{name})"

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, text)
    draft.write_text(text, encoding="utf-8")
    log.write_text("\n".join(sources) + "\n", encoding="utf-8")

    print(f"\n완료: {n - len(fails)}장 저장, {len(fails)}장 실패")
    for f in fails:
        print("실패:", f)
    return 2 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
