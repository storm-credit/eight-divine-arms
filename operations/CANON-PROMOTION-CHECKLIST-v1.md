# 《팔대신병록》 설정집 정본 승격 체크리스트 v1

상태: `active-checklist / awaiting-user-approval`
총괄: PM 오케스트레이터

## 1. 정본 승격 대상

최상위:
- `design/SETTING-BIBLE-v2.0-MASTER.md`

결정·감사:
- `operations/HUMAN-EDIT-REVIEW-PACKET-v1.md`
- `operations/SETTING-BIBLE-v2-COMPLETION-DECISION.md`
- `audit/FINAL-SETTING-BIBLE-COMPLETENESS-AUDIT-v3.md`

지원 모듈:
- S1~S7의 `provisional-canon` 문서
- 가격·권리·수리·지역·세력 장부

## 2. 승격 전 필수 확인

- [x] D01~D27 상위 설정 분야 점검
- [x] S1 세계 운영 교차감사
- [x] S2 조직·강호 교차감사
- [x] S3 무공·병기·의술 교차감사
- [x] S4 기환·종교·생태 교차감사
- [x] S5 권역·외부 무림 교차감사
- [x] S6 기록·명성·용어·장부 교차감사
- [x] S7 팔대신병 개별 교차감사
- [x] 최종 전문가 완전성 감사
- [x] 플롯·장면 참고안의 정본 분리
- [x] 사용자 용어 결정 반영
- [ ] Human Edit 취향 결정 승인
- [ ] 통합 설정집 상태 `canon` 변경
- [ ] 핵심 모듈 상태 동기화
- [ ] 허브·대시보드 정본 상태 갱신

## 3. Human Edit 승인 대상

PM 권고안:

1. 저강도 확정형 기환
2. 익숙한 명문 35~45%, 고유 기능 세력 55~65%
3. 팔대신병 현재 작업명 유지 + 지역 이형명·원기록명
4. 쇄조도를 반쯤 알려진 재난으로 운용
5. 역사 골격 엄격 + 장르 통칭 가독성 우선

5번은 사용자 결정으로 이미 해결됐다.

## 4. 승격 시 변경할 상태

### 최상위

- `SETTING-BIBLE-v2.0-MASTER.md`
  - `provisional-canon / human-edit-ready`
  - → `canon / setting-bible-master`

### 운영

- PM 대시보드
  - → `setting-bible-canon / character-design-locked-until-new-gate`

- 설정 허브
  - → 최상위 정본 문서와 후속 단계 분리

### 모듈

모든 문서를 기계적으로 `canon`으로 바꾸지 않는다.

- 상위 규칙·교차감사 핵심 모듈: `canon`
- 숫자·고유명·지역 변동이 큰 장부: `canon-framework`
- 실제 관직·일자 사용 전 감사가 필요한 분야: `canon-with-local-verification`
- 플롯·장면 참고안: 계속 `deferred-reference`

## 5. 정본 이후 변경 관리

변경 등급:

- C0: 표기·오탈자·링크 — 즉시 수정
- C1: 개별 고유명·지역 속칭 — 관련 카드만 수정
- C2: 세력·신병·기환 규칙 변경 — 관련 S묶음 재감사
- C3: 작품 헌법·기환 강도·역사 구조 변경 — 사용자 승인 후 상위 정본 재개방

## 6. 정본 이후 다음 Gate

설정집 승격 직후 원고로 가지 않는다.

다음 별도 Gate:

1. 인물·관계 설계 범위 동결
2. 기존 심소연·동료·적대자 참고안 재평가
3. 최소 3개 주인공 구조 비교
4. 사용 권역·핵심 세력·중심 신병 선택
5. 인물 바이블 Human Edit
6. 그 뒤 사건·플롯 설계

## 7. 원고 잠금

다음까지 원고 잠금 유지:

- 설정집 `canon` 승격
- 인물 설계 Gate 통과
- 플롯 설계 Gate 통과
- 사용자 원고 진행 승인

## 8. 승인 기록 형식

사용자 승인 뒤 별도 결정 문서를 만든다.

예:

- 승인 범위
- 수정된 Human Edit 항목
- 영향을 받은 모듈
- 재감사 결과
- 정본 승격 커밋
- 다음 Gate 시작 조건