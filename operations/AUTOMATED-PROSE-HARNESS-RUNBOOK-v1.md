# 《팔대신병록》 자동 문체·연속성 하네스 실행서 v1

상태: `active-runbook / automation-enabled / manuscript-locked`

## 1. 역할

자동 하네스는 좋은 문장을 판정하지 않는다. 다음과 같은 측정 가능한 위험 위치만 찾는다.

- 폐기된 인명·성별·무공명.
- 짧은 문장 연속과 한 문장 문단 과밀.
- 같은 문장 첫머리·3어절 표현·주의 표현 반복.
- 풍경 감각 신호 부재.
- 전투는 있으나 거리·방향·발자리·퇴로가 보이지 않는 문제.
- 신규 고유명 과밀 후보.
- 부상·소유물·관계의 연속성 동반 신호 누락.

최종 출고 판정은 `audit/PROSE-STYLE-QA-HARNESS-v1.md`에 따라 PM·문체·무협·전투 검수자가 수행한다.

## 2. 파일

- 실행기: `tools/prose_harness.py`
- 설정: `config/prose_harness.json`
- 단위 테스트: `tests/test_prose_harness.py`
- CI: `.github/workflows/prose-harness.yml`
- 수동 하네스: `audit/PROSE-STYLE-QA-HARNESS-v1.md`

## 3. 로컬 실행

Python 3.11 이상, 외부 패키지 불필요.

```bash
python tools/prose_harness.py manuscripts/EP001.md
```

디렉터리 전체:

```bash
python tools/prose_harness.py manuscripts \
  --recursive \
  --report reports/prose-qa.md
```

폐기 정본 발견 시 실패:

```bash
python tools/prose_harness.py manuscripts \
  --recursive \
  --strict-canon
```

문체 경고까지 실패시키는 실험 모드:

```bash
python tools/prose_harness.py manuscripts/EP001.md \
  --fail-on-warning
```

기본 제작에서는 `--fail-on-warning`을 사용하지 않는다. 단문과 반복 표현은 장면 의도에 따라 정당할 수 있기 때문이다.

## 4. GitHub Actions

다음 경로가 변경될 때 실행한다.

- `tools/**`
- `config/**`
- `tests/**`
- `manuscripts/**`

CI 동작:

1. 단위 테스트 실행.
2. 원고 디렉터리가 존재하면 전체 검사.
3. 폐기 정본 P0가 있으면 실패.
4. P1/P2 문체 경고는 리포트로만 남김.
5. `prose-qa-report` artifact 업로드.

## 5. 설정 보정

실제 1~3화가 작성되면 다음 값을 보정한다.

- `short_sentence_words`
- `short_chain_limit`
- `one_sentence_paragraph_ratio_warn`
- `watch_terms`별 허용 횟수
- 풍경·전투 신호 어휘
- 연속성 동반 신호

한 작품의 기준은 실제 원고 3화 이상에서 보정해야 한다. 초고가 없을 때 숫자를 과도하게 좁히지 않는다.

## 6. 수동 검수와의 결합

자동 리포트 뒤 반드시 다음을 사람이 판단한다.

- 짧은 문장이 충격과 결정을 강화했는가.
- 긴 문장이 공간과 공방을 선명하게 했는가, 아니면 늘어졌는가.
- 풍경이 이동·전투·생계·감정을 바꾸는가.
- 전투의 모든 동작을 설명해 속도가 죽지 않았는가.
- 대사가 인물마다 다른가.
- 맥거핀 설치·증폭·변환·회수 단계가 현재 위치에 맞는가.
- 중액트와 소액트의 부분 결산이 실제로 체감되는가.

## 7. 알려진 한계

- 한국어 형태소 분석을 사용하지 않아 어절 수는 정규식 근사치다.
- 신규 고유명은 Markdown 강조 표기와 설정 목록을 기준으로 보수적으로 찾는다.
- 감정·문학성·박진감·풍경의 아름다움은 자동 판정할 수 없다.
- 자동 경고를 이유로 문장을 기계적으로 길게 합치거나 표현을 삭제하지 않는다.

## 8. 원고 개방 후 순서

1. EP001 초고 작성.
2. 자동 하네스 실행.
3. P0 즉시 수정.
4. P1/P2 위치를 수동 하네스로 재판정.
5. EP001~003 묶음 검수.
6. 실제 결과로 설정 임계값 보정.
7. 10화 묶음에서 중액트·복선·보상 검수.
