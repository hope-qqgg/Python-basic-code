# 1.安装streamlit库
# pip install streamlit

# 2.在Python文件中导入streamlit模块
import streamlit as st

# 3.基于streamlit中提供的API来构建Web应用
# 设置页面的配置项
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    # 页面布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 大标题
st.title("Streamlit 入门示例")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("小鸟游六花是日本轻小说改编的动画《中二病也要谈恋爱》系列中的女主角。富樫勇太的同班同学兼女朋友。父亲的突然离世，令她至今无法接受这个事实。正在她最痛苦无助的时候，遇上了中二的富樫勇太。她相信父亲在“不可视境界线”另端的平行世界，为寻找“不可视境界线”而患上中二病。")
st.write("性格特点因受富樫勇太的感染，因此成为了中二病患者。无论是日常生活还是在校园内都会毫无忌惮的做出一些夸张的行为。对于姐姐（圣调理人）十分惧怕")
st.write("相貌衣着右眼戴着金色的彩瞳，并总是戴着眼罩，左手则绑着绷带，是个身材娇小、皮肤白皙的美少女，会像是小学生一样穿暴走鞋。制服下是哥特式腰带和黑色的过膝长袜。私服则是暗Girl系的时尚服装。被一色评价为“冰山系的面瘫娇小美少女” 。")

# 图片
st.image("./resources/caef76094b36acaf512c4dae75d98d1000e99c90.webp")

# 音频
st.audio("./resources/茶太 - だんご大家族.mp3")

# 视频
st.video("./resources/世界很温柔—《龙族》上杉绘梨衣.mp4")

# logo
st.logo("./resources/微信图片_20260715222041_52_58.jpg")

# 表格
st.table({
    "姓名": ["小鸟游六花", "富樫勇太", "一色诚"],
    "性别": ["女", "男", "男"],
    "年龄": [17, 17, 17],
    "爱好": ["中二病", "中二病", "中二病"]
})

# 输入框
# 普通文本输入框
name = st.text_input("请输入你的名字：", "小鸟游六花")
st.write(f"你好，{name}！欢迎来到Streamlit入门示例。")
# 密码输入框
password = st.text_input("请输入密码：", type="password")
st.write(f"你输入的密码是：{password}")

# 单选按钮
ga = st.radio("请选择你的性别：", ["男", "女","未知"],index=2)
st.write(f"你选择的性别是：{ga}")
# 4.在命令行中运行streamlit run 文件名.py来启动Web应用