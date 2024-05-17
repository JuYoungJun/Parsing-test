import os
import requests
from urllib.parse import quote

# GitHub Personal Access Token 가져오기
GH_PAT = os.getenv('GH_PAT')

# Velog 포스트 링크를 가져오는 함수
def get_velog_post_links():
    # velog-posts 디렉토리의 파일 목록 가져오기
    api_url = "https://api.github.com/repos/JuYoungJun/Parsing-test/contents/velog-posts"
    headers = {
        "Authorization": f"token {GH_PAT}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(api_url, headers=headers)
    
    if response.status_code != 200:
        print("GitHub API로 파일 목록을 가져오는 동안 오류가 발생했습니다.")
        print(f"상태 코드: {response.status_code}")
        print(f"응답 내용: {response.text}")
        return []

    data = response.json()
    post_links = []

    for item in data:
        if item["type"] == "file" and item["name"].endswith(".md"):
            file_name = item["name"]
            post_title = file_name.replace(".md", "")
            # Velog 포스트 링크 생성
            post_link = f"https://velog.io/@jocker/{quote(post_title)}"
            post_links.append(f"- [{post_title}]({post_link})\n")
    
    return post_links

# Velog Posts 섹션에 추가할 내용 가져오기
new_post_links = get_velog_post_links()

if not new_post_links:
    print("새로운 Velog 포스트 링크를 가져오는 동안 오류가 발생했습니다.")
else:
    # README.md 파일 수정하기
    readme_path = "./README.md"
    with open(readme_path, "r+") as readme_file:
        content = readme_file.read()
        start_index = content.find("### Velog Posts")
        end_index = content.find("###", start_index + 1) if start_index != -1 else -1
        
        if start_index != -1 and end_index != -1:
            updated_content = content[:end_index] + "\n".join(new_post_links) + content[end_index:]
        else:
            updated_content = content + "\n\n### Velog Posts\n\n" + "\n".join(new_post_links)
            
        readme_file.seek(0)
        readme_file.write(updated_content)
        readme_file.truncate()
        
    print("README.md 파일이 성공적으로 수정되었습니다.")
