<h1 id="github-기초-git-기본-명령어와-워크플로우">GitHub 기초: Git 기본 명령어와 워크플로우</h1>
<p>이 글에서는 Git의 기본 명령어와 워크플로우에 대해 다루어 보겠습니다. Git은 분산 버전 관리 시스템으로, 프로젝트의 히스토리를 관리하고 협업을 효율적으로 할 수 있게 도와줍니다. GitHub을 효과적으로 사용하기 위해서는 Git의 기본적인 사용법을 이해하는 것이 중요합니다.</p>
<h2 id="목차">목차</h2>
<ol>
<li><a href="https://api.velog.io/rss/@jocker#git%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90">Git의 기본 개념</a></li>
<li><a href="https://api.velog.io/rss/@jocker#git-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4">Git 기본 명령어</a></li>
<li><a href="https://api.velog.io/rss/@jocker#git-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C%EC%9A%B0">Git 워크플로우</a></li>
<li><a href="https://api.velog.io/rss/@jocker#%EA%B3%A0%EA%B8%89-git-%EA%B8%B0%EB%8A%A5">고급 Git 기능</a></li>
<li><a href="https://api.velog.io/rss/@jocker#%EC%8B%A4%EC%A0%84-git-%EC%82%AC%EC%9A%A9-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4">실전 Git 사용 시나리오</a></li>
<li><a href="https://api.velog.io/rss/@jocker#git-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%AA%A8%EC%9D%8C">Git 명령어 모음</a></li>
</ol>
<h2 id="git의-기본-개념">Git의 기본 개념</h2>
<p>Git은 파일의 변경 사항을 기록하고, 특정 시점으로 돌아갈 수 있게 해주는 도구입니다. Git의 주요 개념은 다음과 같습니다 :</p>
<ul>
<li><strong>저장소(Repository)</strong> : 프로젝트의 파일과 변경 이력을 저장하는 공간입니다.</li>
<li><strong>커밋(Commit)</strong> : 파일 변경 사항을 하나의 단위로 기록하는 행위입니다.</li>
<li><strong>브랜치(Branch)</strong> : 독립적으로 작업할 수 있게 해주는 작업 공간입니다. 기본 브랜치는<code>main</code> 또는 <code>master</code> 입니다.</li>
<li><strong>머지(Merge)</strong> : 두 개의 브랜치를 하나로 합치는 작업입니다.</li>
<li><strong>원격 저장소(Remote Repository)</strong> : 인터넷이나 네트워크 어딘가에 있는 저장소입니다. GitHub이 대표적인 예입니다.</li>
<li><strong>푸시(Push)</strong> : 로컬 저장소의 변경사항을 원격 저장소에 업로드하는 것입니다.</li>
<li><strong>풀(Pull)</strong> : 원격 저장소의 변경사항을 로컬 저장소로 가져오는 것입니다.</li>
</ul>
<h2 id="git-기본-며령어">Git 기본 며령어</h2>
<p>Git을 사용하기 위해서는 다양한 명령어를 사용할 수 있어야 합니다. 아래는 기본적인 Git 명령어 들 입니다.</p>
<h3 id="저장소-초기화-및-클론">저장소 초기화 및 클론</h3>
<pre><code class="language-sh"># 로컬 디렉토리를 Git 저장소로 초기화
git init

# 원격 저장소를 로컬로 복제
git clone &lt;저장소_URL&gt;</code></pre>
<h3 id="파일-추가-및-커밋">파일 추가 및 커밋</h3>
<pre><code class="language-sh"># 특정 파일을 스테이징 영역에 추가
git add &lt;파일이름&gt;

# 모든 변경 사항을 스테이징 영역에 추가
git add .

# 스테이징된 변경사항을 커밋
git commit -m &quot;커밋 메시지&quot;

# 파일을 스테이징하고 바로 커밋
git commit -am &quot;커밋 메시지&quot;</code></pre>
<h3 id="상태-및-로그-확인">상태 및 로그 확인</h3>
<pre><code class="language-sh"># 저장소의 현재 상태 확인
git status

# 커밋 히스토리 확인
git log

# 간단한 로그 확인 (한 줄에 한 커밋씩)
git log --oneline

# 브랜치 그래프와 함께 로그 확인
git log --graph --online --all</code></pre>
<h3 id="브랜치-관리">브랜치 관리</h3>
<pre><code class="language-sh"># 새 브랜치 생성
git branch &lt;브랜치이름&gt;

# 브랜치 목록 확인
git branch

# 다른 브랜치로 전환
git checkout &lt;브랜치이름&gt;

# 브랜치 생성 및 전화을 동시에
git checkout -b &lt;브랜치이름&gt;

