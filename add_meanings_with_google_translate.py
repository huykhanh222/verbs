import json
from googletrans import Translator

def add_meanings_with_google_translate(input_file, output_file, source_lang="en", target_lang="vi"):
    """
    Thêm nghĩa tiếng Việt vào danh sách động từ bằng Google Translate.

    Args:
        input_file (str): Đường dẫn đến tệp JSON đầu vào (verbs.json).
        output_file (str): Đường dẫn lưu tệp JSON đầu ra.
        source_lang (str): Ngôn ngữ gốc của các động từ (mặc định là 'en').
        target_lang (str): Ngôn ngữ đích để dịch nghĩa (mặc định là 'vi').
    """
    translator = Translator()

    # Đọc dữ liệu từ tệp JSON
    with open(input_file, "r", encoding="utf-8") as file:
        verbs_list = json.load(file)

    # Thêm nghĩa cho từng động từ
    verbs_with_meanings = []
    for verb_forms in verbs_list:
        base_form = verb_forms[0]  # Chỉ dịch nghĩa của dạng nguyên thể (base form)
        try:
            translated = translator.translate(base_form, src=source_lang, dest=target_lang).text
        except Exception as e:
            translated = f"Không thể dịch: {e}"
        verbs_with_meanings.append({"forms": verb_forms, "meaning": translated})

    # Lưu kết quả vào tệp JSON mới
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(verbs_with_meanings, file, ensure_ascii=False, indent=4)
    print(f"Đã lưu kết quả vào {output_file}")

# Sử dụng script
if __name__ == "__main__":
    input_file_path = "verbs.json"  # Tên file đầu vào chứa danh sách động từ
    output_file_path = "verbs_with_meanings.json"  # File đầu ra chứa kết quả
    add_meanings_with_google_translate(input_file_path, output_file_path)
