import os
import requests

# GitHub Personal Access Token 가져오기
GH_PAT = os.getenv('GH_PAT')

# Velog Posts 디렉토리 URL 설정
velog_posts_url = "https://github.com/JuYoungJun/Parsing-test/tree/main/velog-posts"

# GitHub API 엔드포인트 및 헤더 설정
api_url = "https://api.github.com/repos/JuYoungJun/Parsing-test/contents/velog-posts"
headers = {
    "Authorization": f"token {GH_PAT}",
    "Accept": "application/vnd.github.v3+json"
}

# velog-posts 디렉토리의 파일 목록 가져오기
response = requests.get(api_url, headers=headers)
if response.status_code == 200:
    data = response.json()
    new_content = "\n"

    # 각 파일의 제목 가져오기
    for item in data:
        if item["type"] == "file" and item["name"].endswith(".md"):
            file_name = item["name"]
            post_title = file_name.replace(".md", "")
            post_link = f"- [{post_title}]({velog_posts_url}/{file_name})\n"  # 포스트 제목으로 링크 생성
            new_content += post_link

    # README.md 파일 수정하기
    readme_path = "./README.md"
    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        start_index = content.find("### Velog Posts")
        end_index = content.find("###", start_index + 1) if start_index != -1 else -1
        
        if start_index != -1 and end_index != -1:
            updated_content = content[:end_index] + new_content + content[end_index:]
        else:
            updated_content = content + "\n\n### Velog Posts\n\n" + new_content
            
        readme_file.seek(0)
        readme_file.write(updated_content)
        readme_file.truncate()
        
    print("README.md 파일이 성공적으로 수정되었습니다.")
else:
    print("GitHub API로 파일 목록을 가져오는 동안 오류가 발생했습니다.")
    print(f"상태 코드: {response.status_code}")
    print(f"응답 내용: {response.text}")
