import os
import requests
from urllib.parse import quote_plus

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
            # '['와 ']'를 제거하고 URL 인코딩 적용
            post_title_encoded = quote_plus(post_title.replace('[', '').replace(']', ''))
            # Velog 포스트 링크 생성
            post_link = f"https://velog.io/@jocker/{post_title_encoded}"
            post_links.append((post_title, post_link))
    
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
            # 기존 Velog Posts 섹션 내용을 찾아서 대체
            new_content = content[:start_index + len("### Velog Posts\n\n")]
            existing_links = content[start_index:end_index]

            for post_title, post_link in new_post_links:
                if post_title in existing_links:
                    # 이미 README.md에 해당 포스트가 있으면 덮어쓰기
                    existing_links = existing_links.replace(
                        f"- [{post_title}]",
                        f"- [{post_title}]({post_link})"
                    )
                else:
                    # README.md에 해당 포스트가 없으면 추가
                    new_content += f"- [{post_title}]({post_link})\n"

            new_content += content[end_index:]
            updated_content = new_content
        else:
            # Velog Posts 섹션이 없으면 새로 생성
            updated_content = content + "\n\n### Velog Posts\n\n"
            for post_title, post_link in new_post_links:
                updated_content += f"- [{post_title}]({post_link})\n"
            
        readme_file.seek(0)
        readme_file.write(updated_content)
        readme_file.truncate()
        
    print("README.md 파일이 성공적으로 수정되었습니다.")
