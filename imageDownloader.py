import pandas as pd
import urllib.request as req
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError

# ssl 보안 해제 (신뢰하는 사이트에서만 사용)
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# 다운로드 폴더 경로
download_dir = 'download/'

# 엑셀 파일 경로
excel_file_path = 'exam.xlsx'

# 엑셀 파일에서 URL 추출
df = pd.read_excel(excel_file_path)

# 열 이름
urls = df['COLUMN NAME']


def download_images(url):
    """
    이미지 다운로드 함수

    Args:
        url (String): 다운로드 url
    """
    download_path = download_dir + urlparse(url).path.split("/")[-1]

    try:
        req.urlretrieve(url, download_path)
        print(f"{url} download complete")
    except HTTPError as e:
        print(f"HTTP Error: {e}")
    except URLError as e:
        print(f"URL Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# 각 URL에 대해 이미지 다운로드 실행
print("=========== Download Start =========== ")
for url in urls:
    download_images(url)
print("=========== Download End =========== ")
