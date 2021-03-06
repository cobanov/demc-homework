import os
import gzip
import shutil


def unzip_files(folder):
    out_files = []

    for file in os.listdir(folder):

        if file.endswith(".gz"):
            in_file_path = os.path.join(folder, file)
            out_file_path = os.path.join(folder, file.replace('.gz', ''))
            out_files.append(out_file_path)

            print('\tUnzipping ', in_file_path, ' to ', out_file_path)

            with gzip.open(in_file_path, 'rb') as f_in:
                with open(out_file_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

    return out_files
