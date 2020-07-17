from manimlib.imports import *

class MyText(Text):
    CONFIG = {
        'font' : '黑体',
        'size' : 0.5,
        'stroke_width':1,
    }

class text(Text):
    CONFIG = {
        'font' : '儿童卡通字体',
        'size' : 0.5,
        'stroke_width':1,
    }

class First(Scene):
    def construct(self):
        text1 = MyText("本视频将会以互动视频的形式")
        text2 = MyText("考查大家对数学知识的掌握").next_to(text1,DOWN)
        texta = VGroup(text1,text2)
        text3 = MyText("视频灵感来源于數心的互动视频")
        text4 = MyText("BV147411n7yT").next_to(text3,DOWN).set_color(YELLOW)
        textb = VGroup(text3,text4)
        text5 = MyText("准备好了吗？（共10题）")

        
        self.play(ShowCreation(texta))
        self.wait(1.5)
        self.play(ReplacementTransform(texta,textb))
        self.wait(2)
        self.play(ReplacementTransform(textb,text5))
        self.wait(1.5)

class Second(Scene):
    def construct(self):
        text1 = text("第一题").to_edge(2*UP)
        text2 = text("以下哪位是数学家伽罗瓦").next_to(text1,DOWN,1).set_color(YELLOW)
        text3 = text("A.").to_edge(4*DOWN+LEFT)
        img1 = ImageMobject("gs.jpg",height = 3,invert = False).next_to(text3,RIGHT)
        text4 = text("B.").next_to(img1,RIGHT)
        img2 = ImageMobject("jlw.jpg",height = 3,invert = False).next_to(text4,RIGHT)
        text5 = text("C.").next_to(img2,RIGHT)
        img3 = ImageMobject("lglr.jpg",height = 3,invert = False).next_to(text5,RIGHT)
        text6 = text("D.").next_to(img3,RIGHT)
        img4 = ImageMobject("lm.jpg",height = 3,invert = False).next_to(text6,RIGHT)



        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3),FadeIn(img1))
        self.play(Write(text4),FadeIn(img2))
        self.play(Write(text5),FadeIn(img3))
        self.play(Write(text6),FadeIn(img4))
        self.wait(2)

