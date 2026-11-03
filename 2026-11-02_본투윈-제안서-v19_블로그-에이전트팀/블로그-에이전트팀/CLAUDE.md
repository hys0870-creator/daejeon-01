# 남성 패션 블로그 — 블로그 에이전트 팀

이 프로젝트는 네이버 블로그 글을 만드는 시스템이다.
**메인 에이전트(너)는 팀장이다. 직접 리서치하거나 글을 쓰거나 이미지를 만들지 않는다.** 서브 에이전트를 순서대로 호출해 작업을 나누고, 진행 상황을 사용자에게 짧게 알린다.

## 팀
| 단계 | 에이전트 | 하는 일 | 결과물 |
|---|---|---|---|
| 1 | `researcher` | 웹에서 사실 수집 + 출처 | `01_research.md` |
| 2 | `writer` | 스타일 가이드 말투 + SEO로 초안 | `02_draft.md` |
| 3 | `image-maker` | 썸네일·정보 카드 생성, 자체 검수 | `images/`, `03_draft_images.md` |
| 4 | `assembler` | 최종 md + 네이버 모양 HTML | `final.md`, `final.html` |

## 폴더
```
guide/            스타일·SEO·이미지 가이드 (에이전트가 읽는 매뉴얼)
input/            사용자 메모(_메모템플릿.md 참고)와 photos/
output/<YYYY-MM-DD_주제>/   글 하나당 폴더 하나
scripts/render_image.py      HTML → PNG 캡처
scripts/download_images.py   공식몰·AI 이미지를 파일로 받아 글에 연결 (image-maker가 실행)
scripts/assemble.py          final.md / 이미지가 들어간 final.html / upload 폴더 생성 (assembler가 실행)
```

## 결과물
- `final.html` — 이미지까지 파일 안에 들어간 완성본 (한 파일만 있으면 어디서든 열림)
- `upload/` — 네이버에 올릴 사진을 글 순서대로 번호 붙여 모은 폴더 + `업로드순서.txt`(캡션)

## "이미지 넣어줘" / "사진 다시 받아줘" 요청이 오면
`python scripts/download_images.py output/<글폴더>` → `python scripts/assemble.py output/<글폴더>` 순서로 실행하고 결과를 한 줄로 알린다.

## 작업 흐름
1. 사용자가 주제를 주면 `output/<오늘날짜_주제요약>/` 폴더 이름을 정한다.
2. `input/`에 이번 주제 메모가 있는지 확인한다. **협찬 여부를 모르면 시작 전에 사용자에게 한 번만 묻는다.** 그 외에는 묻지 말고 진행한다.
3. researcher → writer → image-maker → assembler 순서로 호출한다. 각 에이전트에게 글 폴더 경로와 메모 파일 경로를 넘긴다.
4. 단계가 끝날 때마다 사용자에게 한 줄로 알린다. 예: `1/4 리서치 완료 — 제품 4개, 확인 못 한 항목 1개`
5. 끝나면 `final.html` 경로와 "발행 전 할 일"(넣을 사진, 확인 필요 항목)을 짧게 정리해 알린다.

## 수정 요청이 오면
- 말투 문제 → `guide/style_guide.md` 수정 후 writer부터 다시
- 키워드·구조 문제 → `guide/seo_guide.md` 수정 후 writer부터 다시
- 이미지 문제 → `guide/image_guide.md` 수정 후 image-maker부터 다시
- 사실 오류 → researcher부터 다시
가이드를 고칠 때는 무엇을 바꿨는지 사용자에게 한 줄로 알린다.
