# import os
# import requests
# from urllib.parse import quote_plus

# # GitHub Personal Access Token 가져오기
# GH_PAT = os.getenv('GH_PAT')

# # Velog 포스트 링크를 가져오는 함수
# def get_velog_post_links():
#     # velog-posts 디렉토리의 파일 목록 가져오기
#     api_url = "https://api.github.com/repos/JuYoungJun/Parsing-test/contents/velog-posts"
#     headers = {
#         "Authorization": f"token {GH_PAT}",
#         "Accept": "application/vnd.github.v3+json"
#     }
#     response = requests.get(api_url, headers=headers)
    
#     if response.status_code != 200:
#         print("GitHub API로 파일 목록을 가져오는 동안 오류가 발생했습니다.")
#         print(f"상태 코드: {response.status_code}")
#         print(f"응답 내용: {response.text}")
#         return []

#     data = response.json()
#     post_links = []

#     for item in data:
#         if item["type"] == "file" and item["name"].endswith(".md"):
#             file_name = item["name"]
#             post_title = file_name.replace(".md", "")
#             # '[', ']', '!', '?' 를 제거하고 URL 인코딩 적용
#             post_title_encoded = quote_plus(post_title.replace('[', '').replace(']', '').replace('?', '').replace('!', ''))
#             # Velog 포스트 링크 생성
#             post_link = f"https://velog.io/@jocker/{post_title_encoded}"
#             post_links.append((post_title, post_link))
    
#     return post_links

# # Velog Posts 섹션에 추가할 내용 가져오기
# new_post_links = get_velog_post_links()

# if not new_post_links:
#     print("새로운 Velog 포스트 링크를 가져오는 동안 오류가 발생했습니다.")
# else:
#     # README.md 파일 수정하기
#     readme_path = "./README.md"
#     with open(readme_path, "r+") as readme_file:
#         content = readme_file.read()
#         start_index = content.find("### Velog Posts")
#         if start_index != -1:
#             # 섹션 시작과 끝 위치를 찾기
#             end_index = content.find("###", start_index + 1)
#             if end_index == -1:
#                 end_index = len(content)
#             # 기존 Velog Posts 섹션 내용을 제거하고 새로운 섹션 내용 추가
#             new_content = content[:start_index + len("### Velog Posts\n\n")]
#             for post_title, post_link in new_post_links:
#                 new_content += f"- [{post_title}]({post_link})\n"
#             new_content += content[end_index:]
#         else:
#             # Velog Posts 섹션이 없으면 새로 생성
#             new_content = content + "\n\n### Velog Posts\n\n"
#             for post_title, post_link in new_post_links:
#                 new_content += f"- [{post_title}]({post_link})\n"
        
#         # 파일에 새 내용 쓰기
#         readme_file.seek(0)
#         readme_file.write(new_content)
#         readme_file.truncate()
        
#     print("README.md 파일이 성공적으로 수정되었습니다.")

import os
import requests
import re
import urllib.parse
from git import Repo, GitCommandError

# GitHub Personal Access Token 가져오기
GH_PAT = os.getenv('GH_PAT')

# Velog 포스트 링크를 가져오는 함수
def get_velog_post_links():
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
            
            # Velog 링크 생성 (제목을 변환하여 URL 형식으로)
            # post_title_formatted = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', post_title).strip().replace(' ', '-')
            post_title_formatted = re.sub(r'[^a-zA-Z0-9가-힣\s.-]', '', post_title).strip().replace(' ', '-')
            post_link = f"https://velog.io/@jocker/{urllib.parse.quote(post_title_formatted)}"
            post_links.append((post_title, post_link))
    
    return post_links

# Velog Posts 섹션에 추가할 내용 가져오기
new_post_links = get_velog_post_links()

if not new_post_links:
    print("새로운 Velog 포스트 링크를 가져오는 동안 오류가 발생했습니다.")
else:
    readme_path = "./README.md"
    try:
        with open(readme_path, "r+", encoding="utf-8") as readme_file:
            content = readme_file.read()
            # "### Velog Posts" 섹션 찾기
            start_index = content.find("### Velog Posts")
            if start_index == -1:
                # Velog Posts 섹션이 없으면 추가
                new_content = "\n\n### Velog Posts\n\n"
            else:
                # Velog Posts 섹션이 이미 존재하면 추가할 내용만 준비
                new_content = ""

            # 기존 Velog Posts 링크를 저장할 집합
            existing_links = set()
            if start_index != -1:
                # 기존 Velog Posts 섹션 내용 가져오기
                end_index = content.find("###", start_index + 1)
                if end_index == -1:
                    end_index = len(content)
                existing_post_links = content[start_index + len("### Velog Posts\n\n"):end_index]
                existing_lines = existing_post_links.strip().splitlines()
                existing_links = {line.split('](')[1][:-1] for line in existing_lines if line}  # URL만 추출하여 집합으로 변환

            # 중복된 링크를 추가하지 않도록 새로운 링크 처리
            for post_title, post_link in new_post_links:
                if post_link not in existing_links:
                    new_content += f"- [{post_title}]({post_link})\n"
                    existing_links.add(post_link)  # 추가한 링크를 집합에 저장

            # 새로운 내용이 추가된 경우
            if new_content:
                if start_index != -1:
                    # 섹션이 존재하면 해당 부분을 수정
                    updated_content = (
                        content[:start_index + len("### Velog Posts\n\n")] +
                        new_content +
                        content[end_index:]
                    )
                else:
                    # Velog Posts 섹션이 없으면 새로 생성
                    updated_content = content + new_content

                # 파일에 새 내용 쓰기
                readme_file.seek(0)
                readme_file.write(updated_content)
                readme_file.truncate()

            print("README.md 파일이 성공적으로 수정되었습니다.")

            # Git 저장소 관리
            repo = Repo('.')
            try:
                repo.git.pull()  # 원격 저장소의 변경 사항을 가져오기
            except GitCommandError as e:
                print(f"Git pull 중 오류 발생: {e}")

            # 변경 사항을 추가하고 푸시하기
            try:
                repo.git.add(readme_path)
                repo.git.commit('-m', "Update README.md with new Velog posts")
                repo.git.push()  # 변경 사항 푸시
                print("변경 사항이 성공적으로 푸시되었습니다.")
            except GitCommandError as e:
                print(f"Git push 중 오류 발생: {e}")

    except FileNotFoundError:
        print("README.md 파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")
    except Exception as e:
        print(f"파일 수정 중 오류가 발생했습니다: {e}")
