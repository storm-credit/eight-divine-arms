# 《팔대신병록》 PM 진행 대시보드

상태: `prewriting-system-complete / prose-engine-complete / automated-harness-enabled / manuscript-locked`
업데이트: `2026-08-03`

## 1. 역할

- 최종 오너·정본 승인자: 사용자.
- 실행 PM·오케스트레이터·캐논 관리자: 현재 작업 AI.
- 전문 역할은 PM, 연독, 무협, 전투, 세계관, 캐릭터, 복선, 문체, 연속성, 레드팀 등으로 분리해 문서화한다.
- 실제 별도 에이전트가 실행되지 않았다면 병렬 다중 에이전트 실행이라고 주장하지 않는다.

## 2. 정본 핵심

- 남성 단일 주인공: 서유휘.
- 회귀·빙의·상태창 없음.
- 수집형 정통 무협 웹소설.
- 중심 분량: 8대액트·960화.
- 핵심 인물: 소연후, 연무진, 백여울, 진서하, 곽하진, 도해원, 임강현, 위연호, 문시헌, 고윤재, 석주안, 한려진.
- 로맨스: 백여울 단일 상대, 경쟁적 동행형.
- 세트명: 천하팔대신병 / 천공팔기 / 강호기보록.
- 최종 무공: 만류귀일보 → 개로무극, 최종 오의 팔방개로.

## 3. 설계 완료 상태

- 세계관: COMPLETE.
- 설정집: COMPLETE.
- 천하팔대신병 8개 장부: COMPLETE.
- 8대액트: COMPLETE.
- 32중액트: COMPLETE.
- 소액트·미니아크 운용 원칙: COMPLETE.
- 96개 10화 보상 지도: COMPLETE.
- 맥거핀 설치·증폭·변환·회수 구조: COMPLETE.
- ACT 1 1~110화 화별 개요: COMPLETE.
- 1~30화 상세 비트: COMPLETE.
- 1~10화 장면 설계: COMPLETE.
- 구조적 P0: 0.

핵심 문서:

- `canon/INTEGRATED-WORLD-SETTING-DESIGN-BIBLE-v1.md`
- `outline/8ACT-32SUBACT-CANON-BLUEPRINT-v1.md`
- `outline/NESTED-ARC-MACGUFFIN-PAYOFF-ARCHITECTURE-v1.md`
- `production/ACT1-EP001-110-PRODUCTION-OUTLINE-v1.md`
- `production/ACT1-EP001-030-DETAILED-STORY-BEATS-v1.md`
- `production/ACT1-EP001-010-SCENE-DESIGN-v1.md`

## 4. 작문 시스템 완료

- 서유휘 밀착 3인칭 제한 시점.
- 단문 자체가 아니라 단문 사슬과 기계적 한 문장 문단을 금지.
- 전투는 선행 징후 → 거리·부위 → 대응 → 접촉 → 충격 전달 → 새 위치 → 다음 선택 제한 순으로 묘사.
- 풍경은 이동·전투·생계·감정·단서 중 하나 이상을 바꾸는 기능적 묘사로 운용.
- 한국 웹소설 작품은 문장 복제가 아니라 화자성·연독·공간성·권력 보상의 작동 원리만 참고.
- 대액트 → 중액트 → 소액트 → 미니아크 → 개별 화의 중첩 구조를 사용.

핵심 문서:

- `production/PROSE-WRITING-ENGINE-v1.md`
- `production/KOREAN-WEBNOVEL-STYLE-REFERENCE-MATRIX-v1.md`
- `audit/PROSE-STYLE-QA-HARNESS-v1.md`
- `audit/ORCHESTRA-PROSE-STRUCTURE-HARNESS-REVIEW-2026-08-02.md`

## 5. 자동 하네스 구현

파일:

- `tools/prose_harness.py`
- `config/prose_harness.json`
- `tests/test_prose_harness.py`
- `.github/workflows/prose-harness.yml`
- `operations/AUTOMATED-PROSE-HARNESS-RUNBOOK-v1.md`

자동 검사:

- 폐기 정본 P0.
- 짧은 문장 연속과 한 문장 문단 과밀.
- 반복 문장 첫머리·표현·주의어.
- 고유명 밀도 후보.
- 풍경 감각 신호 부재.
- 전투 공간·퇴로 정보 부족.
- 부상·관계 동반 연속성 신호 누락.

CI 정책:

- 단위 테스트와 폐기 정본 P0만 실패 처리.
- 문체 P1/P2는 리포트만 생성.
- 자동 경고가 문학적 최종 판정을 대신하지 않는다.

감사:

- `audit/AUTOMATED-PROSE-HARNESS-COMPLETION-2026-08-03.md`

## 6. 현행 제작 읽기 순서

1. 최신 사용자 결정.
2. `book_writing.md`.
3. `CLAUDE.md`.
4. 최신 canon 문서.
5. `operations/CURRENT-DESIGN-SOURCE-OF-TRUTH-v1.md`.
6. 8액트·32중액트·96블록 정본 설계.
7. ACT 1 제작 설계.
8. `production/PROSE-WRITING-ENGINE-v1.md`.
9. `audit/PROSE-STYLE-QA-HARNESS-v1.md`.
10. 자동 하네스 실행서와 최신 감사.

여성 서유휘, 소겸, 연소담, 양홍주, 진하, 만류귀종 등은 archive-reference다.

## 7. 남은 Gate

원고 개방 전:

1. EP001 문체·시점·분량 카드.
2. EP001~003 감정 곡선과 훅 카드.
3. 첫 10화 제목·화말 기능표.
4. 사용자 원고 작성 승인.

원고 개방 뒤:

1. EP001 초고.
2. 자동 하네스 실행.
3. 수동 120점 하네스 재판정.
4. EP001~003 묶음 검수.
5. 실제 원고로 자동 임계값 보정.
6. 인물 음성 회귀 코퍼스와 구조화 연속성 JSON 추가.

## 8. 현재 정확한 표현

> **세계관·설정집·960화 장기 구조·ACT 1 제작 설계·작문 엔진·문체 수동 하네스·자동 정적 검사기와 CI까지 구현됐다. 자동 하네스는 폐기 정본과 측정 가능한 문체 위험 위치를 찾으며 문학적 최종 판정은 오케스트라 수동 검수가 담당한다. 실제 원고가 없어 임계값 보정과 원격 CI 성공 확인은 아직 남아 있고, 원고는 사용자 승인 전 잠겨 있다.**
