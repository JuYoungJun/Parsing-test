import os

# 벨로그 포스트 디렉토리 경로
posts_directory = "./velog-posts"

# README.md 파일 경로
readme_path = "README.md"

# README.md 파일 열기
with open(readme_path, "a") as readme_file:
    readme_file.write("\n\n### Velog Posts\n\n")  # 벨로그 포스트 섹션 시작
    
    # "velog-posts" 디렉토리 내의 파일 목록 가져오기
    for file_name in os.listdir(posts_directory):
        # 파일 경로 생성
        file_path = os.path.join(posts_directory, file_name)
        
        # 파일이 디렉토리가 아니고, 파일 이름이 ".md"로 끝나는 경우에만 처리
        if os.path.isfile(file_path) and file_name.endswith(".md"):
            # 파일 이름을 README.md 파일에 추가
            readme_file.write(f"- {file_name}\n")
