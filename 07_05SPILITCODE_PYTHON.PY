from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

def read_python_file(file_path):
    """Python 파일을 읽어 텍스트로 반환합니다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def initialize_python_splitter(chunk_size=60, chunk_overlap=0):
    """Python 텍스트 분할기를 초기화합니다."""
    return RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

def split_python_code(python_code, splitter):
    """Python 코드를 분할하여 문서 리스트를 반환합니다."""
    return splitter.create_documents([python_code])

def display_documents(documents):
    """분할된 문서를 출력합니다."""
    for idx, doc in enumerate(documents, start=1):
        print(f"Document {idx}:")
        print(doc.page_content)
        print("-" * 50)

if __name__ == "__main__":
    # 파일 경로
    file_path = r'C:\Users\PC\Desktop\실무인재(겨율특강)\html_jju.txt'

    # Python 파일 읽기
    python_code = read_python_file(file_path)

    # 텍스트 분할기 초기화
    python_splitter = initialize_python_splitter(chunk_size=60, chunk_overlap=0)

    # Python 코드 분할
    python_docs = split_python_code(python_code, python_splitter)

    # 결과 출력
    display_documents(python_docs)
