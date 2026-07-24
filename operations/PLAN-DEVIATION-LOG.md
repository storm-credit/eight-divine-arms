# 《팔대신병록》 계획 이탈·변경 로그

상태: `active-log`
규칙: `CLAUDE.md`

이 문서는 원래 계획과 실제 진행이 달라진 지점, 판단 오류, 도구·파일 문제, 범위 변경을 추적한다.

---

## DEV-20260725-01 — 설정집 완료 의미 혼동

| 항목 | 내용 |
|---|---|
| 발생 위치 | 설정집 완료 보고·S8~S12 상세화 제안 |
| 원래 계획 | 작품 설계를 지탱하는 핵심 설정을 완성한 뒤 인물·플롯으로 진행 |
| 실제 변화 | 구조적 설정 완료를 백과사전형 상세 설정집 완료로 과장 보고한 뒤, 반대로 도감식 상세화를 본선에 추가함 |
| 원인 | `운영 규칙 완성`과 `모든 고유명·사례 상세화`를 구분하지 못함 |
| 영향 | 사용자 혼란, 범위가 설정 백과사전 쪽으로 잠시 이탈 |
| 임시 조치 | S8~S12 백과사전형 확장을 본선에서 철회 |
| 영구 조치 | `PROJECT-DESIGN-SCOPE-LOCK-v1.md`와 `CLAUDE.md`에 상세화 판단 규칙 고정 |
| 상태 | resolved |
| 관련 파일 | `book_writing.md`, `operations/PROJECT-DESIGN-SCOPE-LOCK-v1.md`, `CLAUDE.md` |

---

## DEV-20260725-02 — 플롯 승인 없이 Outline Gate 개방

| 항목 | 내용 |
|---|---|
| 발생 위치 | Plot Human Edit → Outline Gate |
| 원래 계획 | 플롯 권고안을 사용자에게 명시 승인받고 정본 승격한 뒤 Outline 진행 |
| 실제 변화 | 사용자의 `이어서 진행`을 플롯 권고안 승인으로 과도하게 해석하고 50장 Outline까지 작성 |
| 원인 | 진행 지시와 고영향 설계 승인을 구분하지 못함 |
| 영향 | 승인되지 않은 결말·첫 사건·사망 기본값 위에 Outline이 올라감 |
| 임시 조치 | 플롯을 `human-edit-pending`, Outline을 `validation-draft`로 되돌림 |
| 영구 조치 | `이어서`, `계속`, `진행`을 C2~C3 승인으로 해석하지 않는 규칙을 `CLAUDE.md`에 추가 |
| 상태 | mitigated — 사용자 플롯 결정 필요 |
| 관련 파일 | `operations/PLOT-HUMAN-EDIT-PACKET-v2.md`, `audit/DESIGN-PACKAGE-REVIEW-v2.md`, `CLAUDE.md` |

---

## DEV-20260725-03 — Outline 48장·50장 기준 불일치

| 항목 | 내용 |
|---|---|
| 발생 위치 | Outline Gate 장 수·기능표 |
| 원래 계획 | 48장 균형형을 기준으로 막·구간·장 기능을 일관되게 작성 |
| 실제 변화 | 최종부 과밀을 보정하며 50장으로 늘렸으나 제1~3막 헤더와 후보 문서는 48장 기준이 남음 |
| 원인 | 장 수 변경 뒤 모든 산출물과 헤더를 동기화하지 않음 |
| 영향 | 장 배분·시점 비율·감사 근거 불일치 |
| 임시 조치 | 50장 작업안으로 기능 행렬 복구, Outline을 수정 초안으로 재분류 |
| 영구 조치 | 장 수·헤더·범위·링크 무결성 검사를 Gate 완료 조건에 추가 |
| 상태 | mitigated — 최종 장 수 재결정 필요 |
| 관련 파일 | `design/OUTLINE-SEGMENT-FUNCTION-MATRIX-v1.md`, `audit/DESIGN-PACKAGE-REVIEW-v2.md` |

---

## DEV-20260725-04 — 긴 GitHub 문서 저장·조회 절단

| 항목 | 내용 |
|---|---|
| 발생 위치 | 긴 Outline·감사 문서 작성과 조회 |
| 원래 계획 | 하나의 긴 문서로 전 막·전 장 기능을 저장 |
| 실제 변화 | 커넥터 응답 예산과 파일 업데이트 과정에서 중간 절단·부분 조회가 발생함 |
| 원인 | 긴 문서를 한 번에 작성·검증하려 한 도구 운용 문제 |
| 영향 | 구간 행렬 일부 누락, 감사가 실제 결손을 놓침 |
| 임시 조치 | 막·구간별 파일 분리, 부분 조회로 실제 끝부분 확인 |
| 영구 조치 | 긴 산출물은 150~250줄 단위로 분리하고, 생성 뒤 첫·중간·마지막 구간을 재조회 |
| 상태 | resolved for process / existing files still under review |
| 관련 파일 | `design/OUTLINE-CHAPTER-FUNCTIONS-ACT1-3-v1.md`, `design/OUTLINE-CHAPTER-FUNCTIONS-ACT4-5-v1.md`, `CLAUDE.md` |

---

## DEV-20260725-05 — 기존 감사의 자기확증

| 항목 | 내용 |
|---|---|
| 발생 위치 | Plot·Outline 교차감사 |
| 원래 계획 | 기존 설계의 맹점과 결손을 독립적으로 검증 |
| 실제 변화 | 작성된 설계의 의도를 재설명하는 방식으로 감사가 진행되어 파일 결손·반복 공식·무협 중심 약화를 놓침 |
| 원인 | 감사자가 설계자의 전제를 그대로 공유했고 반대 가설·프리모텀이 부족했음 |
| 영향 | `PROVISIONAL PASS`가 과도하게 선언됨 |
| 임시 조치 | 기존 Plot·Outline 통과 판정 철회, 전면 재검토 v2 작성 |
| 영구 조치 | Gate 전 `맹점 훑기`, `먼저 짚을 함정`, 네 시안 비교를 의무화 |
| 상태 | resolved for audit protocol |
| 관련 파일 | `audit/DESIGN-PACKAGE-REVIEW-v2.md`, `CLAUDE.md` |

---

# 새 항목 템플릿

## DEV-YYYYMMDD-NN — 제목

| 항목 | 내용 |
|---|---|
| 발생 위치 |  |
| 원래 계획 |  |
| 실제 변화 |  |
| 원인 |  |
| 영향 |  |
| 임시 조치 |  |
| 영구 조치 |  |
| 상태 | open / mitigated / resolved |
| 관련 커밋·파일 |  |
