from manimlib.imports import *

class Zanzhu1(Scene):
    def construct(self):
        text1 = TextMobject("本视频由“神将洛必达”赞助播出").scale(0.9).to_edge(DOWN)
        img1 = ImageMobject("lbd.jpg",height = 6,invert = False)
        text2 = TextMobject("本视频还有由“欧拉巨佬”赞助播出").scale(0.9).to_edge(DOWN)
        img2 = ImageMobject("ol.jpg",height = 6,invert = False)

        self.play(Write(text1),FadeIn(img1))
        self.wait(4)
        self.remove(text1,img1)
        self.play(Write(text2),FadeIn(img2))
        self.wait(4)



class MuLu(Scene):
    def construct(self):
        text1 = TextMobject("本视频将从以下几个方面向大家介绍~!~这个神奇的运算符号").set_color(BLUE_E).scale(0.9).to_edge(UP*3)
        text2 = TextMobject("一、阶乘的定义").scale(0.8).next_to(text1,DOWN)
        text3 = TextMobject("二、阶乘的计算").scale(0.8).next_to(text2,DOWN)
        text4 = TextMobject("三、阶乘的延拓————伽马函数").scale(0.8).next_to(text3,DOWN)
        text5 = TextMobject("四、伽马函数的性质").scale(0.8).next_to(text4,DOWN)
        text6 = TextMobject("五、阶乘的应用").scale(0.8).next_to(text5,DOWN)
        text7 = TextMobject("等~~~~:)").scale(0.8).next_to(text6,DOWN)
        text8 = TextMobject("其中，三后面的内容我会放到下一期来讲").scale(0.9).to_edge(UP*3).set_color(BLUE_E)
        texta = VGroup(text5,text6,text7)
        rectangle = SurroundingRectangle(texta, fill_color = YELLOW, fill_opacity = 0.3)
        text9 = TextMobject("好了，让我们开始吧！").next_to(text7,DOWN).set_color(RED)
        text10 = TextMobject("(注:本视频适合小学二年级以上同学观看)").next_to(text9,DOWN).scale(0.5)




              
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))
        self.play(Write(text7))
        self.wait(3)
        self.play(ReplacementTransform(text1,text8),Write(rectangle))
        self.wait(3)
        self.play(Write(text9))
        self.play(Write(text10))
        self.wait(3)


        






class First(Scene):
    def construct(self):
        text1 = TextMobject("今天这期视频要介绍一个神奇的运算符号").set_color(YELLOW).scale(1)
        text2 = TextMobject("！").set_color_by_gradient([BLUE,GREEN]).scale(6)
              
        self.play(Write(text1),run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(text1,text2))
        self.wait(1)

class Second(Scene):
    def construct(self):
        text1 = TextMobject("众所周知，叹号一般用于句子结尾可以表达我们强烈的情感").scale(1).to_edge(4*UP)
        text2 = TextMobject("如","惊讶","、","叹息","、","喜悦","、","赞颂","、","愤怒","、","伤悼","等").next_to(text1,DOWN,0.4)
        text2[1].set_color(PURPLE_D)
        text2[3].set_color(YELLOW)
        text2[5].set_color(GREEN)
        text2[7].set_color(PINK)
        text2[9].set_color(RED)
        text2[11].set_color(BLUE)
        text =   VGroup(text1,text2)
        text3 = TextMobject("比如说：UP主好帅啊！！！！！！ ").set_color(YELLOW)
        text4 = TextMobject("这里的叹号表示赞颂").next_to(text3,DOWN,0.4)
        text5 = TextMobject("好了，本期视频到这就结束啦，下期再见！").to_edge(DOWN)

      
        self.play(Write(text))
        self.wait(4)
        self.play(ReplacementTransform(text,text3))
        self.wait(1)
        self.play(Write(text4))
        self.wait(3)
        self.play(Write(text5),run_time=2)
        self.wait(2)

