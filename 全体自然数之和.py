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


class Line(Line):
    CONFIG = {
            "fill_color":YELLOW,
            "fill_opacity": 3.0,
            "stroke_color": None,
            "stroke_opacity": 1.0,
            "stroke_width": DEFAULT_STROKE_WIDTH,
            # The purpose of background stroke is to have
            # something that won't overlap the fill, e.g.
            # For text against some textured background
            "background_stroke_color": BLACK,
            "background_stroke_opacity": 1.0,
            "background_stroke_width": 0,
            # When a color c is set, there will be a second color
            # computed based on interpolating c to WHITE by with
            # sheen_factor, and the display will gradient to this
            # secondary color in the direction of sheen_direction.
            "sheen_factor": 0.0,
            "sheen_direction": UL,
            # Indicates that it will not be displayed, but
            # that it should count in parent mobject's path
            "close_new_points": False,
            "pre_function_handle_to_anchor_scale_factor": 0.01,
            "make_smooth_after_applying_functions": False,
            "background_image_file": None,
            "shade_in_3d": False,
            # This is within a pixel
            # TODO, do we care about accounting for
        }

class kt(Scene):
    def construct(self):
        text1 = Text("本视频为UP主第一次尝试用manim来制作视频", font = "Qisimomo_xinjian").set_color_by_gradient([BLUE]).scale(0.5)
        text2 = TextMobject("如果有什么不足的地方，欢迎大家在评论区指出！",size = 0.5).set_color_by_gradient([BLUE]).to_edge(6*DOWN)
        text  = VGroup(text1,text2)
        text3 =TextMobject("那么就让我们开始吧！").set_color_by_gradient([BLUE])

        self.play(Write(text))
        self.wait(2)
        self.play(ReplacementTransform(text,text3))

        self.wait(2.5)


class Introduction(Scene):
    def construct(self):
        text1 = TextMobject("我们在幼儿源就学过:").to_corner(UL)
        tex1 = TexMobject(r"""1+2=3 \text{, } 1+2+3=6 \text{, } 1+2+3+4=10……""",size = 3.5)
        text2 = TextMobject("我们也知道:").to_edge(LEFT+4.5*UP)
        tex2 = TexMobject(r"""1+2+3+4+5+6+……+100=5050""",size = 3.5)
        text3 = TextMobject("那么，让我们来思考这个问题:").to_edge(LEFT+8*UP)
        tex3 = TexMobject(r"1+2+3+4+5+6+……+100+101+……=",size = 3.5).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).to_edge(3*DOWN)
        text4 = TextMobject("?").to_edge(2*RIGHT+3*DOWN).set_color_by_gradient([RED])
        
        self.play(Write(text1))
        self.play(Write(tex1))
        self.wait(1)
        self.play(ApplyMethod(tex1.shift,2.5*UP))

        self.play(Write(text2))
        self.play(Write(tex2))
        self.wait(1)
        self.play(ApplyMethod(tex2.shift,0.75*UP))

        self.play(Write(text3))
        self.play(Write(tex3))
        self.play(Write(text4))
        
        self.wait(3)



class ky(Scene):
    def construct(self):
        text1 =  TextMobject("我们可以将这个问题写成级数的形式，就像这样:",size = 0.5)
        tex3 = TexMobject(r"""1+2+3+4+5+6+……+100+101+……""",size = 3.5).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text4 = TextMobject("=?").to_edge(2*RIGHT).set_color_by_gradient([RED])
        text2 = TexMobject(r"\sum_{x=1}^\infty {x} ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text3 = TextMobject("但问题来了",size = 0.5).to_edge(LEFT+4.5*UP).set_color_by_gradient([YELLOW])
        L1 = Line(np.array([-0.75,-0.75,0]),np.array([-2,-2,0]),color=RED)
        text5 = TextMobject("这玩意发散，怎么算呢？",size = 0.55).set_color_by_gradient([GREEN]).to_edge(3.5*LEFT+2*DOWN)
        
        self.play(Write(text1))
        self.play(ApplyMethod(text1.shift,3*UP+1.5*LEFT))
        self.play(Write(tex3))
        self.play(Write(text4))
        self.wait(2)
        self.play(ReplacementTransform(tex3,text2))
        self.play(ApplyMethod(text4.shift,4.7*LEFT))
        self.wait(1)
        self.play(Write(text3))
        self.play(Write(L1))
        self.play(Write(text5))
        self.wait(4)

class yk(Scene):
    def construct(self):
        text1 =  TextMobject("要解决这个问题需要知道这两个知识:",size = 0.5).to_corner(UL).set_color_by_gradient([BLUE])
        text2 = TextMobject("1.牛顿广义二项式定理")
        text3 = TextMobject("2.基本数学知识""").to_edge(5*DOWN)
        text  = VGroup(text2,text3)
        
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text))
        self.wait(3)

