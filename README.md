# Auth FastAPI

> HTTP API를 활용한 계정 기능 구현

FastAPI를 활용하여서 회원 기능을 구현한 점을 직접 사용합니다.<br>
3.10 버전에 개선된 타입 힌트 보다는 3.7 이상의 환경에서 사용할 수 있는 개발 될 수 있는 언어로 선 작성할 예정입니다.

- Python 버전 : 3.10
- Web Framework : FastAPI + uvicorn
- ORM : SQLAlchemy 1.4
- HTTP API

---

## 비즈니스 설계

회원 기능의 핵심

---

## DB 설계

회원 데이터에 있는 부분

### Account
<table>
  <th>Name</th>
  <th>type</th>
  <th>Relation</th>
  <th>etc</th>
  <tr>
    <td>id</td>
    <td>uuid</td>
    <td>pk</td>
    <td></td>
  </tr>
  
  <tr>
    <td>email</td>
    <td>varchar</td>
    <td>unique</td>
    <td>이메일</td>
  </tr>

  <tr>
    <td>password</td>
    <td>string</td>
    <td></td>
    <td>hash암호화된 비밀번호</td>
  </tr>

  <tr>
    <td>mobile</td>
    <td>number</td>
    <td>unique</td>
    <td>전화번호</td>
  </tr>

  <!-- <tr>
    <td></td>
    <td>number</td>
    <td></td>
    <td>전화번호</td>
  </tr> -->

  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td></td>
    <td>생성날짜</td>
  </tr>

  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td></td>
    <td>수정날짜</td>
  </tr>
</table>

### account_logs