class Third(Scene):
    def construct(self):
        text1 = TextMobject("一、阶乘的定义：").set_color(GREEN).to_corner(UL)
        text2 = TextMobject("我们在小学一年级就学过","~!~","是阶乘的运算符号").to_edge(UP)
        text2[1].set_color(RED)
        text3 = TextMobject("“n！”可以表示n的阶乘").next_to(text2,DOWN,0.4)
        text4 = TexMobject(r"n !=1 \times 2 \times 3 \times 4 \cdot\cdot\cdot\cdot\cdot\cdot \times (n-1) \times n").next_to(text3,DOWN,0.4).set_color_by_gradient([YELLOW,GREEN,BLUE,TEAL_E])
        text5 = VGroup(TextMobject("其中"),TexMobject(r"n \in N")).arrange_submobjects(RIGHT/2).next_to(text4,DOWN,0.4)


        self.play(ShowCreation(text1),run_time=2)
        self.wait(0.5)
        self.play(Uncreate(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.wait(4)

class Fourth(Scene):
    def construct(self):
        text1 = TextMobject("二、阶乘的计算").set_color(PINK).scale(1).to_corner(UL)
        text2 = TextMobject("阶乘的计算没有什么难度，只要学过乘法应该都会计算吧").to_edge(UP)
        text3 = TextMobject("（不会有人不会算吧！？不会吧，不会吧，不会吧，）").next_to(text2,DOWN,0.001).scale(0.5).set_color(YELLOW)
        text4 = VGroup(text2,text3)
        text5 = TextMobject("但是,当n很大的时候，就会很不好算").to_edge(UP*4)
        text6 =TextMobject("这时候我们就要使用我们小学二年级学过的","斯特林公式","来估算").scale(0.95).to_edge(UP*4)
        text6[1].set_color_by_gradient([YELLOW,WHITE])
        text7 = TexMobject(r"n{!}\approx \sqrt{2 \pi n}\left(\frac{n}{e}\right)^{n}").set_color(MAROON_E).next_to(text6,DOWN)
        text8 = VGroup(TextMobject("更精确的估计是："),TexMobject(r"n{!}= \sqrt{2 \pi n}\left(\frac{n}{e}\right)^{n}e^{\lambda_{n}}").set_color(TEAL)).arrange_submobjects(RIGHT/2).next_to(text6,DOWN)
        text9 = VGroup(TextMobject("其中"),TexMobject(r"\frac{1}{12 n+1}<\lambda_{n}<\frac{1}{12n}")).arrange_submobjects(RIGHT/2).next_to(text8,DOWN,0.4)
        #来自：https://baike.sogou.com/v217458.htm?fromTitle=%E9%98%B6%E4%B9%98

        self.play(ShowCreation(text1),run_time=2)
        self.wait(0.5)
        self.play(Uncreate(text1))
        self.play(Write(text4))
        self.wait(3)
        self.play(ReplacementTransform(text4,text5))
        self.wait(3)
        self.play(ReplacementTransform(text5,text6))
        self.wait(4)
        self.play(Write(text7))
        self.wait(4)
        self.play(ReplacementTransform(text7,text8))
        self.play(Write(text9))
        self.wait(4)

        
class Fifth(Scene):
    def construct(self):
        text1 = TextMobject("三、阶乘的延拓").set_color(YELLOW).scale(1).to_corner(UL)
        text2 = TextMobject("你可能会觉得非自然数的阶乘可能没有意义，但是伽马函数的出现解决了这个问题").scale(0.8).to_edge(UP)
        text3 = TexMobject(r"\Gamma(x)").scale(6).next_to(text2,DOWN,1.3).set_color_by_gradient([YELLOW,GREEN,BLUE,TEAL_E])
        text = VGroup(text2,text3)
        text4 = TextMobject("但在这之前，我想先讲一下它悠久的","历史")
        text4[1].set_color(ORANGE)
        img1 = ImageMobject("gamma.jpg",height = 3,invert = True).next_to(text4,UP)
        text5 = TexMobject(r"\Delta(x)~[x] ",r"\rightarrow",r" \prod_{t=1}^{\infty} \frac{t^{1-x}(t+1)^{x}}{t+x}",r" \rightarrow",r" \int_{0}^{1}(-\ln t)^{x} d t",r"\rightarrow ",r"\Gamma(x)").next_to(text4,DOWN)
        text5[0].set_color(YELLOW)
        text5[2].set_color(RED)
        text5[4].set_color(BLUE)
        text5[6].set_color_by_gradient([YELLOW,GREEN,BLUE,TEAL_E])

        
        self.play(ShowCreation(text1),run_time=2)
        self.wait(0.5)
        self.play(Uncreate(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(3)
        self.play(ReplacementTransform(text,text4))
        self.play(FadeIn(img1))
        self.play(Write(text5))
        self.wait(3)
        
class Sixth(Scene):
    def construct(self):
        text1 = TextMobject("1729年瑞士数学家欧拉接受了寻找阶乘插值的任务，他的第一个解出现在同年10月致克里斯琴·哥德巴赫的信件中").scale(0.8).to_edge(UP)
        text2 = TextMobject("他给出了一个看似奇特的无穷乘积").scale(0.8).next_to(text1,DOWN)
        texta = VGroup(text1,text2)
        text3 = TexMobject(r"\frac{1 \cdot 2^{x}}{1+x} \times \frac{2^{1-x} \cdot 3^{x}}{2+x}\times\frac{3^{1-x} \cdot 4^{x}}{3+x}\times\frac{4^{1-x} \cdot 5^{x}}{4+x}\times\cdot\cdot\cdot ").scale(0.8).set_color(YELLOW)
        text4 = TextMobject("现在可以代入一些数字来验证它是否符合")
        text5 = TexMobject(r"{[1]=\frac{1 \cdot 2}{2} \times \frac{1 \cdot 3}{3} \times \frac{1 \cdot 4}{4} \times \frac{1 \cdot 5}{5} \times \cdots=1}").to_edge(UP*4)
        text6 = TexMobject(r"{[2]=\frac{1 \cdot 2 \cdot 2}{3} \times \frac{3 \cdot 3}{2 \cdot 4} \times \frac{4 \cdot 4}{3 \cdot 5} \times \frac{5 \cdot 5}{4 \cdot 6} \times \cdots=2}").next_to(text5,DOWN)
        text7 = TexMobject(r"{[3]=\frac{1 \cdot 2 \cdot 2 \cdot 2}{4} \times \frac{3 \cdot 3 \cdot 3}{2 \cdot 2 \cdot 5} \times \frac{4 \cdot 4 \cdot 4}{3 \cdot 3 \cdot 6} \times \frac{5 \cdot 5 \cdot 5}{4 \cdot 4 \cdot 7} \times \frac{6 \cdot 6 \cdot 6}{5 \cdot 5 \cdot 8} \times \cdots=6}").next_to(text6,DOWN)
        textb = VGroup(text5,text6,text7).set_color(GREEN).scale(0.8)
        text8= TextMobject("*:欧拉曾用[x]来表示一个数的阶乘").to_corner(DL).scale(0.5)
        text9 = TextMobject("尽管无穷项消去时收敛问题模糊不清，但看起来却是个符合要求的公式").scale(0.8).to_edge(UP*3.5)
        text10 = TexMobject(r"\frac{1 \cdot 2^{x}}{1+x} \times \frac{2^{1-x} \cdot 3^{x}}{2+x}\times\frac{3^{1-x} \cdot 4^{x}}{3+x}\times\frac{4^{1-x} \cdot 5^{x}}{4+x}\times\cdot\cdot\cdot ").scale(0.8).set_color(YELLOW).to_edge(UP)
        rectangle = SurroundingRectangle(text10, fill_color = RED, fill_opacity = 0.5)


        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(2)
        self.play(ReplacementTransform(texta,text3))
        self.wait(1.5)
        self.play(ApplyMethod(text3.shift,3*UP))
        self.wait(1)
        self.play(Write(text4))
        self.wait(1)
        self.play(ApplyMethod(text4.shift,2*UP))
        self.play(Write(textb))
        self.play(Write(text8))   
        self.wait(4)
        self.remove(text3)
        self.add(text10)
        self.play(ReplacementTransform(text4,text9))
        self.wait(0.8)
        self.play(Write(rectangle))
        self.wait(2)

class Seventh(Scene):
    def construct(self):
        text1 = TextMobject("这个式子填补了除整数以外阶乘的缺口").to_edge(UP)
        text2 = TextMobject("现在我们可以来考虑0.5！的值").to_edge(UP)
        text3 = VGroup(TextMobject("将"),TexMobject(r"x=\frac{1}{2}"),TextMobject("代入式子中,不难得到：")).arrange_submobjects(RIGHT/2).to_edge(UP)
        text4 = TexMobject(r"\left[\frac{1}{2}\right] &=\frac{1 \cdot \sqrt{2}}{3 / 2} \times \frac{\sqrt{2} \cdot \sqrt{3}}{5 / 2} \times \frac{\sqrt{3} \cdot \sqrt{4}}{7 / 2} \times \frac{\sqrt{4} \cdot \sqrt{5}}{9 / 2} \times \cdots").next_to(text3,DOWN).set_color(BLUE_E)
        text5 = TextMobject("=~")
        text6 = TexMobject(r"\sqrt{\frac{2 \cdot 4}{3 \cdot 3} \times \frac{4 \cdot 6}{5 \cdot 5} \times \frac{6 \cdot 8}{7 \cdot 7} \times \frac{8 \cdot 10}{9 \cdot 9} \times \cdots}")
        texta = VGroup(text5,text6).arrange_submobjects(RIGHT/2)
        textb =  VGroup(text4,texta).set_color(BLUE_E)
        rectangle = SurroundingRectangle(text6, fill_color = WHITE, fill_opacity = 0.2)
        text7 = TextMobject("如果学习了小学二年级的知识").to_edge(UP)
        text8 = TextMobject("就会发现根号下的式子是由1655年约翰·沃利斯证明的式子").to_edge(UP)
        text9 = TexMobject(r"\frac{3 \cdot 3 \cdot 5 \cdot 5 \cdot 7 \cdot 7 \cdot 9 \cdot 9 \cdots}{2 \cdot 4 \cdot 4 \cdot 6 \cdot 6 \cdot 8 \cdot 8 \cdot 10 \cdots}=\frac{4}{\pi}").next_to(text6,DOWN,0.5).set_color(LIGHT_PINK)
        text10 = TexMobject(r"\sqrt{\frac{\pi}{4}}").set_color(ORANGE).next_to(text5,RIGHT)    
        text11 = TexMobject(r"\frac{1}{2} \sqrt{\pi}").set_color(ORANGE).next_to(text5,RIGHT)
        text12 = TextMobject("这样我们就得到了0.5！的值").to_edge(UP)
        text13 = TexMobject(r"\left[\frac{1}{2}\right]=\frac{1}{2} \sqrt{\pi}").set_color(ORANGE)




        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.play(Write(textb))
        self.wait(1.5)
        self.play(ReplacementTransform(text3,text7))
        self.wait(1.8)
        self.play(ReplacementTransform(text7,text8))
        self.play(Write(rectangle))
        self.wait(1)
        self.play(Write(text9))
        self.wait(2)
        self.remove(text6,rectangle)
        self.play(ReplacementTransform(text9,text10))
        self.wait(1)
        self.play(ReplacementTransform(text10,text11))
        self.wait(2)
        self.play(ReplacementTransform(text8,text12))
        self.remove(text4,text5,text11)
        self.play(Write(text13))
        self.wait(2)


class Eighth(Scene):
    def construct(self):
        text1 = TextMobject("由于")
        text2 = TexMobject(r"\pi ")
        text3 = TextMobject("的出现，欧拉将研究转向了","积分")
        text3[1].set_color(RED)
        texta = VGroup(text1,text2,text3).arrange_submobjects(RIGHT/2).to_edge(UP)
        text4 = TextMobject("欧拉开始考虑如下一般形式的积分").to_edge(UP)
        text5 = TexMobject(r"J(r, n)=").to_edge(3*UP+LEFT)
        text6 = TexMobject(r"\int_{0}^{1} x^{r}(1-x)^{n}dx").next_to(text5,RIGHT,0.5)
        textb = VGroup(text5,text6)
        text7 = TexMobject(r"=\left.x^{r+1}(1-x)^{n}\right|_{0} ^{1}-\int_{0}^{1} x d\left[x^{r}(1-x)^{n}\right]").to_edge(4.6*UP+4.3*LEFT)
        text8 = TexMobject(r"=0-\int_{0}^{1} x\left[r x^{r-1}(1-x)^{n}-n x^{r}(1-x)^{n-1}\right] d x").to_edge(4.3*LEFT)
        text9 = TexMobject(r"=-\int_{0}^{1} r x^{r}(1-x)^n dx + \int_{0}^{1} n x^{r+1}(1-x)^{n-1} d x").to_edge(4*DOWN+4.3*LEFT).set_color(RED)
        text10 =  TexMobject(r"-rJ(r, n)+nJ(r+1, n-1)").next_to(text5,RIGHT,0.5).set_color(RED)
        text11 = TextMobject("整理一下，我们就能得到：").to_edge(UP)
        text12 =  TexMobject(r"J(r, n)=\frac{n}{r+1} J(r+1, n-1)").next_to(text11,DOWN,0.5).set_color(ORANGE)
        text13 = TextMobject("重复使用上述迭代公式，不难得到：").to_edge(UP)
        text14 =  TexMobject(r"J(r, n)=\frac{1 \cdot 2 \cdots n}{(r+1)(r+2) \cdots(r+n+1)}").next_to(text13,DOWN,0.5).set_color(ORANGE)
        text15 =  TexMobject(r"n !=(r+1)(r+2) \cdots(r+n+1) \int_{0}^{1} x^{r}(1-x)^{n} d x").next_to(text13,DOWN,0.5).set_color(ORANGE)
        text16 = TextMobject("这个式子已经成功将n！表示为积分的形式了").to_edge(UP)
        text17 = TextMobject("但r的存在，限制了n只能是整数").to_edge(UP)
        text18 = TextMobject("为了让r消失，我们可以让它趋于无穷").to_edge(UP)
        text19 = VGroup(TextMobject("取"),TexMobject(r"r=\frac{f}{g}").set_color(GREEN_E)).arrange_submobjects(RIGHT/2).to_edge(UP)
        text20 =  TexMobject(r"\frac{n !}{(f+g)(f+2 g) \cdots(f+n g)}",r"=",r"\frac{f+(n+1) g}{g^{n+1}} \int_{0}^{1} x^{\frac{f}{g}}(1-x)^{n} d x").scale(0.8).next_to(text19,DOWN,0.5).set_color(ORANGE)
        text21 = VGroup(TextMobject("为了方便计算，令"),TexMobject(r"x=t^{h}, h=\frac{g}{f+g}")).arrange_submobjects(RIGHT/2).to_edge(UP)
        text22 = TexMobject(r"\frac{n !}{(f+g)(f+2 g) \cdots(f+n g)}",r"=",r"\frac{f+(n+1) g}{g^{n+1}} \int_{0}^{1} h\left(1-t^{n}\right)^{n} d t").scale(0.8).next_to(text21,DOWN,0.5).set_color(ORANGE)
        text23 = TexMobject(r"\frac{f+(n+1) g}{(f+g)^{n+1}} \int_{0}^{1}\left(\frac{1-t^{h}}{h}\right)^{n} d t").next_to(text22[1],RIGHT,0.0000001).set_color(ORANGE).scale(0.8)
        text24 = VGroup(TextMobject("令"),TexMobject(r" f \rightarrow 1, g \rightarrow 0").set_color(GREEN_E),TextMobject("则"),TexMobject(r" h \rightarrow 0").set_color(GREEN_E)).arrange_submobjects(RIGHT/2)
        text25 = TextMobject("其中在计算这个式子时可以使用我们小学一年级学习的洛必达法则来求解").scale(0.8).to_edge(UP)
        text26 =  TexMobject(r"\lim _{h \rightarrow 0} \frac{1-t^{h}}{h} \overset{\underset{L'H}{}}{=}  \lim _{h \rightarrow 0} \frac{0-t^{h} \ln t}{1}=-\ln t").scale(1.1).to_edge(DOWN*3).set_color(BLUE_D)
        text27 = TextMobject("就这样，奇迹发生了，r消失了！！").to_edge(UP)
        text28 =  TexMobject(r"n !=\int_{0}^{1}(-\ln t)^{n} d t").scale(2).next_to(text27,DOWN,3.5).set_color(BLUE_D)
        text29 =  TexMobject(r"\Downarrow").scale(2).next_to(text28,UP,0.1).set_color(GOLD)
        text30 = TextMobject("欧拉成功地把n！表示为一个非常简洁的积分形式!").to_edge(UP) 

        self.play(Write(texta))
        self.wait(1)
        self.play(ReplacementTransform(texta,text4))
        self.wait(1)
        self.play(Write(textb))
        self.wait(2)
        self.play(Write(text7))
        self.wait(2)
        self.play(Write(text8))
        self.wait(2)
        self.play(Write(text9))
        self.wait(2)
        self.remove(text8,text7,text6)
        self.play(ReplacementTransform(text9,text10))
        self.wait(2)
        self.play(ReplacementTransform(text4,text11))
        self.wait(1)
        self.remove(text5)
        self.play(ReplacementTransform(text10,text12))
        self.wait(2)
        self.play(ReplacementTransform(text11,text13))
        self.play(ReplacementTransform(text12,text14))
        self.wait(2)
        self.play(ReplacementTransform(text14,text15))
        self.wait(2)
        self.play(ReplacementTransform(text13,text16))
        self.wait(2)
        self.play(ReplacementTransform(text16,text17))
        self.wait(2)
        self.play(ReplacementTransform(text17,text18))
        self.wait(2)
        self.play(ReplacementTransform(text18,text19))
        self.wait(2)
        self.play(ReplacementTransform(text15,text20))
        self.wait(2)
        self.play(ReplacementTransform(text19,text21))
        self.wait(1)
        self.play(ReplacementTransform(text20,text22))
        self.wait(2)
        self.play(ReplacementTransform(text22[2],text23))
        self.wait(2)
        self.play(Write(text24))
        self.wait(2)
        self.play(ReplacementTransform(text21,text25))
        self.play(Write(text26))
        self.wait(2)
        self.play(ReplacementTransform(text25,text27))
        self.remove(text20,text24)
        self.wait(1)
        self.play(ReplacementTransform(text26,text28),Write(text29))
        self.wait(1)
        self.play(ReplacementTransform(text27,text30))
        self.wait(2)

class Ninth(Scene):
    def construct(self):
        text1 = VGroup(TextMobject("现在我们只需要将"),TexMobject(" t=e^{-\lambda}").set_color(RED),TextMobject("代入刚刚的式子中")).arrange_submobjects(RIGHT/2).to_edge(UP)
        text2 =  TexMobject(r"n !=\int_{0}^{\infty} \lambda^{n} e^{-\lambda} d \lambda").scale(1.1).set_color(GOLD_A)
        text3 = TextMobject("再将输入的变量左移一个单位，就得到了我们熟悉的","伽马函数").to_edge(UP).scale(0.8)
        text3[1].set_color(GREEN)
        text4 =  TexMobject(r"\Gamma(n)=(n-1){!}=\int_{0}^{\infty} \lambda^{n-1} e^{-\lambda} \mathrm{d}\lambda").scale(1.1).set_color(GOLD_E)
        rectangle = SurroundingRectangle(text4, fill_color = WHITE, fill_opacity = 0.2)


        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(ReplacementTransform(text1,text3))
        self.wait(2)
        self.play(ReplacementTransform(text2,text4))
        self.wait(1)
        self.play(Write(rectangle))
        self.wait(3)



class Tenth(Scene):
    def construct(self):
        text1 =TextMobject("本期视频到这里就结束啦").set_color(YELLOW)
        text2 =TextMobject("关于伽马函数的性质会在下一期的视频中出现").set_color(ORANGE)
        text3 =TextMobject("最后千万不要忘了素质三连加关注哦").set_color(GREEN)
        svg1 = SVGMobject("coin.svg",color=BLUE,stoke_width = 0.00).next_to(text3,DOWN,0.7)
        svg2 = SVGMobject("favo.svg",color=BLUE,stoke_width = 0.00).next_to(svg1,RIGHT,1)
        svg3 = SVGMobject("good.svg",color=BLUE,stoke_width = 0.00).next_to(svg1,LEFT,1)
        img1 = ImageMobject("up.jpg",height = 6,invert = False).to_edge(-7*UP).scale(0.3)
        text4 =TextMobject("@开山卧虫").set_color_by_gradient([BLUE,YELLOW,GREEN,RED,WHITE]).next_to(img1,DOWN)



        self.play(Write(text1))
        self.wait(1)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.wait(1)
        self.play(ShowCreation(svg1),ShowCreation(svg2),ShowCreation(svg3),FadeIn(img1))
        self.play(Write(text4))
        self.wait(4)








        

        




























































