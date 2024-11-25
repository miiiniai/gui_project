from transformers import AutoModel, AutoTokenizer

# 토크나이저를 로드합니다.
tokenizer = AutoTokenizer.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True)

# 모델을 로드하고 설정합니다.
model = AutoModel.from_pretrained('ucaslcl/GOT-OCR2_0', trust_remote_code=True, low_cpu_mem_usage=True, device_map='cpu', use_safetensors=True, pad_token_id=tokenizer.eos_token_id)

# 테스트할 이미지 파일 경로를 설정합니다.
image_file = './gui_ocr/image.png'

# 일반 텍스트 OCR을 수행합니다.
res = model.chat(tokenizer, image_file, ocr_type='ocr')

# 포맷된 텍스트 OCR을 수행하는 코드 (주석 처리).
# res = model.chat(tokenizer, image_file, ocr_type='format')

# 세분화된 OCR을 수행하는 코드 (주석 처리).
# res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_box='')
# res = model.chat(tokenizer, image_file, ocr_type='format', ocr_box='')
# res = model.chat(tokenizer, image_file, ocr_type='ocr', ocr_color='')
# res = model.chat(tokenizer, image_file, ocr_type='format', ocr_color='')

# 다중 크롭 OCR을 수행하는 코드 (주석 처리).
# res = model.chat_crop(tokenizer, image_file, ocr_type='ocr')
# res = model.chat_crop(tokenizer, image_file, ocr_type='format')

# 포맷된 OCR 결과를 렌더링하는 코드 (주석 처리).
# res = model.chat(tokenizer, image_file, ocr_type='format', render=True, save_render_file = './demo.html')

# 결과를 출력합니다.
print(res)
