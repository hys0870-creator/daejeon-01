# EP01. 철근 없이 1,900년? 로마 콘크리트의 비밀

- 카테고리: 건축 × 과학 × 역사
- 길이: 약 39초 (1인 내레이션, 다큐 톤)
- 구조: 훅 → 의외의 사실 → 원리 → 증거 → 꼬리물기(바다) → 여운

---

## 1. 대본 (TTS에 이대로 붙여넣기)

| # | 장면 | 내레이션 | 자막 강조(노랑) |
|---|---|---|---|
| 1 | 판테온 | 판테온의 거대한 돔은 1,900년 가까이 버티고 있습니다. 철근 하나 없이요. | 1,900년 / 철근 |
| 2 | 하얀 알갱이 | 비밀 중 하나는, 오랫동안 실수로 여겨졌던 하얀 알갱이였습니다. | 실수 / 하얀 알갱이 |
| 3 | 뜨거운 혼합 | 로마인들은 생석회를 뜨겁게 섞었고, 그 과정에서 석회 덩어리가 콘크리트 속에 남았는데요. | 생석회 / 뜨겁게 |
| 4 | 자가치유 | 금이 가서 물이 스며들면, 이 덩어리가 녹아 틈을 스스로 메웁니다. | 스스로 |
| 5 | 실험실 | MIT 연구팀이 이 방식을 재현해 금을 냈더니, 2주 만에 물이 새지 않았죠. | 2주 |
| 6 | 바다 방파제 | 더 신기한 건 바다입니다. 보통 콘크리트는 바닷물에 상하는데, 로마 방파제는 바닷물과 화산재가 반응해 새 광물이 자라면서 오히려 단단해졌습니다. | 바다 / 화산재 / 단단해 |
| 7 | 엔딩 | 2천 년 전 로마의 실수는, 사실 2천 년짜리 설계였던 셈입니다. | 2천 년짜리 설계 |

**TTS용 통짜 텍스트:**

> 판테온의 거대한 돔은 천구백 년 가까이 버티고 있습니다. 철근 하나 없이요. 비밀 중 하나는, 오랫동안 실수로 여겨졌던 하얀 알갱이였습니다. 로마인들은 생석회를 뜨겁게 섞었고, 그 과정에서 석회 덩어리가 콘크리트 속에 남았는데요. 금이 가서 물이 스며들면, 이 덩어리가 녹아 틈을 스스로 메웁니다. 엠아이티 연구팀이 이 방식을 재현해 금을 냈더니, 2주 만에 물이 새지 않았죠. 더 신기한 건 바다입니다. 보통 콘크리트는 바닷물에 상하는데, 로마 방파제는 바닷물과 화산재가 반응해 새 광물이 자라면서 오히려 단단해졌습니다. 2천 년 전 로마의 실수는, 사실 2천 년짜리 설계였던 셈입니다.

(숫자·영문은 TTS가 잘못 읽지 않게 한글로 바꿔 두었어요.)

---

## 2. 팩트체크

| 주장 | 확인 결과 | 출처 |
|---|---|---|
| 판테온은 서기 128년쯤 봉헌됐고, 세계 최대의 무근(철근 없는) 콘크리트 돔이다 | ✅ 확인 (2026년 기준 약 1,898년) | MIT News 2023 |
| 하얀 석회 덩어리는 배합이 부실한 흔적으로 여겨져 왔다 | ✅ 확인 | MIT News 2023 |
| 생석회 고온 혼합(hot mixing) → 석회 덩어리가 칼슘 저장소 역할 → 균열 자가치유 | ✅ 확인 (Masic 연구팀, *Science Advances* 2023.1) | MIT News |
| 재현 시료에 균열을 내고 물을 흘렸더니 약 2주 만에 균열이 메워져 물이 멈췄고, 대조군은 계속 샜다 | ✅ 확인 | MIT News |
| 바닷물과 화산재가 반응해 알루미늄 토버모라이트·필립사이트가 생기고, 시간이 지나며 더 단단해진다 | ✅ 확인 (Jackson 연구팀, *American Mineralogist* 2017) | Popular Science |

⚠️ 표현상 주의할 점:
- 판테온이 버틴 이유는 석회 덩어리 하나가 아니에요. 위로 갈수록 가벼운 골재를 쓴 것 등 여러 요인이 있어서 "비밀 **중 하나**"라고 표현했습니다.
- "실수가 아니라 설계였다"는 연구팀의 해석이에요. 엔딩은 "~였던 셈"으로 단정을 피했습니다.