class zp(Scene):
    def construct(self):
        text1 =  TextMobject("广义二项式定理最早出现在牛顿回复莱布尼兹的《前信》中",size = 0.3).scale(0.9).to_corner(UL)
        text2 =  TextMobject("具体长这个亚子：",size = 0.5)
        text3 = TexMobject(r"(P+PQ)^{\frac{m}{n}}=  P^{\frac{m}{n}}+{\frac{m}{n}}AQ+{\frac{m-n}{2n}BQ}+{\frac{m-2n}{3n}CQ}+{\frac{m-3n}{4n}DQ}+……*",color=BLUE).scale(0.7)
        text4 =  TextMobject("（其中A、B、C、D……分别指该项的前一项)").scale(0.7).set_color_by_gradient([BLUE]). next_to(text3,DOWN,0.4)
        text5 =   TextMobject("*:此处参考了《微积分的历程：从牛顿到勒贝格》一书中的描述").scale(0.6).to_corner(DL)
        text =   VGroup(text3,text4)
        text6 =  TextMobject("现在，请在10秒之内记住这个公式"). next_to(text,DOWN,0)
        text7 =  TexMobject(r"\sum\limits_{n=1}^4 n",color=RED). next_to(text,DOWN,0)
        text8 =  TexMobject(r"\int_{0}^{3}x^2\,dx",color=PURPLE_E). next_to(text,DOWN,0)
        text9 =  TexMobject(r"2(2^2)",color=YELLOW). next_to(text,DOWN,0)
        text10 =  TexMobject(r"\frac{1}{4}\times\dbinom{8}{2}",color=BLUE). next_to(text,DOWN,0)
        text11 =  TexMobject(r"3!",color=GOLD). next_to(text,DOWN,0)
        text12 =  TexMobject(r"\sqrt{\sqrt{7^2+24^2}}",color=PURPLE_A). next_to(text,DOWN,0)
        text13 =  TexMobject(r"\prod\limits_{n=1}^3 \frac{n+1}{n}",color=PINK). next_to(text,DOWN,0)
        text14 =  TexMobject(r"det\begin{vmatrix}5&1\\7&2\end{vmatrix}",color=TEAL_B). next_to(text,DOWN,0)
        text15 =  TexMobject(r"(2x)'",color=DARK_BLUE). next_to(text,DOWN,0)
        text16 =  TexMobject(r"sin(\frac{\pi}{2})",color=MAROON_C). next_to(text,DOWN,0)
        text17 =  TextMobject("时间到，我相信你已经把这个公式记下来了"). next_to(text,DOWN,0)
               
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.play(ApplyMethod(text2.shift,4.8*LEFT+2.5*UP))
        self.play(Write(text),Write(text5))
        self.wait(8)
        self.play(ApplyMethod(text.shift,1.5*UP))
        self.wait(1)
        self.play(ReplacementTransform(text5,text6))
        self.wait(3)
        self.play(ReplacementTransform(text6,text7))
        self.wait(1)
        self.play(ReplacementTransform(text7,text8))
        self.wait(1)
        self.play(ReplacementTransform(text8,text9))
        self.wait(1)
        self.play(ReplacementTransform(text9,text10))
        self.wait(1)
        self.play(ReplacementTransform(text10,text11))
        self.wait(1)
        self.play(ReplacementTransform(text11,text12))
        self.wait(1)
        self.play(ReplacementTransform(text12,text13))
        self.wait(1)
        self.play(ReplacementTransform(text13,text14))
        self.wait(1)
        self.play(ReplacementTransform(text14,text15))
        self.wait(1)
        self.play(ReplacementTransform(text15,text16))
        self.wait(1)
        self.play(ReplacementTransform(text16,text17))
        self.wait(2)


