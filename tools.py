import hashlib

def md5_generator(raw_pass):
    md5_pass = hashlib.md5()
    md5_pass.update(raw_pass.encode('utf-8'))
    return md5_pass.hexdigest()
