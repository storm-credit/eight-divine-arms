# 《팔대신병록》 PM 진행 대시보드

상태: `korean-webnovel-fun-design / human-edit-pending`
총괄: PM 오케스트레이터
상위 정책: [`../book_writing.md`](../book_writing.md)
실행 규칙: [`../CLAUDE.md`](../CLAUDE.md)
메타 프롬프팅: [`META-PROMPTING-PROTOCOL-v1.md`](META-PROMPTING-PROTOCOL-v1.md)
범위 고정: [`PROJECT-DESIGN-SCOPE-LOCK-v1.md`](PROJECT-DESIGN-SCOPE-LOCK-v1.md)
계획 이탈: [`PLAN-DEVIATION-LOG.md`](PLAN-DEVIATION-LOG.md)
한국 웹소설 감사: [`../audit/KOREAN-WEBNOVEL-MARTIAL-MOTIF-AND-SERIAL-FUN-AUDIT-v1.md`](../audit/KOREAN-WEBNOVEL-MARTIAL-MOTIF-AND-SERIAL-FUN-AUDIT-v1.md)
주인공 이름: [`PROTAGONIST-NAME-DECISION-v1.md`](PROTAGONIST-NAME-DECISION-v1.md)
재미 Human Edit: [`KOREAN-WEBNOVEL-FUN-HUMAN-EDIT-PACKET-v1.md`](KOREAN-WEBNOVEL-FUN-HUMAN-EDIT-PACKET-v1.md)

## 1. 우리가 만드는 것

**한국 플랫폼에서 연재할 무협 웹소설 《팔대신병록》의 완성형 작품 설계 패키지.**

설정 백과사전도 현재 원고도 아니다.

필수 산출물:

1. 설정·세계 시스템
2. 인물·관계
3. 결말·전체 플롯
4. 무료분 1~25화·소구간
5. 전체 화수·막별 화수
6. 웹소설 화 단위 Outline
7. 연속성·누락·과잉·재미·연독 최종 감사
8. 집필 준비 판정

## 2. 현재 위치

| 영역 | 상태 | 판정 |
|---|---|---|
| 작품 헌법·세계·시스템 | `canon` | 유지 |
| 인물·관계 프레임 | `canon-framework` | 유지, 플롯 통합 재검토 |
| 주인공 이름 | `서유휘` | 사용자 결정, Plot Master 전 동기화 |
| 기존 플롯 v2 | `superseded-for-redesign` | 참고 후보 |
| 플롯 재설계 v3 | `recommended-default / human-edit-pending` | B안 PM 권고 |
| R-1 라이벌 후보 | `four-options / human-edit-pending` | 진아령형 PM 권고 |
| 서유휘 음성 후보 | `four-options / human-edit-pending` | 생활형 반문 혼합안 PM 권고 |
| 무료분 1~5화 훅 | `four-options / human-edit-pending` | H-C+A+D 조합 PM 권고 |
| STORY FUN GATE | `partial / not-passed` | 동료 케미·작은 승리·6~25화 미설계 |
| 한국 웹소설 화 단위 | `redesign-required` | 무료분 Master·전체 화수 미설계 |
| 기존 5막·8구간 | `validation-framework` | 비교 자료 |
| 기존 50장 Outline | `validation-draft / revision-required` | 화 단위 정본 아님 |
| 장면·원고 | `locked` | 미착수 |

현재 표현은 **핵심 기반 유지, 한국 웹소설 재미 후보 설계 완료, 사용자 통합 선택 대기**다.

## 3. 실행 프로토콜

모든 큰 작업은 다음을 거친다.

1. 컨텍스트 덤핑
2. 결과를 크게 바꾸는 누락 질문 최대 3개
3. 프롬프트 깎아내기
4. 역할·목표·제약·성공조건·중지요건·출력 형식 명시
5. 실행환경별 변환
6. 맹점 훑기와 프리모텀
7. 디자인 시안 4개
8. 사용자 Human Edit
9. 자기점검과 독립 점검
10. 계획 이탈 기록

## 4. 플롯 재설계 네 안

| 안 | 구조 | 상태 |
|---|---|---|
| A | 보증 회복형 | 후보 |
| B | 장기 분산 호송형 | **PM 권고** |
| C | 회수자 추적형 | 후보 |
| D | 연해 공동체 방어형 | 후보 |

PM 권고 조합:

- A의 분점 보증·가족 가업 stakes
- B의 하나의 장기 복합 호송
- C의 반복 현장 회수자
- D의 가족·공방·지역 공동체 영구 손실

## 5. 한국 웹소설 재미 후보

### 5.1 R-1 라이벌

문서: [`../design/R1-RECURRING-RIVAL-FOUR-OPTIONS-v1.md`](../design/R1-RECURRING-RIVAL-FOUR-OPTIONS-v1.md)

PM 권고:

> **진아령형 경쟁 표국 특급 회수표사**

- 집중 인계와 명확한 책임을 신봉
- 첫 등장부터 사람을 살리지만 생존자·인계함을 압류
- 서유휘와 같은 표국 언어를 반대로 사용
- 최종 흑막이 아니라 구조·계약·전투·임시 공조를 반복하는 직업 라이벌