class zp2(Scene):
    def construct(self):
        text1 =  TextMobject("牛顿大佬的表达：").scale(0.9).to_corner(UL)
        text2 = TexMobject(r"(P+PQ)^{\frac{m}{n}}=  P^{\frac{m}{n}}+{\frac{m}{n}}AQ+{\frac{m-n}{2n}BQ}+{\frac{m-2n}{3n}CQ}+{\frac{m-3n}{4n}DQ}+……",color=BLUE).scale(0.7).to_edge(3*UP)
        text3 =  TextMobject("在UP主的努力下，我们也可以将上述公式写成这样：").scale(0.9).to_edge(LEFT+5*UP)
        text4 = TexMobject(r"(P+PQ)^{\frac{m}{n}}= P^{\frac{m}{n}}\left[(1+\sum\limits_{i=1}^\infty\left( \prod\limits_{k=0}^i \frac{m-kn}{n+kn}Q\right)\right] ").scale(1.2).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text5 = VGroup(TextMobject("将两边的"),TexMobject(r"P^{\frac{m}{n}}"),TextMobject("约去，我们可以得到：")) .scale(0.9).to_edge(3*DOWN)
        text5.arrange_submobjects(RIGHT/2).scale(0.9).to_edge(4.5*DOWN)
        text6 = TexMobject(r"(1+Q)^{\frac{m}{n}}= 1+\sum\limits_{i=1}^\infty\left( \prod\limits_{k=0}^i \frac{m-kn}{n+kn}Q\right) ").scale(1).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).to_edge(DOWN)
        

        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(3)
        self.play(Write(text3))
        self.play(ReplacementTransform(text2,text4))
        self.wait(6)
        self.play(Write(text5))
        self.play(ReplacementTransform(text4,text6))
        self.wait(6)




