import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@jocker'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# Git 사용자 정보 설정
repo.git.config('--global', 'user.name', 'JuYoungJun')
repo.git.config('--global', 'user.email', 'kaks162@gmail.com')

# 변경사항 커밋 및 푸시
repo.git.add(A=True)
repo.git.commit('-m', 'Update Velog posts')
repo.remotes.origin.push(refspec='HEAD:main')

# GitHub 액세스 토큰을 사용하여 푸시
access_token = os.getenv('GH_PAT')  # 환경 변수로부터 액세스 토큰을 가져옴
repo.remotes.origin.push('main', set_upstream=True, access_token=access_token)
