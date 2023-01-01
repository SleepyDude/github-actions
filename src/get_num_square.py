import os

num = os.getenv('INPUT_NUM')
if num:
    try:
        num = int(num)
    except Exception:
        exit('ERROR: The INPUT_NUM provided ("{}") is not an integer'.format(num))
else:
    num = 1

print(f"::set-output name=num_squared::{num**2}")