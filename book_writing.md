# 《팔대신병록》 집필·설계 최상위 정책

상태: `canon-policy / epic-fate-braided-tonal-reset`
역할: 저장소 최상위 운영 정책
총괄: PM 오케스트레이터
실행 규칙: [`CLAUDE.md`](CLAUDE.md)
메타 프롬프팅: [`operations/META-PROMPTING-PROTOCOL-v1.md`](operations/META-PROMPTING-PROTOCOL-v1.md)
작법 에이전트: [`operations/NARRATIVE-CRAFT-AGENT-ORCHESTRATION-v1.md`](operations/NARRATIVE-CRAFT-AGENT-ORCHESTRATION-v1.md)
작품 감각 재설정: [`operations/TONAL-DIRECTION-RESET-DECISION-v1.md`](operations/TONAL-DIRECTION-RESET-DECISION-v1.md)
대하 무협 4안: [`design/TIANLONG-BABU-TONAL-VISION-FOUR-OPTIONS-v1.md`](design/TIANLONG-BABU-TONAL-VISION-FOUR-OPTIONS-v1.md)
완성 구성표: [`operations/DESIGN-PACKAGE-COMPLETION-MATRIX-v2.md`](operations/DESIGN-PACKAGE-COMPLETION-MATRIX-v2.md)

## 1. 프로젝트 목표

현재 목표는 **한국 플랫폼에서 연재할 대하 무협 웹소설 《팔대신병록》의 완성형 작품 설계 패키지**다.

작품 감각 목표:

> 서로 다른 삶과 비극을 가진 복수의 영웅이 문파·혈연·정체·국가·팔대신병을 통해 교차하는 호쾌하고 비애감 있는 무협.

《천룡팔부》의 인물·반전·장면을 복사하지 않는다. 참고하는 것은:

- 복수 영웅의 독립 서사와 운명 교차
- 개인→가족·사승→문파·공동체→민족·국가로 확대되는 갈등
- 선의·의리·욕망이 파국을 만드는 인과
- 무공과 정체의 결합
- 호쾌함·유머·비애·비극의 공존

한국 웹소설의 명확한 독자 앵커·회차 보상·무료분 진입은 유지한다.

## 2. 우리가 만드는 것

본선 산출물:

1. 작품 감각과 한 문장 약속
2. 결말과 역산 인과
3. 공동 주인공 구조와 인물별 독립 결말
4. 맥거핀·비밀·설치 회수 구조
5. 세계·무공·기환·팔대신병 핵심
6. 인물·관계·세력
7. 전체 플롯
8. 총화수·액트·서브액트
9. 무료분 1~25화
10. 웹소설 화 단위 Outline
11. 용어·집필법
12. 시간·이동·부상·정보·관계·권리·절단 장부
13. 작법별·FUN·연속성 최종 감사
14. 집필 준비 판정

현재 목표가 아닌 것:

- 설정 백과사전 완성
- 장면별 완성 대사·묘사
- 장편 초고
- 과거 60장·50장안 자동 복원

## 3. 기본 원칙

- 최신 사용자 결정이 과거 승인안보다 우선한다.
- 작품 감각을 정하기 전에 표국·조선소·호송 구조를 정본화하지 않는다.
- 결말을 먼저 설계하고 플롯·액트·화수를 역산한다.
- 맥거핀은 인물을 움직이는 장치이며 작품의 감정 핵심을 대체하지 않는다.
- 팔대신병을 하나씩 수집하는 퀘스트로 만들지 않는다.
- 중요 설계는 4안·Human Edit·독립 감사를 거친다.
- 다중 주인공을 사용해도 한국 웹소설 독자 앵커를 명확히 한다.
- 설정은 인물 선택·플롯 인과·전투·회차 보상에 필요한 만큼 활성화한다.
- 재미·연독·회차 절단은 설정 정합성과 같은 수준의 Gate다.
- 사용자의 `진행`·`이어서`를 고영향 선택 승인으로 자동 해석하지 않는다.
- 원고는 설계 패키지 승인 전까지 잠근다.

