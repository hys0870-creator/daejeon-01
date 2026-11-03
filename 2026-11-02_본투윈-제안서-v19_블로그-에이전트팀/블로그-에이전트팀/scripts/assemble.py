import re, sys, html, os
d = sys.argv[1]
_g = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'guide', 'style_guide.md')
try:
    NICK = re.search(r'닉네임: \*\*(.+?)\*\*', open(_g, encoding='utf-8').read()).group(1)
except Exception:
    NICK = '[닉네임]'
s = open(f'{d}/03_draft_images.md', encoding='utf-8').read()
_, fm, body = s.split('---', 2)
title = re.search(r'title:\s*(.+)', fm).group(1).strip()
tags = re.findall(r'#[^,\]\s]+', fm)
body = body.strip()

todo_photo = re.findall(r'\[사진: ([^\]]+)\]', body)
todo_ai = re.findall(r'\[AI코디 (\d+): ([^\]]+)\]', body)
todo_chk = re.findall(r'\[확인 필요: ([^\]]+)\]', body)
n_assume = body.count('[테스트용 가정')

# final.md
md = [f'# {title}', '', body, '', ' '.join(tags), '', '---', '', '## 발행 전 할 일', '']
if n_assume: md.append(f'- [ ] 테스트용 가정 착용 문단 {n_assume}곳 → 실제 착용 후 내용 교체, 표시 삭제')
n_off = body.count('image.uniqlo.com')
n_web = len(re.findall(r'!\[[^\]]*\]\(https?://', body))
if n_web: md.append(f'- [ ] 아직 링크로 남은 이미지 {n_web}장 → python scripts/download_images.py output/{os.path.basename(os.path.normpath(d))} 실행 후 다시 조립')
if n_off: md.append('- [ ] 공식몰 사진 출처 캡션 유지, 계속 운영할 블로그라면 직접 찍은 사진으로 교체 검토')
md.append('- [ ] 네이버 업로드: upload 폴더의 사진을 번호 순서대로 올리고 업로드순서.txt 캡션 붙이기')
for c in todo_chk: md.append(f'- [ ] 확인 필요: {c}')
for i, p in enumerate(todo_photo, 1): md.append(f'- [ ] 사진 {i}: {p}')
for n, p in todo_ai: md.append(f'- [ ] AI 코디 {n}: ai_prompts.md 프롬프트로 생성 → "{p}"')
open(f'{d}/final.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')

# final.html
def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\[(테스트용 가정[^\]]*)\]', r'<mark class="as">\1</mark>', t)
    t = re.sub(r'\[(확인 필요:[^\]]*)\]', r'<mark>\1</mark>', t)
    return t
out = []
for blk in re.split(r'\n\s*\n', body):
    lines = [l for l in blk.split('\n') if l.strip()]
    if not lines: continue
    if lines[0].startswith('>'):
        q = [l[1:].strip() for l in lines]
        if len(q) > 1:
            out.append('<div class="pbox"><div class="pn">' + inline(q[0]) + '</div>' + ''.join(f'<div>{inline(x)}</div>' for x in q[1:]) + '</div>')
        else:
            out.append(f'<blockquote>{inline(q[0])}</blockquote>')
        continue
    if lines == ['---']:
        out.append('<hr>'); continue
    m = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)', lines[0])
    if m and len(lines) == 1:
        cap = m.group(1); src = m.group(2)
        out.append(f'<figure><img src="{html.escape(src)}" alt="{html.escape(cap)}" loading="lazy"><figcaption>{html.escape(cap)}</figcaption></figure>'); continue
    m = re.fullmatch(r'\[사진: ([^\]]+)\]', lines[0])
    if m and len(lines) == 1:
        out.append(f'<div class="slot">📷 내 사진 넣을 자리<br><small>{html.escape(m.group(1))}</small></div>'); continue
    m = re.fullmatch(r'\[AI코디 (\d+): ([^\]]+)\]', lines[0])
    if m and len(lines) == 1:
        out.append(f'<div class="slot ai">AI 코디 이미지 {m.group(1)} 넣을 자리 <small>(ai_prompts.md)</small><br><small>{html.escape(m.group(2))}</small><br><small class="cap">캡션: AI로 생성한 코디 예시 이미지입니다</small></div>'); continue
    m = re.fullmatch(r'\[([^\]]+)\]\((https?://[^)]+)\)', lines[0])
    if m and len(lines) == 1:
        out.append(f'<a class="lcard" href="{html.escape(m.group(2))}">{html.escape(m.group(1))}<small>{html.escape(m.group(2))}</small></a>'); continue
    out.append('<p>' + '<br>'.join(inline(l) for l in lines) + '</p>')

