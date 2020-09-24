import hashlib
def django_md5(args):
    md5 = hashlib.md5()
    md5.update(args.encode('utf-8'))
    str_md5 = md5.hexdigest()
