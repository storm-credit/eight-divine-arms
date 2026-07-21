# 《팔대신병록》 집필·설계 최상위 정책

상태: `provisional-canon / setting-bible-human-edit`
역할: 저장소 최상위 운영 정책
총괄: PM 오케스트레이터

이 문서는 《팔대신병록》 프로젝트의 모든 설계·검증·집필 작업보다 우선한다.

## 1. 기본 원칙

- 본문 집필보다 설정집과 인물·플롯 설계를 먼저 완료한다.
- 설정 아이디어는 자유롭게 발산하되 정본과 분리한다.
- 중요한 설정은 단일 초안으로 확정하지 않는다.
- 역사·연표·거리·가격·소유권·인물 관계를 장부로 검증한다.
- 정본은 사용자 승인 없이 `canon`으로 승격하지 않는다.
- 이전 결정과 충돌하는 새 아이디어는 자동 덮어쓰지 않고 재검토 대상으로 등록한다.
- 현재는 설정집 Human Edit 단계이며 원고·장면·대사 작업은 잠근다.

## 2. 공식 작업 파이프라인

`Draft → Validate → Human Edit → Finalize`

### Draft

- 브레인스토밍과 구조 설계
- 복수 후보 생성
- 상태: `brainstorm` 또는 `draft`

### Validate

- 역사·지리·무협·경제·미스터리·감정 검증
- 악마의 변호인과 정합성 감사
- 상태: `review`

### Human Edit

- 사용자가 방향·정서·선호 판단
- PM이 이견·위험·권고안 요약
- 수정·승인을 결정 로그에 반영
- 상태: `provisional-canon`

### Finalize

- 용어·연표·관계·문서 링크 최종 정리
- 장부 동기화
- 사용자 승인
- 상태: `canon`

## 3. 문서 위계

1. 최신 사용자 결정
2. `book_writing.md`
3. `operations/SETTING-BIBLE-ONLY-SCOPE.md`
4. `design/SETTING-BIBLE-v2.0-MASTER.md`
5. `operations/HUMAN-EDIT-REVIEW-PACKET-v1.md`
6. `lore_index.md`
7. 최신 완료·Gate 결정 문서
8. S1~S7 `provisional-canon` 모듈
9. `audit/` 장부와 교차감사
10. `원고_index.md`
11. 과거 플롯·장면·브레인스토밍 참고안

과거 `SETTING-BIBLE-v1.0`, Gate 3~5 인물·플롯, 시놉시스·60장 개요·장면 카드는 정본 기준이 아니다.

## 4. 정본 사용 규칙

후속 설정 설계는 다음만 전제로 사용한다.

- `canon`
- PM이 작업 기준으로 승인한 `provisional-canon`
- 최신 사용자 결정

후속 인물·플롯 설계는 통합 설정집 `canon` 승격 뒤 별도 Gate에서 시작한다.

후보·브레인스토밍·기존 플롯 문서는 아이디어와 검증 자료로만 사용한다.

## 5. 설정집 단계

완료된 묶음:

- S1 세계 운영 현실
- S2 강호 제도·조직 운영
- S3 무공·병장기·의술
- S4 기환·종교·생태
- S5 권역·외부 무림
- S6 기록·명성·용어·가격·권리 장부
- S7 팔대신병 개별 설정집
- 설정집 v2.0 통합
- 최종 전문가 완전성 감사

현재:

- 설정 구조·운영 규칙: 완료
- 상태: `provisional-canon / human-edit-ready`
- 상위 설정 누락: 0
- 치명적 충돌: 0

## 6. Human Edit 대상

- 기환 체감 강도
- 익숙한 문파·세가와 고유 기능 세력의 비중
- 팔대신병 명명 방식
- 쇄조도 원사건의 공개·은폐 정도
- 역사 고증과 장르 가독성의 균형

역사/장르 균형은 사용자 결정으로 다음처럼 처리한다.

- 역사적 골격과 사건 인과는 엄격하게
- 진원표국·검표수·표사 등 장르 통칭은 가독성을 우선

세부 권고안은 `operations/HUMAN-EDIT-REVIEW-PACKET-v1.md`를 따른다.

## 7. 집필·플롯 잠금

설정집 `canon` 승격 전 금지:

- 새 초고
- 새 장면 카드
- 60장 개요 상세화
- 대사·문체·연출
- 특정 주인공·동료·적대자의 정본화
- 기존 6부 플롯의 자동 채택

기존 자료 상태:

- 시놉시스: `deferred-reference`
- 6부 개요: `deferred-reference`
- 60장 개요: `premature-detail / deferred-reference`
- 장면 카드: `premature-detail / deferred-reference`
- 실제 초고: 삭제·중단

## 8. 설정집 정본 이후 Gate

설정집 승인 뒤에도 바로 원고로 가지 않는다.

1. 인물·관계 설계 범위 동결
2. 주인공 구조 최소 3안 비교
3. 사용할 권역·세력·신병 선택
4. 인물 바이블 교차감사와 Human Edit
5. 결말·대서사 후보 재설계
6. 플롯 Human Edit
7. 장면·원고 진행 승인

기존 심소연·사문경·6부 구조는 후보 중 하나로만 재평가한다.

## 9. 변경 관리

정본 변경 시 기록한다.

- 변경 전·후
- 변경 이유
- 영향 D분야·S모듈
- 장부 갱신
- 재검토 조건

변경 등급:

- C0 표기·링크
- C1 고유명·지역 속칭
- C2 세력·신병·기환 규칙
- C3 작품 헌법·역사 구조

중요한 변경은 `retcon`으로 표시한다.

## 10. 품질 기준

- 설정은 사건과 인물의 선택으로 드러나야 한다.
- 클리셰는 장르 언어로 활용하되 변형한다.
- 반전은 기존 사실의 재해석을 우선한다.
- 전투는 목표·지형·상성·비용·결과를 가진다.
- 세력은 수입·물류·정보·지역 기반을 가진다.
- 초자연은 규칙·조건·대가가 있다.
- 여운을 위해 비극과 대량 사망에 의존하지 않는다.
- 신병은 새 능력으로 편하게 위기를 해결하지 않는다.
- 익숙한 명문과 작품 고유 기능 세력의 역할을 구분한다.
- 세계 설정을 한 장면에서 설명하지 않는다.

## 11. 현재 최우선 기준

1. `design/SETTING-BIBLE-v2.0-MASTER.md`
2. `operations/HUMAN-EDIT-REVIEW-PACKET-v1.md`
3. `audit/FINAL-SETTING-BIBLE-COMPLETENESS-AUDIT-v3.md`
4. `operations/CANON-PROMOTION-CHECKLIST-v1.md`
5. `operations/PM-PROGRESS-DASHBOARD.md`
6. `lore_index.md`

## 12. 현재 실행 상태

- 설정집: `structural-complete / human-edit-ready`
- 원고: 잠금
- 다음 작업: Human Edit 승인 또는 수정
- 승인 뒤: 설정집 `canon` 승격과 인물 설계 Gate 개방