todo_html = ''.join(f'<li>{html.escape(x[6:] if x.startswith("- [ ] ") else x)}</li>' for x in md[md.index('## 발행 전 할 일')+2:])
page = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>
body{{margin:0;background:#fff;color:#222;font-family:"Nanum Gothic","Malgun Gothic","Apple SD Gothic Neo",sans-serif}}
.todo{{background:#FFF8E1;border-bottom:1px solid #F0DFA8;padding:16px 20px;font-size:14px;line-height:1.7}}
.todo b{{font-size:15px}}.todo ul{{margin:6px 0 0;padding-left:20px}}
article{{max-width:740px;margin:0 auto;padding:40px 16px 80px;text-align:center}}
h1{{font-size:26px;line-height:1.4;margin:0 0 10px;text-align:left}}
.by{{color:#999;font-size:13px;text-align:left;padding-bottom:24px;border-bottom:1px solid #eee;margin-bottom:36px}}
p{{font-size:16px;line-height:1.8;margin:0 0 28px}}
blockquote{{margin:56px auto 32px;font-size:19px;font-weight:700;position:relative;padding:22px 0}}
blockquote:before,blockquote:after{{content:"\\201C";display:block;font-size:42px;color:#bbb;line-height:.6;font-family:Georgia,serif}}
blockquote:after{{content:"\\201D";margin-top:18px}}
.pbox{{border:1px solid #ddd;padding:20px;margin:48px auto 28px;max-width:420px;font-size:15px;line-height:1.9}}
.pbox .pn{{font-weight:700;font-size:17px;margin-bottom:4px}}
figure{{margin:0 0 28px}}img{{width:100%;display:block;background:#f3f3f3;min-height:60px}}
figcaption{{font-size:13px;color:#999;margin-top:8px}}
.slot{{border:2px dashed #bbb;color:#888;padding:46px 16px;margin:0 0 28px;font-size:15px;line-height:1.7;background:#fafafa}}
.slot.ai{{border-color:#B9A6E0;color:#7461A8;background:#F8F5FF}}.slot .cap{{color:#999}}
mark{{background:#FFE58A;padding:1px 4px}}mark.as{{background:#FFD3C2;font-size:13px}}
hr{{border:0;border-top:1px solid #eee;margin:48px 0}}
.lcard{{display:block;border:1px solid #ddd;padding:16px;text-align:left;color:#222;text-decoration:none;font-weight:700;margin-bottom:28px}}
.lcard small{{display:block;color:#999;font-weight:400;margin-top:4px}}
.tags{{color:#3478C6;font-size:14px;line-height:1.9;margin-top:40px}}
</style></head><body>
<div class="todo"><b>발행 전 할 일 (미리보기 전용 — 네이버에는 붙이지 마세요)</b><ul>{todo_html}</ul></div>
<article><h1>{html.escape(title)}</h1><div class="by">{html.escape(NICK)} · {__import__("datetime").date.today().strftime("%Y. %-m. %-d.")}</div>
{chr(10).join(out)}
<div class="tags">{' '.join(html.escape(t) for t in tags)}</div></article></body></html>'''
import base64, shutil, mimetypes
def _embed(m):
    src = m.group(1)
    fp = os.path.join(d, src)
    if src.startswith('http') or not os.path.exists(fp): return m.group(0)
    mt = mimetypes.guess_type(fp)[0] or 'image/png'
    data = open(fp, 'rb').read()
    try:  # 미리보기용으로만 블로그 폭(966px)에 맞춰 줄인다. upload/ 원본은 그대로.
        from PIL import Image
        import io
        im = Image.open(fp)
        if im.width > 1000 or len(data) > 400_000:
            im = im.convert('RGB'); im.thumbnail((966, 966 * 4))
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=85); data = buf.getvalue(); mt = 'image/jpeg'
    except Exception:
        pass
    return 'src="data:%s;base64,%s"' % (mt, base64.b64encode(data).decode())
open(f'{d}/final.html', 'w', encoding='utf-8').write(re.sub(r'src="([^"]+)"', _embed, page))
up = os.path.join(d, 'upload'); shutil.rmtree(up, ignore_errors=True); os.makedirs(up)
order = []
for i, (cap, src) in enumerate(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', body), 1):
    fp = os.path.join(d, src)
    if src.startswith('http') or not os.path.exists(fp):
        order.append(f'{i:02d}\t(링크 — 아직 파일 없음)\t{cap}'); continue
    name = f'{i:02d}{os.path.splitext(fp)[1]}'
    shutil.copy(fp, os.path.join(up, name)); order.append(f'{name}\t{cap}')
open(os.path.join(up, '업로드순서.txt'), 'w', encoding='utf-8').write('번호 순서대로 네이버 에디터에 올리고, 각 사진 아래 캡션을 붙이세요.\n\n' + '\n'.join(order) + '\n')
print('ok', len(todo_photo), len(todo_ai), len(todo_chk), n_assume)