---

## 3. 장면별 AI 영상 프롬프트 (Kling / Higgsfield, 9:16, 5초)

**공통 스타일 꼬리말** (매 프롬프트 끝에 붙이기):
`cinematic documentary, photorealistic, warm golden-hour light, soft volumetric haze, shallow depth of field, slow smooth camera, muted earthy palette with warm highlights, 9:16 vertical, no text, no watermark`

**공통 네거티브:** `text, letters, subtitles, watermark, logo, distorted faces, extra fingers, cartoon, oversaturated`

**추천 순서:** 이미지 모델로 첫 프레임을 먼저 만들고, Kling의 image-to-video로 움직이면 장면끼리 톤이 잘 맞아요.

| # | 길이 | 프롬프트 |
|---|---|---|
| 1 | 5초 | Low-angle shot inside the Pantheon in Rome, camera slowly tilts up toward the massive coffered concrete dome, a beam of sunlight pours through the oculus, dust particles floating in the light, sense of awe and scale |
| 2 | 5초 | Extreme macro shot of an ancient grey Roman concrete surface, camera slowly pushes in on small bright white lime chunks embedded in the rough aggregate, raking side light reveals texture |
| 3 | 6초 | Ancient Roman construction site, two workers in simple tunics mix quicklime with volcanic ash in a large wooden trough, thick white steam and heat shimmer rising from the mixture, camera slowly dollies forward |
| 4 | 5초 | Macro shot of a thin crack spreading through old concrete, a trickle of water seeps in, white mineral crystals slowly grow from the edges and seal the crack, time-lapse feel, glistening water |
| 5 | 5초 | Modern materials-science laboratory, a cracked cylindrical concrete sample in a clear test rig with water flowing through it, a scientist in a lab coat seen from behind observing, cool blue lab light mixed with warm practical lights |
| 6a | 5초 | Aerial drone shot of an ancient Roman harbor breakwater made of weathered concrete blocks, turquoise Mediterranean waves crashing against it, camera slowly orbits |
| 6b | 5초 | Microscopic view inside concrete, seawater flows into pores and delicate plate-like mineral crystals grow and interlock, glowing subtly, scientific visualization feel |
| 7 | 5초 | Exterior of the Pantheon at dusk, camera slowly pulls back and rises to reveal the full portico and the dome against a warm sky, timeless and contemplative mood |

(6번 장면은 6a에서 6b로 넘어가게 두 클립을 이어 붙입니다. 클립 이름은 `06.mp4` 하나로 합치거나, 두 개를 보내 주시면 제가 붙일게요.)

---

## 4. 내레이션 음성 만드는 법

- **추천 툴:** 타입캐스트, ElevenLabs, 캡컷 TTS 중 편한 것
- **톤:** 차분한 다큐 내레이터(남성 저음 또는 여성 아나운서), 속도는 1.0~1.1배
- **내보내기:** `narration.mp3` / 자막(SRT) 내보내기가 되면 `narration.srt`도 함께
  - SRT가 있으면 자막 타이밍이 정확히 맞아요. 없으면 글자 수로 자동 배분합니다.
- 7번 엔딩 문장 앞에는 0.5초 정도 쉬도록 문장 사이에 쉼을 넣어 주세요.

---

## 5. 업로드용

**커버 문구:** 철근 없이 1,900년? 🏛️

**캡션:**
> 판테온은 어떻게 2천 년 가까이 버텼을까?
> 오랫동안 '실수'라고 여겨졌던 하얀 알갱이의 정체 🤍
>
> 📚 참고: MIT Masic 연구팀(Science Advances, 2023), Utah대 Jackson 연구팀(American Mineralogist, 2017)
>
> 알아두면 쓸데없지만 신기한 잡지식, 매일 하나씩.
> 다음엔 뭐가 궁금해요? 댓글로 남겨주세요 👇

**해시태그 (8개):** #알쓸신잡 #잡학지식 #로마 #판테온 #건축 #과학상식 #역사 #릴스

**고정 댓글:** "더 신기한 건, 요즘 연구팀들이 이 2천 년 전 레시피로 '스스로 낫는 콘크리트'를 연구하고 있다는 것 🧪"

**업로드할 때:** 실사 AI 영상이므로 인스타 업로드 화면의 고급 설정에서 **'AI 정보' 라벨을 켜 주세요.**
