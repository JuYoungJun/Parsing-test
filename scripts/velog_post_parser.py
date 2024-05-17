import os

# 벨로그 포스트 디렉토리 경로
posts_directory = "./velog-posts"

# README.md 파일 경로
readme_path = "./README.md"

# Velog Posts 섹션에 추가할 내용
new_post_links = []

# 상위 디렉토리 내의 파일 목록 가져오기
for file_name in os.listdir(posts_directory):
    # 파일 경로 생성
    file_path = os.path.join(posts_directory, file_name)
    
    # 파일이 디렉토리가 아니고, 파일 이름이 ".md"로 끝나는 경우에만 처리
    if os.path.isfile(file_path) and file_name.endswith(".md"):
        # 파일 이름을 README.md 파일에 추가하고 링크 생성
        post_title = file_name.replace(".md", "")
        post_link = f"- [{post_title}]({file_path})"  # 포스트 제목으로 링크 생성
        new_post_links.append(post_link)

# README.md 파일 열기
with open(readme_path, "r+") as readme_file:
    # 파일 내용 읽기
    content = readme_file.read()
    
    # Velog Posts 섹션의 시작과 끝 인덱스 찾기
    start_index = content.find("### Velog Posts")
    end_index = content.find("###", start_index + 1) if start_index != -1 else -1
    
    # Velog Posts 섹션이 있는지 확인
    if start_index != -1 and end_index != -1:
        # 섹션이 있으면 링크를 추가합니다.
        new_content = content[:end_index] + "\n".join(new_post_links) + content[end_index:]
    else:
        # 섹션이 없으면 섹션을 추가하고 링크를 추가합니다.
        new_content = content + "\n\n### Velog Posts\n\n" + "\n".join(new_post_links)
    
    # 파일 내용을 새로운 내용으로 덮어씁니다.
    readme_file.seek(0)
    readme_file.write(new_content)
    readme_file.truncate()
