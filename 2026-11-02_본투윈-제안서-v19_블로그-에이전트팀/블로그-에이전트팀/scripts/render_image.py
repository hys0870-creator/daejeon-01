"""HTML 파일을 PNG 이미지로 캡처한다.

사용법:
    python scripts/render_image.py <입력.html> <출력.png> [--width 966] [--height 1080] [--scale 2]

--height 를 생략하면 페이지 내용 높이에 맞춰 캡처한다.
처음 한 번만 설치:
    pip install playwright
    playwright install chromium
"""
import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("html")
    p.add_argument("png")
    p.add_argument("--width", type=int, default=966)
    p.add_argument("--height", type=int, default=None)
    p.add_argument("--scale", type=float, default=2.0)
    a = p.parse_args()

    html = Path(a.html).resolve()
    out = Path(a.png).resolve()
    if not html.exists():
        print(f"HTML 파일이 없습니다: {html}")
        return 1
    out.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(
            viewport={"width": a.width, "height": a.height or 100},
            device_scale_factor=a.scale,
        )
        page.goto(html.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        if a.height:
            page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": a.width, "height": a.height})
        else:
            h = page.evaluate(
                "Math.ceil(Math.max(document.body.scrollHeight,"
                " document.body.getBoundingClientRect().height))"
            )
            page.set_viewport_size({"width": a.width, "height": h})
            page.screenshot(path=str(out), full_page=True)
        browser.close()

    print(f"저장: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
