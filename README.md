# QR Code Image Generator

<img src="https://github.com/user-attachments/assets/9b7a3c6a-5df3-4b68-8b83-c3baa9d3fa4d" width="500"> 

QR 코드와 텍스트를 결합하여 라벨 이미지를 생성하는 Python 모듈입니다. PIL(Python Imaging Library)을 사용하여 QR 코드 생성 및 이미지 처리를 수행합니다.

## 주요 구성 요소

- `ImageLayout`: QR 코드와 텍스트를 조합한 최종 이미지 생성
- `QRDrawer`: QR 코드 이미지 생성
- `TextDrawer`: 텍스트 이미지 생성

## 기능

- QR 코드 자동 생성
- 사용자 이름 텍스트 렌더링
- 이미지 저장 및 표시
- 커스텀 이미지 크기 설정

## 테스트 구성

- `test_create_qr_image`: QR 코드 이미지 생성 테스트
- `test_save_qr_image`: 이미지 저장 기능 테스트
- `test_draw_returns_image`: QR/텍스트 드로잉 테스트
- `test_save_image`: 파일 저장 테스트

## 사용 방법

```python
from src.layout import ImageLayout

# QR 코드 이미지 생성
image = ImageLayout.create_qr_image(url, username)

# 이미지 저장
image.save("output.png")
```

## 테스트 실행

```bash
pytest tests/
```

## 주의사항

- 이미지 저장 경로 존재 확인 필요
- 적절한 이미지 크기 설정 필요
- 한글 텍스트 렌더링 지원

Citations:
![test_print](https://github.com/user-attachments/assets/9b7a3c6a-5df3-4b68-8b83-c3baa9d3fa4d)

---
