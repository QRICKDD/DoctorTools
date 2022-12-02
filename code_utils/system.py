


#输入字符串变成二进制
def test_str_to_bin():
    in_str="djc 开源万岁！"
    in_str_utf=in_str.encode('utf-8')
    in_str_utf_hex=in_str_utf.hex()#把十进制变成16,因为uft就是十六进制
    in_str_utf_hex_int=int(in_str_utf_hex,base=16) #把in_str_uft_hexs视为16进制，转为10进制
    byte=bin(in_str_utf_hex_int) #把十进制改为2进制

    print("in_str_utf",in_str_utf)
    print("in_str_utf_hex",in_str_utf_hex)
    print("in_str_utf_hex_int", in_str_utf_hex_int)
    print(byte)

    #另外一种方法用bytearray  但是这种方法 存在中文时候会编码 空格子也是 或长 或短
    byte_in_str=map(bin,bytearray(in_str,'utf-8'))
    byte_in_str=[item for item in byte_in_str]
    print(" ".join(byte_in_str))


    #另外一种方法是bytearray + join +formate 参考bch
    bch_in_str= bytearray(in_str, 'utf-8')
    print("bch_in_str",bch_in_str)
    bch_res = ' '.join(format(x, '08b') for x in bch_in_str)
    print(bch_res)

#解码 解码流程  二进制->十进制->bytes编码-
def test_bin_to_str():
    in_str = "djc 开源万岁！"
    bch_in_str = bytearray(in_str, 'utf-8')
    print("bch_in_str", bch_in_str)
    bch_res = ''.join(format(x, '08b') for x in bch_in_str)
    print(bch_res)

    #开始解码 bytes可以把十进制变成对应的utf-8字符 然后在用utf-8解码就行了
    packet = bytes(int(bch_res[i: i + 8], 2) for i in range(0, len(bch_res),8))
    print(packet)
    print(packet.decode('utf-8'))

    #示例
    print(bytes([40,41]).decode('utf-8'))



