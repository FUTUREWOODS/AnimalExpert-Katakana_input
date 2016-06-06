def setup():
    katakana_columns=[]
    #katakana_columns.append("カナ",濁点あり,半濁点あり)
    katakana_columns.append(["アイウエオ",False,False])
    katakana_columns.append(["カキクケコ",True,False])
    katakana_columns.append(["サシスセソ",True,False])
    katakana_columns.append(["タチツテト",True,False])
    katakana_columns.append(["ナニヌネノ",False,False])
    katakana_columns.append(["ハヒフヘホ",True,True])
    katakana_columns.append(["マミムメモ",False,False])
    katakana_columns.append(["ヤユヨ",False,False])
    katakana_columns.append(["ラリルレロ",False,False])
    katakana_columns.append(["ワヲン",False,False])
    katakana_columns.append(["゛゜",False,False]) #濁点、半濁点（特別扱い）

    function_dakuten=""
    for column in katakana_columns:
        if column[1]:
            for kana in column[0]:
                function_dakuten += "if(c=='{}') return '{}';".format(kana,chr(ord(kana)+1))
    function_dakuten += "return c;"

    function_handakuten=""
    for column in katakana_columns:
        if column[2]:
            for kana in column[0]:
                function_handakuten += "if(c=='{}') return '{}';".format(kana,chr(ord(kana)+2))
    function_handakuten += "return c;"

    return katakana_columns,function_dakuten,function_handakuten


def generate_html(katakana_columns,function_dakuten,function_handakuten):
    from jinja2 import Template
    f = open("katakana_input.jinja2")
    template = Template(f.read())
    f.close()
    html = template.render(
            katakana_columns=katakana_columns,
            function_dakuten=function_dakuten,
            function_handakuten=function_handakuten)
    return html



if __name__ == "__main__":
    res = setup()

    html=generate_html(*res)

    f=open("../html/katakana_input.html","w")
    f.write(html)
    f.close()
