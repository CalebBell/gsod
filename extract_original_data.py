import gzip
import os
import shutil
end_year = 2020
start_year = 1929
#end_year = 1929
remove = True

for y in range(start_year, end_year + 1):
    year_str = str(y)
    files = os.listdir(year_str)
    for f in files:
        name = os.path.join(year_str, f)
        if f[-3:] == '.gz':
            new_path = name.replace('.gz', '')
            if not os.path.exists(new_path):
                with gzip.open(name, 'rb') as f_in:
                    with open(new_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
            if remove:
                os.remove(name)
