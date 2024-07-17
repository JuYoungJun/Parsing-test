<h1 id="jdk-java-development-kit-설치-가이드">JDK (Java Development Kit) 설치 가이드</h1>
<h2 id="1-jdk란">1. JDK란?</h2>
<p>JDK는 Java 프로그래밍을 위한 필수 도구 모음입니다. Java 어플리케이션 개발에 필요한 Java 가상 머신(JVM), 컴파일러, 디버거 등 모든 도구를 제공합니다.</p>
<h2 id="2-java-virtual-machine-jvm">2. Java Virtual Machine (JVM)</h2>
<p>Java Virtual Machine (JVM)은 Java 프로그램을 실행하는 데 중요한 가상 머신입니다. JVM은 하드웨어와 운영 체제와 독립적으로 Java 코드를 실행할 수 있는 가상화된 환경을 제공합니다.</p>
<h3 id="jvm의-주요-기능">JVM의 주요 기능:</h3>
<ul>
<li><strong>바이트코드 해석</strong>: JVM은 Java 컴파일러에 의해 생성된 바이트코드를 해석하고 실행합니다.</li>
<li><strong>메모리 관리</strong>: JVM 내부의 자동 메모리 관리 기능은 개발자가 메모리를 직접 관리할 필요 없도록 합니다.</li>
<li><strong>가비지 컬렉션</strong>: 사용되지 않는 메모리 자원을 정리하여 시스템 성능을 최적화합니다.</li>
<li><strong>보안</strong>: 다양한 보안 기능을 제공하여 Java 애플리케이션의 안전한 실행을 보장합니다.</li>
<li><strong>클래스 로딩</strong>: 실행 시 필요한 클래스 파일을 동적으로 로드하여 필요한 클래스를 사용할 수 있게 합니다.</li>
</ul>
<p>JVM은 Java의 크로스 플랫폼 호환성을 제공하며 코드 실행 환경을 표준화하는 중요한 역할을 합니다. 이로 인해 &quot;한 번 작성하고 어디서든 실행&quot;이 가능한 Java의 유명한 특성을 실현합니다.</p>
<p>JVM의 구조, 장점, 동작 방식에 대해 더 깊이 탐구하기 위해 <a href="https://api.velog.io/rss/@jocker">다가오는 블로그 포스트</a>를 기대해 주세요.</p>
<h2 id="3-jdk-11-설치하기">3. JDK 11 설치하기</h2>
<h3 id="단계별-설치-절차">단계별 설치 절차:</h3>
<h3 id="1-oracle-사이트-접속">1. Oracle 사이트 접속</h3>
<ul>
<li>먼저 <a href="https://www.oracle.com/java/technologies/javase-jdk11-downloads.html">Oracle JDK 다운로드 페이지</a>에 접속합니다.</li>
</ul>
<h3 id="2-jdk-11-다운로드">2. JDK 11 다운로드</h3>
<ul>
<li>해당 페이지에서 운영 체제에 맞는 JDK 11 설치 파일을 다운로드합니다.<ul>
<li><strong>Windows</strong>: <code>.exe</code> 파일을 선택하여 다운로드합니다.</li>
<li><strong>macOS</strong>: <code>.dmg</code> 파일을 선택하여 다운로드합니다.</li>
<li><strong>Linux</strong>: <code>.tar.gz</code> 파일을 선택하여 다운로드합니다.</li>
</ul>
</li>
</ul>
<h3 id="3-설치-파일-실행">3. 설치 파일 실행</h3>
<ul>
<li>다운로드가 완료되면 설치 파일을 실행합니다.<ul>
<li><strong>Windows</strong>: 다운로드한 <code>.exe</code> 파일을 더블 클릭하여 실행합니다. 설치 마법사가 시작됩니다.</li>
<li><strong>macOS</strong>: 다운로드한 <code>.dmg</code> 파일을 더블 클릭하여 마운트하고, 마운트된 디스크 이미지에서 설치 파일을 실행합니다.</li>
<li><strong>Linux</strong>: 다운로드한 <code>.tar.gz</code> 파일을 압축 해제한 후, 터미널을 열고 압축 해제된 디렉터리에서 설치 스크립트를 실행합니다.</li>
</ul>
</li>
</ul>
<h3 id="4-설치-과정-진행">4. 설치 과정 진행</h3>
<ul>
<li>설치 마법사의 지시에 따라 JDK 11을 설치합니다.<ul>
<li><strong>경로 설정</strong>: JDK를 설치할 경로를 지정합니다. 보통 기본 경로를 사용할 수 있지만 필요에 따라 사용자 정의 경로로 변경할 수 있습니다.</li>
</ul>
</li>
</ul>
<h3 id="5-환경-변수-설정-선택-사항">5. 환경 변수 설정 (선택 사항)</h3>
<ul>
<li>시스템 환경 변수를 설정하여 JDK를 사용할 수 있도록 합니다.<ul>
<li><strong>Windows</strong>: 제어판 &gt; 시스템 및 보안 &gt; 시스템 &gt; 고급 시스템 설정 &gt; 환경 변수에서 PATH에 JDK 설치 경로를 추가합니다.</li>
<li><strong>macOS</strong>: 터미널에서 <code>~/.bash_profile</code> 또는 <code>~/.zshrc</code> 파일을 열고 <code>export PATH=&quot;/path/to/jdk/bin:$PATH&quot;</code>와 같이 추가합니다.</li>
<li><strong>Linux</strong>: 터미널에서 <code>~/.bashrc</code> 또는 <code>~/.zshrc</code> 파일을 열고 <code>export PATH=&quot;/path/to/jdk/bin:$PATH&quot;</code>와 같이 추가합니다.</li>
</ul>
</li>
</ul>
<h2 id="환경-변수-설정의-필요성과-장점">환경 변수 설정의 필요성과 장점:</h2>
<ul>
<li><strong>환경 변수 설정 필요성</strong>: JDK를 설치할 때 JDK 설치 경로를 환경 변수에 등록하여 터미널이나 명령 프롬프트에서 <code>java</code> 및 <code>javac</code>와 같은 명령어를 쉽게 사용할 수 있습니다.</li>
<li><strong>장점</strong>:<ul>
<li><strong>편의성</strong>: 환경 변수를 설정하여 JDK 개발 도구를 매번 경로를 입력하지 않고 사용할 수 있습니다.</li>
<li><strong>유연성</strong>: 여러 JDK 버전을 사용할 때 각 경로를 설정하여 쉽게 전환할 수 있습니다.</li>
<li><strong>자동화</strong>: 개발 환경을 자동으로 설정하는 스크립트에서 JDK를 포함한 개발 도구를 설정하는 데 환경 변수를 사용할 수 있습니다.</li>
</ul>
</li>
</ul>
<p>JDK 11 설치가 완료되었습니다! 이제 Java 어플리케이션을 개발할 수 있는 Java 개발 환경을 구축할 준비가 되었습니다.</p>
<p>위 설치 가이드를 통해 JDK 11을 성공적으로 설치하고 환경 변수를 설정하는 방법에 대해 자세히 설명하였습니다. 필요시 추가적인 설명이나 스크린샷을 포함하여 직관적인 안내를 제공할 수 있습니다.</p>