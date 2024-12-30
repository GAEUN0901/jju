from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter

# GPT-2 모델의 토크나이저를 불러옵니다.
hf_tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# 입력 파일 경로
input_file_path = "C:/Users/PC/Desktop/실무인재(겨율특강)/실무인재참고파일 - 복사본.txt"

# 파일을 읽어옵니다.
with open(input_file_path, encoding="utf-8") as f:
    file_content = f.read()

# 파일의 처음 350자를 출력합니다.
print(file_content[:350])

# RecursiveCharacterTextSplitter를 사용하여 텍스트를 분할합니다.
chunk_size = 300  # 청크 크기
chunk_overlap = 50  # 청크 간의 중복 크기

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
)

# 텍스트를 분할합니다.
split_texts = text_splitter.split_text(file_content)

# 각 청크를 포맷에 맞게 출력합니다.
for i, chunk in enumerate(split_texts, 1):
    lines = chunk.splitlines()
    title = lines[0] if lines else "Untitled"
    definition = next((line for line in lines[1:] if line.startswith("정의:")), "")
    example = next((line for line in lines[1:] if line.startswith("예시:")), "")
    keywords = next((line for line in lines[1:] if line.startswith("연관키워드:")), "")

    print(f"{i} {title}\n")  # 청크 번호와 제목 출력
    print(f"{definition}\n")  # 정의 출력
    print(f"{example}\n")  # 예시 출력
    print(f"{keywords}\n")  # 연관키워드 출력
    print("=" * 80 + "\n")
