# 광고 문구 서비스 앱

이 프로젝트는 OpenAI의 GPT-3.5 모델을 사용하여 제품에 대한 광고 문구를 생성하고, 생성된 문구를 MongoDB에 저장하며, Streamlit을 통해 사용자 인터페이스를 제공하는 웹 애플리케이션입니다.

## 주요 기능

1. 광고 문구 생성: 제품 이름, 주요 내용, 광고 문구의 느낌을 입력받아 AI 기반의 광고 문구를 생성합니다.
2. 데이터베이스 저장: 생성된 광고 문구를 MongoDB에 저장합니다.
3. 저장된 광고 조회: 이전에 생성된 광고 문구를 제품별로 조회할 수 있습니다.
4. 광고 삭제: 저장된 광고 문구를 삭제할 수 있습니다.

## 기술 스택

- Frontend: Streamlit
- Backend: FastAPI
- Database: MongoDB
- AI Model: OpenAI GPT-3.5

## 파일 구조

- `app.py`: Streamlit을 사용한 프론트엔드 애플리케이션
- `main.py`: FastAPI를 사용한 백엔드 서버

## 설치 및 실행 방법

1. 필요한 라이브러리 설치:
pip install streamlit pymongo requests fastapi openai
Copy
2. 환경 변수 설정:
- `MONGO_URL`: MongoDB 연결 URL
- `OPENAI_API_KEY`: OpenAI API 키

3. 백엔드 서버 실행:
uvicorn main:app --reload
Copy
4. 프론트엔드 애플리케이션 실행:
streamlit run app.py
Copy
## 사용 방법

1. 웹 브라우저에서 Streamlit 앱에 접속합니다.
2. 제품 이름, 주요 내용을 입력하고 광고 문구의 느낌을 선택합니다.
3. "광고 문구 생성하기" 버튼을 클릭하여 광고 문구를 생성합니다.
4. 생성된 광고 문구는 자동으로 MongoDB에 저장됩니다.
5. 사이드바에서 저장된 광고 문구를 제품별로 조회하고 삭제할 수 있습니다.

## 주의사항

- 이 애플리케이션은 OpenAI API를 사용하므로, API 사용량과 관련된 비용에 주의해야 합니다.
- MongoDB 연결 URL과 OpenAI API 키는 보안을 위해 환경 변수로 관리해야 합니다.
