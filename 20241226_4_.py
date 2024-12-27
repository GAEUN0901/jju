import os

os.environ['OPENAI_API_KEY'] = "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"
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# template 정의. {country}는 변수로, 이후에 값이 들어갈 자리를 의미
template = "{country}의 수도는 어디인가요?"

# from_template 메소드를 이용하여 Prompt Template 객체 생성
prompt = PromptTemplate.from_template(template)

# Prompt Template 출력
print(prompt)

# Prompt Template에 변수 값 채워넣기
prompt_filled = prompt.format(country="대한민국")
print(prompt_filled)

# ChatOpenAI 모델 생성
model = ChatOpenAI(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0.1
)

# 체인 생성 및 실행
chain = prompt | model
response = chain.invoke({"country": "대한민국"})
print(response.content)





import os

os.environ['OPENAI_API_KEY'] = "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"
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 프롬프트 템플릿 정의 (국가를 위한 플레이스홀더 포함)
template = "{country}의 수도는 어디인가요?"

# PromptTemplate 인스턴스 생성
prompt = PromptTemplate(
    template=template,
    input_variables=["country"]
)

# Prompt Template 출력
print(prompt)

# Prompt Template에 변수 값 채워넣기
prompt_filled = prompt.format(country="대한민국")
print(prompt_filled)

# 새로운 템플릿 정의 (두 개의 국가 포함)
template = "{country1}과 {country2}의 수도는 어디인가요?"
prompt = PromptTemplate(
    template=template,
    input_variables=["country1"],
    partial_variables={
        "country2": "미국"
    }
)

# Prompt Template 출력
print(prompt)

# Prompt Template에 첫 번째 변수 값 채워넣기
prompt_filled = prompt.format(country1="대한민국")
print(prompt_filled)

# Partial 적용 (두 번째 변수를 캐나다로 설정)
prompt_partial = prompt.partial(country2="캐나다")
print(prompt_partial)