# 브랜치 병합
git merge &lt;브랜치이름&gt;

# 브랜치 삭제
git brach -d &lt;브랜치이름&gt;</code></pre>
<h3 id="원격-저장소-관리">원격 저장소 관리</h3>
<pre><code class="language-sh"># 원격 저장소 추가
git remote add &lt;원격저장소이름&gt; &lt;저장소_URL&gt;

# 원격 저장소 목록 확인
git remote -v

# 원격 저장소에 변경사항 푸시
git push &lt;원격저장소이름&gt; &lt;브랜치이름&gt;

# 원격 저장소의 변경사항 가져오기
git pull &lt;원격저장소이름&gt; &lt;브랜치이름&gt;</code></pre>
<h2 id="git-워크플로우">Git 워크플로우</h2>
<p>Git을 사용한 기본적인 작업 흐름은 다음과 같습니다 :</p>
<p>1.<strong>저장소 초기화 또는 클론</strong> : 새로운 프로젝트를 시작할때 <code>git init</code>을 사용하거나, 기존 프로젝트를 복제할 때 <code>git clone</code>을 사용합니다.
2.<strong>브랜치 생성</strong> : 새로운 기능 개발이나 버그 수정을 위해 새 브랜치를 만듭니다.
3.<strong>파일 수정</strong> : 프로젝트 파일을 수정합니다.
4.<strong>변경사항 스테이징</strong> : 수정한 파일을 스테이징 영역에 추가합니다. (<code>git add</code>)
5.<strong>커밋</strong> : 스테이징된 변경사항을 커밋합니다. (<code>git commit</code>)
6.<strong>푸시</strong> : 로컬의 변경사항을 원격 저장소에 업로드합니다. (<code>git push</code>)
7.<strong>풀 리퀘스트</strong> : GitHub에서 변경사항을 메인 브랜치에 병합하기 위해 풀 리퀘스트를 생성합니다.
8.<strong>리뷰 및 병합</strong> : 코드 리뷰 후 변경사항을 메인 브랜치에 병합합니다.
9.<strong>동기화</strong> : 로컬 저장소를 최신 상태로 유지하기 위해 변경사항을 가져옵니다. (<code>git pull</code>)</p>
<h2 id="고급-git-기능">고급 Git 기능</h2>
<p>Git에는 더 복잡한 시나리오를 처리할 수 있는 고급 기능들이 있습니다. 여기에는 몇 가지 예시가 있습니다 :</p>
<h3 id="리베이스-rebase">리베이스 (Rebase)</h3>
<p>리베이스는 브랜치의 기준점을 다른 브랜치의 최신 커밋으로 옮기는 작업입니다. 이는 히스토리를 더 깔금하게 만들어줍니다.</p>
<pre><code class="language-sh">git checkout feature-branch
git rebase main</code></pre>
<h3 id="대화형-리베이스-interactive-rebase">대화형 리베이스 (Interactive Rebase)</h3>
<p>여러 커밋을 수정, 병합, 삭제하는 등 커밋 히스토리를 재구성할 수 있습니다.</p>
<pre><code class="language-sh">git rebase -i HEAD~3</code></pre>
<h3 id="스태시-stash">스태시 (Stash)</h3>
<p>작업 중인 변경사항을 임시로 저장하고 나중에 다시 적용할 수 있습니다.</p>
<pre><code class="language-sh">git stash
git stash pop</code></pre>
<h3 id="체리픽-cherry-pick">체리픽 (Cherry-pick)</h3>
<p>다른 브랜치의 특정 커밋만 현재 브랜치에 적용합니다.</p>
<pre><code class="language-sh">git cherry-pick &lt;커밋해시&gt;</code></pre>
<h3 id="실전-git-사용-시나리오">실전 Git 사용 시나리오</h3>
<p>실제 프로젝트에서 Git을 어떻게 사용하는지 살펴 보겠습니다.</p>
<h3 id="시나리오-1--새로운-기능-개발">시나리오 1 : 새로운 기능 개발</h3>
<pre><code class="language-sh"># 최신 main 브랜치로 이동
git checkout main
git pull origin main

# 새 기능 브랜치 생성
git checkout -b feature/new-login-page

# 작업 후 변경사항 커밋
git add .
git commit -m &quot;Add new login page design&quot;

# 원격 저장소에 푸시
git push origin feature/new-login-page

# GitHub에서 풀 리퀘스트 생성</code></pre>
<h3 id="시나리오-2--긴급-버그-수정">시나리오 2 : 긴급 버그 수정</h3>
<pre><code class="language-sh"># 현재 작업 임시 저장
git stash

# main 브랜치에서 핫픽스 브랜치 생성
git checkout main
git checkout -n hotfix/login-crash

