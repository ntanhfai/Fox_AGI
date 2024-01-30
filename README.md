# Fox_AGI
## Chú ý khi chạy LLM:

Cần thay đổi biến khai báo định nghĩa đường dẫn:

```python
# Tại đây:
# ...ENV\Lib\site-packages\huggingface_hub\constants.py:95

default_home = os.path.join(os.path.expanduser("~"), ".cache")
```

