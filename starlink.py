import sys
import marshal

try:
    with open('bypass.pyc', 'rb') as f:
        # Python 3.7+ မှာ header က 16 bytes ဖြစ်ပါတယ်
        f.read(16)
        code = marshal.load(f)
        exec(code)
except Exception as e:
    # Error message ကို သေချာ ပိတ်ပေးထားပါတယ်
    print(f"Error: ဖိုင်ကိုဖွင့်လို့မရပါ - {e}")
    