## 4. 현재 상태

유지:

- 세계·무공·기환·팔대신병 핵심: `canon`
- 주인공 이름 서유휘: `user-selected`
- 서유휘의 검표·인계 경력, 과오, 신체 제약: `reusable-canon-framework`
- 기존 세력·지역·인물 자산: `reusable-candidates`

효력 정지·재검토:

- 표국 중심 대서사: `suspended-for-tonal-reassessment`
- 조선소 1화 시작: `candidate-only`
- B 장기 분산 호송: `deferred-candidate`
- 진아령 장기 라이벌: `reusable-rival-candidate`
- 분점 보증 최종 손실: `candidate-only`
- 기존 무료분·50장 Outline: `validation-reference / not-canon`

새 Gate:

- 작품 감각: `four-options / human-edit-pending`
- 결말: `reopened`
- 공동 주인공: `not-designed`
- 맥거핀·미스터리: `not-designed`
- 총화수·액트·서브액트: `locked-pending-foundation`
- 원고: `locked`

## 5. 작품 감각 후보

- T-A: 서유휘 단일 주인공 대하형
- T-B: **1+2 삼인 운명교차형 — PM 권고**
- T-C: 3인 동등 주인공형
- T-D: 팔인 군상 운명륜형

T-B 작업값:

- 서유휘 55~65%
- 공동 주인공 B 17~23%
- 공동 주인공 C 17~23%

표국은 서유휘의 삶과 능력으로 유지할 수 있지만 작품 전체 장르로 확정하지 않는다.

## 6. 작법·에이전트 원칙

전문 에이전트:

1. 결말 설계자
2. 맥거핀·미스터리 설계자
3. 운명 직조 설계자
4. 인물 비극·관계 설계자
5. 무협 액션 설계자
6. 한국 웹연재 설계자
7. 세계·용어 통합 설계자
8. 연속성 감사자
9. 반대감사자
10. PM 오케스트레이터

필수 작법:

- Ending First / Backward Design
- MacGuffin
- Braided Narrative
- Want / Need / Lie / Wound
- Promise / Progress / Payoff
- Try / Fail Cycles
- Scene / Sequel
- Battle as Argument
- Setup / Payoff Ledger
- 회차 절단 설계

작성 에이전트와 감사 에이전트를 분리한다.

## 7. 문서 위계

1. 최신 사용자 결정
2. `book_writing.md`
3. `operations/TONAL-DIRECTION-RESET-DECISION-v1.md`
4. `CLAUDE.md`
5. `operations/NARRATIVE-CRAFT-AGENT-ORCHESTRATION-v1.md`
6. `operations/META-PROMPTING-PROTOCOL-v1.md`
7. `operations/PM-PROGRESS-DASHBOARD.md`
8. 작품 감각·결말·공동 주인공·맥거핀 Human Edit 결정
9. 설정·인물 정본
10. 플롯·Outline 후보
11. 과거 참고안

## 8. 새 본선 순서

1. 작품 감각 Human Edit
2. 결말 4안과 승인
3. 1+2 공동 주인공 4안과 승인
4. 맥거핀·비밀 구조 4안과 승인
5. 세 주인공 Want/Need/Lie/Wound
6. 세 운명축 교차표
7. 전체 화수·액트·서브액트 4안
8. 무료분 진입점 4안
9. Plot Master
10. 무료분 1~25화
11. 웹소설 화 단위 Outline
12. 용어·전투·설명·회차 절단 통합
13. 연속성·FUN·작법 독립 감사
14. 사용자 집필 준비 승인
15. 그 뒤 원고

## 9. 원고 잠금

다음까지 원고는 작성하지 않는다.

- 작품 감각 승인
- 결말 승인
- 공동 주인공 승인
- 맥거핀 승인
- 액트·서브액트·화수 승인
- 무료분·Outline Gate 통과
- 최종 감사
- 사용자 집필 승인
