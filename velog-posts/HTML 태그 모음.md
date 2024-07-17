<h1 id="html-태그-속성attribute">HTML 태그 속성(Attribute)</h1>
<p>HTML 태그는 다양한 속성을 포함하여 더 많은 기능을 제공할 수 있습니다. 각 속성은 태그에 추가 정보를 제공하거나 동작을 조정하는 데 사용됩니다.</p>
<h2 id="주요-html-태그-속성">주요 HTML 태그 속성</h2>
<h3 id="공통-속성common-attributes">공통 속성(Common Attributes)</h3>
<ul>
<li><code>id</code>: 요소의 고유 식별자를 정의합니다.</li>
<li><code>class</code>: 요소에 대한 CSS 클래스를 지정합니다.</li>
<li><code>style</code>: 요소에 직접 CSS 스타일 규칙을 적용합니다.</li>
<li><code>title</code>: 요소의 추가 정보(툴팁 등)를 지정합니다.</li>
<li><code>data-*</code>: 사용자 정의 데이터 속성을 정의하고, JavaScript에서 접근할 수 있습니다.</li>
</ul>
<h3 id="링크-관련-속성">링크 관련 속성</h3>
<p>HTML 링크(<code>&lt;a&gt;</code>) 요소에서 사용되는 주요 속성들을 자세히 설명하고, 추가 속성들을 소개합니다.</p>
<ul>
<li><code>href</code>: 링크가 이동할 URL을 지정합니다.</li>
<li><code>target</code>: 링크가 열리는 위치를 지정합니다 (<code>_blank</code>, <code>_self</code>, <code>_parent</code>, <code>_top</code> 등).</li>
<li><code>rel</code>: 링크와 대상 사이의 관계를 지정합니다 (<code>nofollow</code>, <code>noopener</code>, <code>noreferrer</code> 등).</li>
</ul>
<h4 id="href-속성"><code>href</code> 속성</h4>
<p><code>href</code> 속성은 링크의 목적지를 정의합니다. 이 속성은 반드시 필요하며, 유효한 URL을 지정해야 합니다.</p>
<h4 id="target-속성"><code>target</code> 속성</h4>
<p><code>target</code> 속성은 링크가 어떻게 열리는지를 지정합니다. 주로 웹 페이지에서 새 창에서 링크를 열거나 같은 창에서 열지를 결정하는 데 사용됩니다. 일반적으로 사용되는 값으로는 <code>_blank</code> (새 창에서 열기), <code>_self</code> (현재 창에서 열기), <code>_parent</code> (상위 창에서 열기), <code>_top</code> (최상위 창에서 열기) 등이 있습니다.</p>
<h4 id="rel-속성"><code>rel</code> 속성</h4>
<p><code>rel</code> 속성은 링크와 링크 대상 사이의 관계를 정의합니다. 예를 들어, <code>nofollow</code>는 검색 엔진이 링크를 따라가지 않도록 지시하고, <code>noopener</code> 및 <code>noreferrer</code>는 보안 관련 정책을 적용하여 보안 문제를 예방합니다.</p>
<h3 id="이미지-관련-속성">이미지 관련 속성</h3>
<p>HTML 이미지(<code>&lt;img&gt;</code>) 요소에서 사용되는 주요 속성들을 자세히 설명하고, 추가 속성들을 소개합니다.</p>
<ul>
<li><code>src</code>: 이미지 파일의 경로를 지정합니다.</li>
<li><code>alt</code>: 이미지에 대한 대체 텍스트를 지정합니다.</li>
<li><code>width</code>, <code>height</code>: 이미지의 너비와 높이를 지정합니다.</li>
<li><code>loading</code>: 이미지 로딩 방식을 지정합니다 (<code>lazy</code>, <code>eager</code> 등).</li>
</ul>
<h4 id="src-속성"><code>src</code> 속성</h4>
<p><code>src</code> 속성은 웹 페이지에 표시할 이미지 파일의 경로를 지정합니다. 이 속성은 필수적이며, 유효한 이미지 파일 경로를 지정해야 합니다.</p>
<h4 id="alt-속성"><code>alt</code> 속성</h4>
<p><code>alt</code> 속성은 이미지의 대체 텍스트를 지정합니다. 이미지를 표시할 수 없는 경우나 스크린 리더 사용자에게 이미지를 설명해 주는 중요한 역할을 합니다.</p>
<h4 id="width-height-속성"><code>width</code>, <code>height</code> 속성</h4>
<p><code>width</code>와 <code>height</code> 속성은 이미지의 크기를 지정합니다. 이 속성들을 사용하여 이미지를 원하는 크기로 조절할 수 있습니다.</p>
<h4 id="loading-속성"><code>loading</code> 속성</h4>
<p><code>loading</code> 속성은 이미지의 로딩 방식을 지정합니다. <code>lazy</code> 값은 페이지가 로드될 때 이미지를 로드하지 않고, 스크롤되거나 사용자 조작에 따라 필요할 때 로드하는 것을 의미합니다. <code>eager</code> 값은 페이지가 로드될 때 즉시 이미지를 로드합니다.</p>
<h3 id="폼-관련-속성">폼 관련 속성</h3>
<p>HTML 폼 요소에서 사용되는 주요 속성들을 자세히 설명하고, 추가 속성들을 소개합니다.</p>
<ul>
<li><code>action</code>: 폼 데이터를 전송할 서버 쪽 스크립트의 URL을 지정합니다.</li>
<li><code>method</code>: 폼 데이터 전송 방식을 지정합니다 (<code>GET</code>, <code>POST</code> 등).</li>
<li><code>name</code>: 폼 요소의 이름을 지정합니다.</li>
<li><code>value</code>: 폼 요소의 초기 값을 지정합니다.</li>
<li><code>placeholder</code>: 입력 필드에 임시 텍스트를 표시합니다.</li>
</ul>
<h4 id="action-속성"><code>action</code> 속성</h4>
<p><code>action</code> 속성은 폼 데이터가 전송될 서버 쪽 스크립트의 URL을 지정합니다. 폼 데이터는 이 URL로 전송되어 처리됩니다.</p>
<h4 id="method-속성"><code>method</code> 속성</h4>
<p><code>method</code> 속성은 폼 데이터의 전송 방식을 지정합니다. 가장 일반적으로 사용되는 값으로는 <code>GET</code>과 <code>POST</code>가 있습니다. <code>GET</code>은 URL 매개변수로 데이터를 전송하고, <code>POST</code>는 HTTP 본문을 통해 데이터를 전송합니다.</p>
<h4 id="name-속성"><code>name</code> 속성</h4>
<p><code>name</code> 속성은 폼 요소의 이름을 지정합니다. 서버 쪽 스크립트에서 이 이름을 사용하여 데이터를 식별하거나 처리할 수 있습니다.</p>
<h4 id="value-속성"><code>value</code> 속성</h4>
<p><code>value</code> 속성은 폼 요소의 초기 값을 지정합니다. 사용자가 폼을 제출하기 전에 미리 설정된 값이 입력됩니다.</p>
<h4 id="placeholder-속성"><code>placeholder</code> 속성</h4>
<p><code>placeholder</code> 속성은 입력 필드에 표시할 임시 텍스트를 지정합니다. 이 속성은 사용자에게 입력 방식을 안내하는 데 유용합니다.</p>
<h3 id="텍스트-입력-관련-속성">텍스트 입력 관련 속성</h3>
<p>HTML 텍스트 입력 요소에서 사용되는 주요 속성들을 자세히 설명합니다.</p>
<ul>
<li><code>maxlength</code>: 입력 가능한 최대 문자 수를 지정합니다.</li>
<li><code>readonly</code>: 읽기 전용 입력 필드를 지정합니다.</li>
<li><code>disabled</code>: 비활성화된 입력 필드를 지정합니다.</li>
</ul>
<h4 id="maxlength-속성"><code>maxlength</code> 속성</h4>
<p><code>maxlength</code> 속성은 입력 필드에 입력할 수 있는 최대 문자 수를 제한합니다. 이 속성을 사용하여 사용자가 입력할 수 있는 글자 수를 제한할 수 있습니다.</p>
<h4 id="readonly-속성"><code>readonly</code> 속성</h4>
<p><code>readonly</code> 속성은 입력 필드를 읽기 전용으로 설정합니다. 사용자는 이 속성이 지정된 입력 필드의 값을 변경할 수 없습니다.</p>
<h4 id="disabled-속성"><code>disabled</code> 속성</h4>
<p><code>disabled</code> 속성은 입력 필드를 비활성화 상태로 만듭니다. 비활성화된 입력 필드는 사용자가 상호 작용할 수 없으며, 폼 데이터가 전송되지 않습니다.</p>
<h3 id="목록-관련-속성">목록 관련 속성</h3>
<p>HTML 목록 요소에서 사용되는 주요 속성들을 설명합니다.</p>
<ul>
<li><code>type</code>: 순서 없는 목록(<code>&lt;ul&gt;</code>)의 마커 유형을 지정합니다 (<code>disc</code>, <code>circle</code>, <code>square</code>).</li>
<li><code>start</code>: 순서 있는 목록(<code>&lt;ol&gt;</code>)의 시작 값(숫자)을 지정합니다.</li>
</ul>
<h4 id="type-속성"><code>type</code> 속성</h4>
<p><code>type</code> 속성은 순서 없는 목록(<code>&lt;ul&gt;</code>)의 마커 유형을 지정합니다. 각 마커 유형은 <code>disc</code> (원), <code>circle</code> (원), <code>square</code> (사각형) 등으로 지정할 수 있습니다.</p>
<h4 id="start-속성"><code>start</code> 속성</h4>
<p><code>start</code> 속성은 순서 있는 목록(<code>&lt;ol&gt;</code>)의 시작 값(숫자)을 지정합니다. 이 속성을 사용하여 목록의 시작 번호를 설정할 수 있습니다.</p>
<h3 id="테이블-관련-속성">테이블 관련 속성</h3>
<p>HTML 테이블에서 사용되는 주요 속성들을 자세히 설명하고 추가 속성들을 소개합니다.</p>
<ul>
<li><p><code>colspan</code>, <code>rowspan</code>: <code>colspan</code>은 한 셀에 병합할 열의 수를, <code>rowspan</code>은 한 셀에 병합할 행의 수를 지정합니다. 이 속성들을 사용하여 셀을 병합하여 복잡한 테이블 구조를 만들 수 있습니다.</p>
</li>
<li><p><code>headers</code>: 이 속성은 <code>&lt;th&gt;</code> 요소의 제목과 연결된 <code>&lt;td&gt;</code> 요소의 ID를 지정합니다. 테이블의 각 데이터 셀에 대해 헤더 셀과의 관계를 정의하여 스크린 리더 사용자가 테이블을 더 잘 이해할 수 있도록 합니다.</p>
</li>
<li><p><code>border</code>: 테이블의 테두리 두께를 지정합니다. 숫자가 클수록 테두리가 더 두껍게 표시됩니다. 예를 들어, <code>border=&quot;1&quot;</code>은 테이블 주위에 얇은 선을 그리고, <code>border=&quot;2&quot;</code>는 두꺼운 선을 그립니다.</p>
</li>
<li><p><code>bordercolor</code>: 테이블 테두리의 색상을 지정합니다. 이 속성을 사용하여 테이블의 테두리 색상을 원하는 색으로 설정할 수 있습니다. 색상은 CSS 색상 표기법을 따릅니다.</p>
</li>
</ul>
<h3 id="추가-테이블-속성">추가 테이블 속성</h3>
<ul>
<li><p><code>align</code>: 테이블의 내용을 수평으로 정렬하는 방법을 지정합니다. 값으로는 <code>left</code>, <code>center</code>, <code>right</code>를 사용할 수 있습니다.</p>
</li>
<li><p><code>bgcolor</code>: 테이블의 배경 색상을 지정합니다. 이 속성을 사용하여 테이블의 배경을 원하는 색으로 채울 수 있습니다.</p>
</li>
<li><p><code>cellpadding</code>, <code>cellspacing</code>: <code>cellpadding</code>은 셀의 내부 여백을 설정하고, <code>cellspacing</code>은 셀 사이의 간격을 설정합니다. 둘 다 테이블의 모양과 느낌을 조정하는 데 사용됩니다.</p>
</li>
<li><p><code>width</code>: 테이블의 너비를 지정합니다. 픽셀(px), 백분율(%) 등의 단위로 너비를 설정할 수 있습니다. 예를 들어, <code>width=&quot;100%&quot;</code>는 테이블을 부모 요소의 전체 너비에 맞게 확장합니다.</p>
</li>
<li><p><code>summary</code>: 테이블의 요약 정보를 제공합니다. 스크린 리더 사용자에게 테이블의 목적과 구조를 이해하는 데 도움이 됩니다.</p>
</li>
<li><p><code>scope</code>: <code>&lt;th&gt;</code> 요소에서 사용되며, 헤더 셀의 범위를 지정합니다. 가능한 값으로는 <code>row</code>, <code>col</code>, <code>rowgroup</code>, <code>colgroup</code>이 있습니다.</p>
</li>
</ul>
<h3 id="멀티미디어-관련-속성">멀티미디어 관련 속성</h3>
<p>HTML에서 사용되는 멀티미디어 요소에서 사용되는 주요 속성들을 자세히 설명하고, 추가 속성들을 소개합니다.</p>
<ul>
<li><code>autoplay</code>: 미디어가 자동으로 재생될지 여부를 지정합니다.</li>
<li><code>controls</code>: 미디어 컨트롤 (재생, 일시 정지 등)을 표시할지 여부를 지정합니다.</li>
<li><code>loop</code>: 미디어가 끝나면 자동으로 반복 재생할지 여부를 지정합니다.</li>
</ul>
<h4 id="autoplay-속성"><code>autoplay</code> 속성</h4>
<p><code>autoplay</code> 속성은 미디어가 자동으로 재생될지 여부를 지정합니다. 이 속성이 있으면 페이지가 로드될 때 자동으로 미디어가 재생됩니다.</p>
<h4 id="controls-속성"><code>controls</code> 속성</h4>
<p><code>controls</code> 속성은 미디어 컨트롤을 표시할지 여부를 지정합니다. 이 속성이 있으면 미디어 플레이어에 재생, 일시 정지, 볼륨 조절 등의 컨트롤이 표시됩니다.</p>
<h4 id="loop-속성"><code>loop</code> 속성</h4>
<p><code>loop</code> 속성은 미디어가 재생이 끝나면 자동으로 반복 재생할지 여부를 지정합니다. 이 속성이 있으면 미디어가 끝나면 다시 처음부터 재생됩니다.</p>
<h3 id="기타-속성">기타 속성</h3>
<p>HTML 요소에서 사용되는 기타 주요 속성들을 설명합니다.</p>
<ul>
<li><code>aria-*</code>: 접근성을 개선하고 스크린 리더 사용자에게 정보를 제공하는 데 사용되는 속성입니다.</li>
<li><code>tabindex</code>: 요소의 탭 순서를 지정합니다.</li>
<li><code>role</code>: 요소의 역할을 지정합니다 (<code>button</code>, <code>navigation</code>, <code>tabpanel</code> 등).</li>
</ul>
<h4 id="aria--속성"><code>aria-*</code> 속성</h4>
<p><code>aria-*</code> 속성은 접근성을 향상시키기 위해 추가된 속성으로, 스크린 리더 사용자에게 요소의 상태, 의미 등을 전달합니다. 예를 들어, <code>aria-label</code>, <code>aria-labelledby</code>, <code>aria-describedby</code> 등이 있습니다.</p>
<h4 id="tabindex-속성"><code>tabindex</code> 속성</h4>
<p><code>tabindex</code> 속성은 요소의 탭 순서를 지정합니다. 이 속성을 사용하여 포커스가 이동할 순서를 정할 수 있습니다.</p>
<h4 id="role-속성"><code>role</code> 속성</h4>
<p><code>role</code> 속성은 요소의 역할을 지정합니다. 예를 들어, 버튼 역할을 갖는 요소인 경우 <code>role=&quot;button&quot;</code>을 설정하여 스크린 리더가 이 요소를 버튼으로 인식하게 할 수 있습니다.</p>
<h2 id="마무리">마무리</h2>
<p>위 속성들은 HTML 요소의 다양한 기능을 활용하는 데 도움이 됩니다. 각 속성은 해당하는 태그에서 적절하게 사용되어 웹 페이지의 기능과 사용자 경험을 개선할 수 있습니다.</p>