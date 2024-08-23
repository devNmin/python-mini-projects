# My Docs 프로젝트 📚

이 프로젝트는 **MkDocs**를 사용하여 정적 사이트를 생성하고, Vercel을 통해 배포합니다. MkDocs는 간단한 문서 사이트를 빠르게 만들 수 있는 도구입니다.

## 설치 방법

### 1. 레포지토리 클론
먼저 레포지토리를 클론합니다:
```bash
git clone https://github.com/devNmin/python-mini-projects.git
cd python-mini-projects/mkdocs-vercel
```
### 2. MkDocs 설치

먼저 MkDocs를 설치해야 합니다. 다음 명령어를 터미널에서 실행하세요:

```bash
pip install mkdocs
```
### 3. 로컬 서버 실행
로컬에서 MkDocs를 실행해 사이트를 미리보기 할 수 있습니다. 다음 명령어를 사용하세요:
```bash
mkdocs serve
```
이 명령어를 실행하면 로컬 서버가 시작되고, 웹 브라우저에서 http://127.0.0.1:8000/ 주소로 접속할 수 있습니다.

## 필수 파일
이 프로젝트를 정상적으로 실행하고 배포하기 위해서는 다음 파일들이 필요합니다:

- vercel.json: Vercel 배포 설정 파일입니다. Vercel에서 이 프로젝트를 자동으로 인식하고 배포할 수 있도록 도와줍니다.

- requirements.txt: 프로젝트에서 사용하는 파이썬 패키지를 명시하는 파일입니다. MkDocs와 같은 의존성을 설치할 때 사용됩니다.

이 두 파일이 프로젝트 루트에 반드시 존재해야 하며, 특히 Vercel을 통해 배포하려면 vercel.json 파일이 필수적입니다.



## 배포

이 프로젝트는 Vercel을 사용하여 배포됩니다. 커밋하면 Vercel이 자동으로 배포를 처리합니다.

1. **GitHub에 레포지토리 생성**  
   먼저 GitHub에 프로젝트용 레포지토리를 생성합니다.

2. **Vercel 홈페이지에서 Import**  
   Vercel 홈페이지에 가서 'Import Project' 버튼을 클릭하고 GitHub 계정을 연결하여 생성한 레포지토리를 선택합니다.

3. **자동 배포 설정**  
   Vercel은 GitHub 레포지토리와 연동되어, 레포지토리에 푸시될 때마다 자동으로 배포를 수행합니다. 따라서, 코드를 푸시할 때마다 Vercel이 자동으로 최신 버전을 배포합니다.

## 폴더 구조
- docs/ - 문서가 저장되는 폴더
- mkdocs.yml - MkDocs 설정 파일
- vercel.json - Vercel 배포 설정 파일
- requirements.txt - Python 의존성 파일