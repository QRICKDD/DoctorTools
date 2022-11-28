import bchlib
import torch
"""
BCH码是一类重要的纠错码，它把信源待发的信息序列按固定的κ位一组划分成消息组，
再将每一消息组独立变换成长为n(n>κ)的二进制数字组，称为码字。如果消息组的数目为M(显然M>=2),
由此所获得的M个码字的全体便称为码长为n、信息数目为M的分组码，
记为n，M。把消息组变换成码字的过程称为编码，其逆过程称为译码。
"""

"""
基本信息
"""
#嵌密信息
pre_secret='Hello'
BCH_POLYNOMIAL = 137  #生成多项式
BCH_BITS = 5
bch = bchlib.BCH(BCH_POLYNOMIAL, BCH_BITS)
"""
字符串转bit流
"""
#不满7个字符就用' '填充,这边是吧字符串变成二进制bit流
data = bytearray(pre_secret + ' '*(7-len(pre_secret)), 'utf-8')
print("加密信息的byte:",data)
ecc=bch.encode(data) #拿到纠错码
print("bch编码:",ecc)
packet=data+ecc  #嵌入纠错码
#使用format函数，将bytearray中存储的十六制数转换为二进制
packet_binary = ''.join(format(x, '08b') for x in packet)
print(packet_binary)
correct_bin=packet_binary
secret = [int(x) for x in packet_binary]
secret.extend([0,0,0,0])#单纯为了凑满100位

#添加错误
secret[0]=1
secret[2]=1

#下面开始解码
packet_binary = "".join([str(int(bit)) for bit in secret[:96]])
packet = bytes(int(packet_binary[i : i + 8], 2) for i in range(0, len(packet_binary), 8))
packet = bytearray(packet)
data, ecc = packet[:-bch.ecc_bytes], packet[-bch.ecc_bytes:] #拿到数据 和纠错码
bitflips = bch.decode_inplace(data, ecc)#纠错 牛皮啊
code = data.decode("utf-8")