# 버그 수정 후 커밋
git commit -am &quot;Fix login crash issue&quot;

# main에 병합 후 태그 생성
git checkout main
git merge hotfix/login-crash
git tag -a v1.0.1 -m &quot;Hotfix : login crash&quot;

# 원격 저장소에 변경사항 푸시
git push origin main --tags

# 원래 작업으로 복귀
git checkout feature/new-login-page
git stash pop</code></pre>
<h2 id="git-명령어-모음">Git 명령어 모음</h2>
<details>
Git 명령어 모음 (클릭하여 펼치기)

<h3 id="기본-명령어">기본 명령어</h3>
<pre><code class="language-sh">git init                    # 새 Git 저장소 초기화
git clone &lt;url&gt;             # 원격 저장소 복제
git add &lt;file&gt;              # 파일을 스테이징 영역에 추가
git commit -m &quot;message&quot;     # 변경사항 커밋
git status                  # 작업 디렉토리 상태 확인
git diff                    # 변경사항 비교
git log                     # 커밋 히스토리 조회</code></pre>
<h3 id="브랜치-관련">브랜치 관련</h3>
<pre><code class="language-sh">git branch                  # 브랜치 목록 조회
git branch &lt;name&gt;           # 새 브랜치 생성
git checkout &lt;branch&gt;       # 브랜치 전환
git merge &lt;branch&gt;          # 현재 브랜치에 다른 브랜치 병합
git branch -d &lt;branch&gt;      # 브랜치 삭제</code></pre>
<h3 id="원격-저장소-관련">원격 저장소 관련</h3>
<pre><code class="language-sh">git remote add &lt;name&gt; &lt;url&gt; # 원격 저장소 추가
git fetch &lt;remote&gt;          # 원격 저장소에서 정보 가져오기
git pull &lt;remote&gt; &lt;branch&gt;  # 원격 저장소에서 변경사항 가져와 병합
git push &lt;remote&gt; &lt;branch&gt;  # 원격 저장소에 변경사항 푸시</code></pre>
<h3 id="고급-기능">고급 기능</h3>
<pre><code class="language-sh">git rebase &lt;branch&gt;         # 현재 브랜치를 다른 브랜치 위로 재배치
git rebase -i HEAD~&lt;n&gt;      # 대화형 리베이스
git stash                   # 변경사항 임시 저장
git stash pop               # 임시 저장한 변경사항 적용
git cherry-pick &lt;commit&gt;    # 특정 커밋 선택하여 현재 브랜치에 적용</code></pre>
<h3 id="되돌리기-관련">되돌리기 관련</h3>
<pre><code class="language-sh">git reset &lt;file&gt;            # 스테이징 취소
git reset --soft HEAD^      # 최근 커밋 취소 (변경사항 유지)
git reset --hard HEAD^      # 최근 커밋 취소 (변경사항 삭제)
git revert &lt;commit&gt;         # 특정 커밋 되돌리기</code></pre>
</details>


<h2 id="결론">결론</h2>
<p>Git은 매우 유용한 도구로, 이르 효과적으로 사용하기 위해서는 기본 명령어와 워크플로우를 잘 이해해야 합니다. 이글을 통해 Git의 기본 사용법부터 고급 기능까지 익히셨기를 바랍니다. Git과 GitHub을 활용하면 프로젝트 관리와 협업이 훨씬 수월해집니다.</p>
<p>이 시리즈의 다음 그에서는 Git 과 GitHub을 실제 개발 환경에서 어떻게 활용하는지 살펴보겠습니다.
Android Studio, Eclipse, Spring Toll Suite(STS)와 같은 IDE들과 GitHub을 연동하는 방법, 그리고 GitHub의 고급 기능들을 알아볼 예정입니다.</p>
<h2 id="다음-시리즈-미리보기">다음 시리즈 미리보기</h2>
<ul>
<li><strong>3. Android Studio와 GitHub 연동</strong> : Android 개발자를 위한 Git 활용법</li>
<li><strong>4. Eclipse와 GitHub 연동</strong> : Java 개발자를 위한 Git 워크 플로우</li>
<li><strong>5. STS1(Spring Tool Suite 4)와 GitHub 연동</strong> : Spring 개발자를 위한 Git 사용법</li>
<li><strong>6. 고급 GitHub 기능</strong> : 이슈 트래킹, 프로젝트 관리, GitHub Actions 소개</li>
<li><strong>7. GitHub Pages를 이용한 정적 사이트 배포</strong> : 개인 또는 프로젝트 페이지 만들기</li>
</ul>
<p>이 시리즈를 통해 GitHub의 기본부터 고급 기술까지 단계별로 배울 수 있습니다. 다음 그에서 만나요!</p>