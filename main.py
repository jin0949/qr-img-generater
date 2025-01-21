from src.layout import ImageLayout


def main():
    url = "https://example.com"
    username = "테스트 사용자"

    try:
        image = ImageLayout.create_qr_image(url, username)

        save_path = "./result.png"
        image.save(save_path)

        image.show()

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
