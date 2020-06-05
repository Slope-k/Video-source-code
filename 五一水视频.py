from manimlib.imports import *
CONFIG = {
        'font' : 'SourceHanSansSC-Normal',
        'size' : 0.5,
        "template_tex_file_body": TEMPLATE_TEX_FILE_BODY,
        # 笔画宽度
        "stroke_width": 0.0,
        # 填充不透明度
        "fill_opacity": 3.0,
        # 笔画的描边宽度
        "background_stroke_width": 1,
        # 笔画的描边颜色
        "background_stroke_color": BLACK,
        "should_center": True,
        "height": None,
        "organize_left_to_right": False,
        "alignment": "",
    }

class kt(Scene):
    def construct(self):
        text1 = TextMobject("如何高雅地使用manim来演绎情话(..›-‹..)").set_color_by_gradient([BLACK]).scale(0.9).to_edge(UP)
        text2 = TextMobject("美").set_color_by_gradient([RED]).to_edge(4*LEFT).scale(1.4)
        text3 = TextMobject("+").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4)
        text4 = TextMobject("心").set_color_by_gradient([GOLD_E]).to_edge(4*LEFT).scale(1.4)
        text5 = TextMobject("=").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4)
        text6 = TextMobject("?").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4)
        text7 = VGroup(text2,text3,text4,text5,text6)
        text7.arrange_submobjects(RIGHT/2).to_edge(4*LEFT).scale(1.4)
        text8 = TextMobject("Mg").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4).set_color_by_gradient([RED])
        text9 = TexMobject(r"ZnSO_4").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4).set_color_by_gradient([GOLD_E])
        text10 = VGroup(text8,text3,text9,text5,text6)
        text10.arrange_submobjects(RIGHT/2).to_edge(4*LEFT).scale(1.4)
        text11 = TextMobject("我相信大家在接受胎教的时候就学过这个方程式").set_color_by_gradient([BLACK]).to_edge(DOWN).scale(0.8)
        text12 = TextMobject("Zn").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4).set_color_by_gradient([GOLD_E])
        text1A = TextMobject("+").set_color_by_gradient([BLACK]).set_color_by_gradient([BLACK])
        text13 = TexMobject(r"Mg",r"SO_4").set_color_by_gradient([BLACK]).to_edge(4*LEFT).scale(1.4)
        text13[0].set_color(RED)
        text13[1].set_color(GOLD_E)
        text14 = VGroup(text12,text1A,text13)
        text14.arrange_submobjects(RIGHT/2).next_to(text10,RIGHT/2).scale(1.4)
        text15 = TextMobject("[你的美偷走了我的心](这梗是不是太老了……)").set_color_by_gradient([BLACK]).to_edge(DOWN).scale(0.8)
        
        
        

        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text7))
        self.wait(2)
        self.play(ReplacementTransform(text2,text8))
        self.play(ReplacementTransform(text4,text9))
        self.play(Write(text11))
        self.wait(1.5)
        self.play(ReplacementTransform(text6,text14))
        self.wait(2)
        self.play(ReplacementTransform(text11,text15))
        self.wait(2)