### 5.2 서유휘 음성·행동 리듬

문서: [`../design/SEO-YUHWI-VOICE-AND-ACTION-RHYTHM-FOUR-OPTIONS-v1.md`](../design/SEO-YUHWI-VOICE-AND-ACTION-RHYTHM-FOUR-OPTIONS-v1.md)

PM 권고:

- 표면 음성: 생활형 반문·짧은 직설
- 현장 판단: 검표·하중·연결부 관찰
- 내면 결함: 책임을 먼저 떠안는 습관

보정:

- 현대식 유행어 금지
- 사망·중상 장면에서 유머 중지
- 말로 이기는 장면보다 행동의 비용 강조
- 동료가 서유휘 판단을 이기는 장면을 막마다 배치

### 5.3 무료분 1~5화

문서: [`../design/FREE-EPISODES-1-5-HOOK-FOUR-OPTIONS-v1.md`](../design/FREE-EPISODES-1-5-HOOK-FOUR-OPTIONS-v1.md)

PM 권고:

> **H-C 먼저 분산하는 구조 + H-A 조선소 붕괴 + H-D 진아령 첫 구조·압류**

1. 서유휘가 안전 불일치를 발견하고 사람·부품을 먼저 분산
2. 조선소 붕괴, 진아령이 더 많은 사람을 구조
3. 분산 덕분에 전멸은 막지만 증인 실종·분점 동결 발생
4. 두 사람이 제3의 회수자를 쫓으며 첫 임시 공조
5. 서유휘가 이름과 분점 보증을 걸고 장기 분산 호송을 자청

## 6. 한국 웹소설 재미 엔진

표면 장르:

> **직업 호송 모험·추적 무협**

하부 엔진:

- 역사 미스터리
- 권리·기록 갈등
- 가족·가업 비용
- 저강도 기환

권고 배합:

- 직업·호송 목표 35%
- 캐릭터 음성·동료 케미·라이벌 30%
- 세계·세력·재등장 보상 20%
- 고개념 무협 재해석 15%

## 7. 모티브 참고 위계

### 1차 — 한국 무협 웹소설 회차 재미

- 《환생표사》
- 《광마회귀》
- 《화산귀환》
- 《무림서부》
- 《일타강사 백사부》
- 《절대회귀》
- 《시한부 천재가 살아남는 법》

### 2차 — 세계·세력·장기 교차 보상

- 한백림 《한백무림서》
  - 《무당마검》
  - 《화산질풍검》
  - 《천잠비룡포》

### 3차 — 장르 원형·보조 구조

- 김용·고룡 등 중화권 무협
- 《수호전》
- 서구 모험·미스터리 장편

## 8. FUN 후보 교차감사

문서: [`../audit/KOREAN-WEBNOVEL-FUN-CANDIDATES-CROSS-AUDIT-v1.md`](../audit/KOREAN-WEBNOVEL-FUN-CANDIDATES-CROSS-AUDIT-v1.md)

판정:

- P0 구조 결함: 없음
- P1 보정: 서유휘 무모함·진아령 과강화·무료분 화물 과밀·2~3화 행정극화 등
- FUN GATE: 아직 미통과
- Human Edit 뒤 무료분 정밀 기능표와 6~25화 설계 필요

무료분 전면 대상 권고:

1. 증인 1명
2. 안전 부품 상자 1개
3. 분점 보증

## 9. 사용자 통합 선택 대기

Human Edit 패킷:

- [`KOREAN-WEBNOVEL-FUN-HUMAN-EDIT-PACKET-v1.md`](KOREAN-WEBNOVEL-FUN-HUMAN-EDIT-PACKET-v1.md)

PM 통합 권고:

1. B 장기 분산 호송형
2. 주손실 ① 분점 보증·직업 신용
3. 진아령형 반복 라이벌
4. 서유휘 음성 혼합안
5. 무료분 권고 조합

명시 응답 예:

- `통합 권고 승인`
- `B, ①, 진아령, 음성 혼합안, 무료분 권고안 승인`

## 10. 승인 뒤 작업

1. 사용자 선택 결정 로그
2. 서유휘 이름·욕망·음성 정본 동기화
3. 진아령 정밀 카드와 반복 대결 설계
4. 무료분 전면 대상 3개 확정
5. 무료분 1~5화 기능표
6. 핵심 동료 케미 4안
7. 무료분 6~15화 첫 소구간
8. 무료분 16~25화 첫 결산
9. FUN GATE 재감사
10. Plot Master v3
11. 전체 화수·막별 화수 후보 4안
12. 웹소설 화 단위 Outline
13. 시간·이동·부상·권리·단서·절단 장부
14. 독립 교차감사와 Outline Human Edit
15. 전체 설계 최종 감사

## 11. 지금 하지 않는 것

- 기존 50장 Outline 직접 정본화
- 백과사전식 설정 확장
- 장면별 완성 대사·묘사·전투 수순
- 기존 60장안 자동 복원
- 웹소설 화와 출간 장 혼용
- 장편 초고

사용자 명시 선택 전에는 Plot Master v3와 웹소설 Outline을 정본으로 만들지 않는다.
