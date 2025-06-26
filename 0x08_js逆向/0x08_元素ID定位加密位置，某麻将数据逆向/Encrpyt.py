import execjs

def main():
    q =""
    with open('Encrypt.js', 'r', encoding='utf-8') as f:
        decrypt_js = f.read()
    datas = execjs.compile(decrypt_js).call('main', q)
    for data in datas:
        print(data)

if __name__ == '__main__':
    main()