class Third(Scene):
    def construct(self):
        text1 = text("第二题").to_edge(2*UP)
        text2 = text("   公元前5世纪，毕达哥拉斯学派的成员希帕索斯发\n现：等腰直角三角形斜边与一直角边是不可公度的，\n它们的比不能归结为整数或整数之比。这一发现触发\n了_________").next_to(text1,DOWN,1).set_color(YELLOW)
        text3 = text("A.第一次数学危机").next_to(text2,DOWN,0.5).set_color(RED)
        text4 = text("B.第二次数学危机").next_to(text3,DOWN).set_color(GREEN)
        text5 = text("C.第三次数学危机").next_to(text4,DOWN).set_color(BLUE)
        text6 = text("D.第四次数学危机").next_to(text5,DOWN).set_color(GOLD)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Fourth(Scene):
    def construct(self):
        text1 = text("第三题").to_edge(2*UP)
        text2 = text("著名的理发师悖论又叫作_____").next_to(text1,DOWN,1)
        text3 = text("A.罗尔悖论").next_to(text2,DOWN,0.5).set_color(GREEN)
        text4 = text("B.无限猴子悖论").next_to(text3,DOWN,0.5).set_color(BLUE)
        text5 = text("C.罗素悖论").next_to(text4,DOWN,0.5).set_color(GOLD)
        text6 = text("D.阿基里斯悖论").next_to(text5,DOWN,0.5).set_color(RED)

        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Fifth(Scene):
    def construct(self):
        text1 = text("第四题").to_edge(2*UP)
        text2 = text("433是第几个素数").next_to(text1,DOWN,1)
        text3 = text("A.83").next_to(text2,DOWN,0.5).set_color(BLUE)
        text4 = text("B.84").next_to(text3,DOWN,0.5).set_color(GOLD)
        text5 = text("C.85").next_to(text4,DOWN,0.5).set_color(RED)
        text6 = text("D.86").next_to(text5,DOWN,0.5).set_color(GREEN)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Sixth(Scene):
    def construct(self):
        text1 = text("第五题").to_edge(2*UP)
        text2 = text("    哈代探望病重的拉马努金时，拉马努金认为以下哪个数\n是很有趣的数").next_to(text1,DOWN,1)
        text3 = text("A.314").next_to(text2,DOWN,0.5).set_color(GOLD)
        text4 = text("B.1729").next_to(text3,DOWN,0.5).set_color(RED)
        text5 = text("C.2333").next_to(text4,DOWN,0.5).set_color(GREEN)
        text6 = text("D.42").next_to(text5,DOWN,0.5).set_color(BLUE)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Seventh(Scene):
    def construct(self):
        text1 = text("第六题").to_edge(2*UP)
        text2 = text("     1830年法国数学家傅里叶卒于法国巴黎，导致其不幸身\n亡的化学方程式是").next_to(text1,DOWN,1)
        text3 = TexMobject(r"A.2 H_{2} S+3 O_{2}\overset{\underset{\text {点燃}}{}}{=} 2 H_{2} O+2 S O_{2}").next_to(text2,DOWN,0.5).set_color(RED)
        text4 = TexMobject(r"B.2 C + O_{2}\overset{\underset{\text {点燃}}{}}{=} 2 CO").next_to(text3,DOWN,0.5).set_color(GREEN)
        text5 = TexMobject(r"C.4 \mathrm{HCl} \text { (浓) }+\mathrm{MnO}_{2}\triangleq\mathrm{MnCl}_{2}+2 \mathrm{H}_{2} \mathrm{O}+\mathrm{Cl}_{2} \uparrow").next_to(text4,DOWN,0.5).set_color(BLUE)
        text6 = TexMobject(r"D.3 \mathrm{NO} _{2}+\mathrm{H} _{2} \mathrm{O}=2 \mathrm{HNO} _{3}+\mathrm{NO}").next_to(text5,DOWN,0.5).set_color(GOLD)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Eighth(Scene):
    def construct(self):
        text1 = text("第七题").to_edge(2*UP)
        text2 = text("    哈代乘坐一条小船返回英国，为了旅途的平安，他给\n玻尔发去了一张简短的明信片，明信片上面的内容为：").next_to(text1,DOWN,1)
        text3 = text("A.这可能是我见你的最后一面了").next_to(text2,DOWN,0.5).set_color(GREEN)
        text4 = text("B.我已经证明黎曼猜想了").next_to(text3,DOWN,0.5).set_color(GOLD)
        text5 = text("C.黎曼猜想可能我这辈子都无法证明了").next_to(text4,DOWN,0.5).set_color(RED)
        text6 = text("D.黎曼猜想可能是一个永远也解不开的迷").next_to(text5,DOWN,0.5).set_color(BLUE)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Ninth(Scene):
    def construct(self):
        text1 = text("第八题").to_edge(2*UP)
        text2 = VGroup(text("当"),TexMobject(r"n"),text("满足什么条件时,"),TexMobject(r"x^{n}+y^{n}=z^{n}"),text("无正整数解")).arrange_submobjects(RIGHT/2).next_to(text1,DOWN,1)
        text3 = VGroup(text("A.当"),TexMobject(r"n \in \mathbb{Q}")).arrange_submobjects(RIGHT/2).next_to(text2,DOWN,0.5).set_color(RED)
        text4 = VGroup(text("B.当"),TexMobject(r"n>0")).arrange_submobjects(RIGHT/2).next_to(text3,DOWN,0.5).set_color(GOLD)
        text5 = VGroup(text("C.当"),TexMobject(r"n>4 \text{且为整数}")).arrange_submobjects(RIGHT/2).next_to(text4,DOWN,0.5).set_color(BLUE)
        text6 = VGroup(text("D.当"),TexMobject(r"n>2 \text{且为整数}")).arrange_submobjects(RIGHT/2).next_to(text5,DOWN,0.5).set_color(GREEN)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Tenth(Scene):
    def construct(self):
        text1 = text("第九题").to_edge(2*UP)
        text2 = text("以下不属于千禧问题的是______").next_to(text1,DOWN,1)
        text3 = text("A.四色问题").next_to(text2,DOWN,0.5).set_color(GREEN)
        text4 = text("B.黎曼猜想").next_to(text3,DOWN,0.5).set_color(BLUE)
        text5 = text("C.霍奇猜想").next_to(text4,DOWN,0.5).set_color(GOLD)
        text6 = text("D.NP问题").next_to(text5,DOWN,0.5).set_color(RED)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class Eleventh(Scene):
    def construct(self):
        text1 = text("最后一题").to_edge(1.5*UP)
        text2 = text("右图是一条\n完美的心形线，\n以下选项中\n不是心形线的\n是").to_edge(3*UP+6*LEFT)
        img1 = ImageMobject("xxx.jpg",height = 3,invert = False).next_to(text2,RIGHT,1)
        text3 = TexMobject(r"A.x^{2}+(y-\sqrt[3]{x^{2}})^{2}=1").next_to(text1,DOWN,3.2).set_color(RED)
        text4 = TexMobject(r"B.5 x^{2}-6| x| y+5 y^{2}=128").next_to(text3,DOWN).set_color(GREEN)
        text5 = TexMobject(r"C. r = Arccos(sin\theta )").next_to(text4,DOWN).set_color(BLUE)
        text6 = TexMobject(r"D.-\tan (\sqrt{1-\sqrt{|x|^{3}}})+\frac{\pi}{2}").next_to(text5,DOWN).set_color(GOLD)
        
        self.play(Write(text1))
        self.play(Write(text2),FadeIn(img1))
        self.wait(2)
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.wait(2)

class ABC(Scene):
    def construct(self):
        text1 = MyText("很遗憾，你答对了0-3题").set_color(RED)
        text2 = MyText("看来你对数学的了解还不够深，要继续努力学习鸭！").next_to(text1,DOWN)
        texta = VGroup(text1,text2)

        self.play(ShowCreation(texta),run_time = 3)
        self.wait(3)

class DEF(Scene):
    def construct(self):
        text1 = MyText("不错哦，你答对了4-6题").set_color(RED)
        text2 = MyText("看来你对数学的了解还阔以哦，要继续努力学习鸭！").next_to(text1,DOWN)
        texta = VGroup(text1,text2)

        self.play(ShowCreation(texta),run_time = 3)
        self.wait(3)

class GHIJ(Scene):
    def construct(self):
        text1 = MyText("NB！你答对了7-10题").set_color(RED)
        text2 = MyText("看来你对数学很了解呢！").next_to(text1,DOWN)
        texta = VGroup(text1,text2)

        self.play(ShowCreation(texta),run_time = 3)
        self.wait(3)