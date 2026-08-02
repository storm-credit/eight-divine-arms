# 《팔대신병록》 작문 엔진·문체 하네스 완료 보고

상태: `protocol-complete / automation-not-implemented / manuscript-locked`
작성일: `2026-08-02`

## 완료

- 현행 정본용 작문 엔진: `production/PROSE-WRITING-ENGINE-v1.md`
- 문체·작문 QA 하네스: `audit/PROSE-STYLE-QA-HARNESS-v1.md`
- 여성 인계표사·호송물 기반 구 집필법 강등: `operations/KOREAN-WEBNOVEL-WRITING-METHOD-v1.md`

## 작문 엔진 범위

- 서유휘 밀착 3인칭 제한 시점.
- 화 단위 입력·장면 배열·초고·장면 종료 절차.
- 인물별 대사 음성.
- 액션·수집·설명 엔진.
- 초고 후 8단계 개정 패스.
- AI식 균일 문장과 설계어 노출 금지.

## 하네스 범위

- 화별 100점 Gate.
- P0/P1/P2 판정.
- 사건·연독·주인공성·음성·액션·수집·문체·연속성 검사.
- AI 문체 냄새 탐지.
- 3화·10화 묶음 검사.
- 인물 음성 회귀 테스트.
- QA 출력 양식과 출고 기준.

## 중요 한계

현재 하네스는 Markdown 기반 검수 프로토콜이다. 원고 파일을 읽어 통계를 자동 산출하는 실행 코드나 CI는 아직 구현하지 않았다.

따라서 현재 판정은:

- 작문 엔진 규칙: COMPLETE.
- 문체 QA 하네스 규칙: COMPLETE.
- 자동 실행 스크립트: NOT IMPLEMENTED.
- 실제 원고 기준 캘리브레이션: 원고 개방 뒤 EP001~003으로 수행.

원고는 사용자 승인 전까지 잠근다.
