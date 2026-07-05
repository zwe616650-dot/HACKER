import sys
import marshal
import os

file_path = 'bypass.pyc'

if not os.path.exists(file_path):
    print(f"Error: '{file_path}' ဖိုင်ကို ရှာမတွေ့ပါ။")
else:
    try:
        with open(file_path, 'rb') as f:
            # header 16 bytes ကို ဖတ်ပြီးမှ marshal.load လုပ်ပါ
            header = f.read(16)
            if len(header) < 16:
                print("Error: ဖိုင် header မပြည့်စုံပါ။")
            else:
                code = marshal.load(f)
                exec(code)
    except EOFError:
        print("Error: ဖိုင်ထဲတွင် data မရှိပါ သို့မဟုတ် corrupt ဖြစ်နေသည်။")
    except ValueError as ve:
        print(f"Error: Python version မကိုက်ညီခြင်း ဖြစ်နိုင်သည်။ ({ve})")
    except Exception as e:
        print(f"Error: တစ်စုံတစ်ခု မှားယွင်းနေသည် - {e}")
        