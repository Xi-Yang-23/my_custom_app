# -*- coding: utf-8 -*-
def number_to_chinese(num):
    """将数字转为中文大写金额"""
    if num == 0:
        return "零元整"
    
    # 中文数字和单位
    digits = ["", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    units = ["", "拾", "佰", "仟"]
    big_units = ["", "万", "亿"]
    
    def convert_section(n):
        """转换四位数以内的数字"""
        if n == 0:
            return ""
        res = ""
        str_n = str(n).zfill(4)
        for i, char in enumerate(str_n):
            d = int(char)
            if d != 0:
                res += digits[d] + units[3 - i]
            elif res and not res.endswith("零"):
                res += "零"
        return res.rstrip("零")
    
    # 转为分（避免浮点误差）
    total_fen = int(round(num * 100))
    yuan = total_fen // 100
    jiao = (total_fen % 100) // 10
    fen = total_fen % 10
    
    # 处理元部分（亿/万/元）
    if yuan == 0:
        result = "零元"
    else:
        yi = yuan // 100000000
        wan = (yuan % 100000000) // 10000
        rest = yuan % 10000
        
        parts = []
        if yi:
            parts.append(convert_section(yi) + "亿")
        if wan:
            parts.append(convert_section(wan) + "万")
        if rest:
            parts.append(convert_section(rest))
        elif yi or wan:
            parts.append("零")
        result = "".join(parts) + "元"
    
    # 处理角分
    if jiao == 0 and fen == 0:
        result += "整"
    else:
        if jiao:
            result += digits[jiao] + "角"
        if fen:
            result += digits[fen] + "分"
    
    # 修正“一十”为“十”
    return result.replace("壹拾", "拾")