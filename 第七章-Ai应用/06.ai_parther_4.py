# 保存会话
import streamlit as st
import os
from openai import OpenAI
import datetime
import json


print("---------------> 重新执行此文件，渲染展示此页面")

# 设置页面的配置项
st.set_page_config(
    page_title="可爱的小废物",
    page_icon="🥰",
    # 页面布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 保存会话函数
def save_session():
    if st.session_state.session_id:
        # 构建新的会话对象
        session_data = {
            "nickname": st.session_state.nick_name,
            "description": st.session_state.description,
            "session_id": st.session_state.session_id,
            "messages": st.session_state.messages
        }
        # 如果sessions 文件存在，则追加，否则创建
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        # 保存会话
        with open(f"sessions/{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载所有的会话
def load_sessions():
    session_list = []
    # 加载sessions目录下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    return session_list

# 大标题
st.title("Ai聊天")

# logo
st.logo("🥰")

# 系统提示词
system_prompt = """
    你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
        1．每次只回1条消息
        2．禁止任何场景或状态描述性文字
        3．匹配用户的语言
        4．回复简短，像微信聊天一样
        5.有需要的话可以用❤等emoji表情和颜文字
        6.用符合伴侣性格的方式对话
        7．回复的内容，要充分体现伴侣的性格特征
        伴侣性格：
            － %s
        你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天消息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "宵宫"
# 性格
if 'description' not in st.session_state:
    st.session_state.description = "一个活泼开朗的小女孩"

# 会话标识
if 'session_id' not in st.session_state:
    st.session_state.session_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 展示聊天消息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 创建与Ai大模型交互的客户端对象（DEEPSEEK_API_KEY环境变量的名字，值是API_KEY）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 侧边栏
with st.sidebar:
    # 会话信息
    st.subheader("Ai控制面板")

    # 新键会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        # 1.保存当前会话
        save_session()

        # 2.创建一个空的会话
        if st.session_state.messages: # 如果聊天消息非空，True；否则，False
            st.session_state.messages = []
            st.session_state.session_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            save_session()
            st.rerun()  # 重新运行页面(刷新页面)

    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        # st.button(session, width="stretch", icon="📁")
        # st.button("", width="stretch", icon="❌️")
        col1,col2 = st.columns([4,1])
        with col1:
            # 加载会话消息
            if st.button(session, width="stretch", icon="📁", key=f"load_{session}"):
                pass
        with col2:
            # 删除会话消息
            if st.button("", width="stretch", icon="❌️", key=f"del_{session}"):
                pass

    # Ai信息
    st.subheader("Ai信息")
    # 昵称输入框
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    # 性格描述输入框
    description = st.text_area("请输入性格描述", placeholder="请输入性格描述", value=st.session_state.description)
    if description:
        st.session_state.description = description

# 输入框
prompt = st.chat_input("你好，我是纳兰宵宫，滴嘟滴嘟~")
if prompt: # 字符串会自动转换为布尔值，非空字符串为True
    with st.chat_message("user"):
        st.write(prompt)
    print("---------------> 调用ai大模型，提示词：", prompt) # 在控制台输出提示词

    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用ai大模型
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.description)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # # 打印AI大模型的回复(非流式输出)
    # print("<--------------- 调用ai大模型返回的结果",response.choices[0].message.content) # 在控制台输出AI大模型的回复
    # with st.chat_message("assistant"):
    #     st.write(response.choices[0].message.content) # 在网也的回答
    # # 保存大模型返回的结果
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 打印AI大模型的回复(流式输出)
    with st.chat_message("assistant"):
        response_message = st.empty()  # 创建一个空的元素来显示AI的回复
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response += content
                response_message.write(full_response)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
