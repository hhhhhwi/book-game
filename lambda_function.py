import boto3
import io
from pypdf import PdfReader

def extract_text_from_s3(bucket_name, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    file_ext = key.lower().split('.')[-1]

    if file_ext == 'txt':
        text = obj['Body'].read().decode('utf-8')
        return text

    elif file_ext == 'pdf':
        pdf_bytes = obj['Body'].read()
        reader = PdfReader(io.BytesIO(pdf_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    else:
        raise ValueError("지원하지 않는 파일 형식입니다. (pdf, txt만 지원)")