class zp3(Scene):
    def construct(self):
        text1 =  TextMobject("有了这个公式，我们就可以解决最开始的那个问题").scale(1).to_corner(UL)
        text2 =  TextMobject("现在我们考虑这个式子：").scale(1).to_corner(UL)
        text3 =  TexMobject(r"\frac{1}{\left(1-x\right)^2}=",color=YELLOW).scale(1)
        text4 =  TextMobject("?",color=RED)
        text5 =  VGroup(text3,text4)
        text5.arrange_submobjects(RIGHT/2).scale(1)
        text6 = TextMobject("写成这样可能会影响你的思考").scale(1).to_corner(UL)
        text7 = TextMobject("我们可以写成这样").scale(1).to_corner(UL)
        text8 = TexMobject(r"\left({1-x}\right)^{-2}=",color=YELLOW).scale(1)
        text9 =  VGroup(text8,text4)
        text9.arrange_submobjects(RIGHT/2).scale(1)
        text10 =  TextMobject("运用刚才的得到的公式，不难得到：").scale(1).to_corner(UL)
        text11 = TexMobject(r"\left(1-x\right)^{-2}= ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).scale(1).to_edge(LEFT+4.5*UP)
        text12 = TexMobject(r"1+\sum\limits_{i=1}^\infty\left( \prod\limits_{k=0}^i \frac{k+2}{k+1}x\right) ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).scale(1).to_edge(LEFT+4.5*UP)
        text13 =  VGroup(text11,text12)
        text13.arrange_submobjects(RIGHT/2).scale(0.9).to_edge(LEFT+4.5*UP)
        text14 = TexMobject(r"1+2x+3x^2+4x^3+5x^4+……").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).scale(1).to_edge(5.4*UP+6*LEFT)
        text15 =  VGroup(text11,text14)
        text16 =  TextMobject("两边都乘上x，可以得到").scale(1).to_corner(UL)
        text17 =  TexMobject(r"\frac{x}{\left(1-x\right)^2} ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text18 =  TexMobject(r"=")
        text19 =  TexMobject(r"x+2x^2+3x^3+4x^4+5x^5+……")
        text20 =  VGroup(text17,text18,text19)
        text20.arrange_submobjects(RIGHT/2).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text21 =  TextMobject("现在我们将x=-1代入等式").scale(1).to_corner(DOWN)
        text22 =  TexMobject(r"\frac{-1}{\left(1+1\right)^2} ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text23 =  TexMobject(r"=")
        text24 =  TexMobject(r"-1+2\left(-1\right)^2+3\left(-1\right)^3+4\left(-1\right)^4+5\left(-1\right)^5+……")
        text25 =  VGroup(text22,text23,text24)
        text25.arrange_submobjects(RIGHT/2).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text26 = TextMobject("整理一下，我们可以得到").scale(1).to_corner(DOWN)
        text27 =  TexMobject(r"\frac{-1}{4} ").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text28 =  TexMobject(r"=")
        text29 =  TexMobject(r"-1+2-3+4-5+……")
        text30 =  VGroup(text27,text28,text29)
        text30.arrange_submobjects(RIGHT/2).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text31 =  TextMobject("我们可以将等式的右边分为两部分").scale(1).to_corner(UL)
        text32 = TexMobject(r"\begin{cases}-1-3-5-7-9-……\\2+4+6+8+10+…… \end{cases}").next_to(text27,3*RIGHT).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text34 = TextMobject("现在，我们在第一部分的每两项之间-2的倍数，在第二部分的每两项之间+2倍数来保持等式成立").scale(0.8).to_corner(DOWN)
        text35 = TexMobject(r"\begin{cases}-1-2-3-4-5-6-7-8-9-……\\2+2+4+4+6+6+8+8+10+10+…… \end{cases}").scale(0.8).next_to(text27,3*RIGHT).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text36 = TextMobject("我们再整理一下").scale(1).to_corner(DOWN)
        text37 = TexMobject(r"\begin{cases}-\left(1+2+3+4+5+6+7+8+9+……\right)\\4\times\left(1+2+3+4+5+6+7+8+9+……\right)\end{cases}").scale(0.8).next_to(text27,3*RIGHT).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text38 = TextMobject("现在我们只需要将上下两部分相加").scale(1).to_corner(DOWN)
        text39 = TexMobject(r"3\times\left(1+2+3+4+5+6+7+8+9+……\right)").scale(0.8).next_to(text27,3*RIGHT).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text = VGroup(text27,text28,text39)
        text40 = TexMobject(r"-\frac{1}{12}=1+2+3+4+5+6+7+8+9+……").scale(0.8).set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE])
        text41 = TextMobject("至此，这个问题已经解决了").scale(1).to_corner(DOWN)
        
        
        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.play(Write(text5))
        self.wait(2)
        self.play(ReplacementTransform(text2,text6))
        self.wait(2)
        self.play(ReplacementTransform(text6,text7))       
        self.play(ReplacementTransform(text3,text8))
        self.wait(3)
        self.play(ReplacementTransform(text7,text10))
        self.play(ReplacementTransform(text9,text13))
        self.wait(3)
        self.play(ReplacementTransform(text12,text14))
        self.wait(3)
        self.play(ReplacementTransform(text10,text16))
        self.play(ReplacementTransform(text15,text20))
        self.wait(2)
        self.play(Write(text21))
        self.play(ReplacementTransform(text20,text25))
        self.wait(2)
        self.play(ReplacementTransform(text21,text26))
        self.play(ReplacementTransform(text25,text30))
        self.wait(1)
        self.play(ReplacementTransform(text16,text31))
        self.wait(1)
        self.play(ReplacementTransform(text29,text32))
        self.wait(2)
        self.play(ReplacementTransform(text26,text34))
        self.play(ReplacementTransform(text32,text35))
        self.wait(3)
        self.play(ReplacementTransform(text34,text36))
        self.wait(1)
        self.play(ReplacementTransform(text35,text37))
        self.wait(2)
        self.play(ReplacementTransform(text36,text38))
        self.play(ReplacementTransform(text37,text39))
        self.wait(1)
        self.play(ReplacementTransform(text,text40))
        self.play(ReplacementTransform(text38,text41))
        self.remove(text31)
        self.wait(5)

class jw(Scene):
    def construct(self):
        text1 =  TextMobject("看到这个答案，你是不是感到很震惊").scale(1)
        text2 =  TextMobject("学了怎么多年的数学，也许这是你第一次知道正数相加也可以得出负数").scale(0.8)
        text3 =  TextMobject("这可以是正确的，也可以是错误的,主要还是看怎么理解").scale(0.9)
        text4 =  TextMobject("关于全体自然数之和的证明还有很多方法。B站，知乎上一抓一大把").scale(0.8)
        text41 =  TextMobject("如果有兴趣可以去看看哦！！").scale(0.9)
        text5 =TextMobject("本期视频到这里就结束啦").set_color_by_gradient([YELLOW])
        text6 =TextMobject("最后还有一件很重要的事！！").set_color_by_gradient([YELLOW])
        text7 =TextMobject("那就是素质三连（别给我说下次一定 ￣へ￣）！！！").set_color_by_gradient([YELLOW]).to_edge(6*DOWN)  
        text8 =TextMobject("如果能够关注@开山卧虫，那就更好了！！").set_color_by_gradient([YELLOW]).to_edge(6*DOWN)
        textc  = VGroup(text7,text8)
        textc.arrange_submobjects(DOWN).set_color_by_gradient([YELLOW])

        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.wait(2)
        self.play(ReplacementTransform(text3,text4))
        self.wait(2)
        self.play(ReplacementTransform(text4,text41))
        self.wait(4)
        self.play(ReplacementTransform(text41,text5))
        self.wait(2)
        self.play(ReplacementTransform(text5,text6))
        self.wait(2)
        self.play(ReplacementTransform(text6,textc))
        self.wait(5)
