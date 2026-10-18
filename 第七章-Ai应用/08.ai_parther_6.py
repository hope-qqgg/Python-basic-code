# 删除会话消息
import streamlit as st
import os

from openai import OpenAI
import datetime
import json

print("---------------> 重新执行此文件，渲染展示此页面")

# 以脚本所在目录为基准，避免启动目录不同导致读写到别处的 sessions 目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SESSIONS_DIR = os.path.join(BASE_DIR, "sessions")


# 生成一个不重复的会话ID
def generate_session_id():
    while True:
        new_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if not os.path.exists(os.path.join(SESSIONS_DIR, f"{new_id}.json")):
            return new_id

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
    # 没有消息就不保存，避免生成空的会话文件
    if st.session_state.session_id and st.session_state.messages:
        # 构建新的会话对象
        session_data = {
            "nickname": st.session_state.nick_name,
            "description": st.session_state.description,
            "session_id": st.session_state.session_id,
            "messages": st.session_state.messages
        }
        # 如果 sessions 目录不存在，则创建
        os.makedirs(SESSIONS_DIR, exist_ok=True)
        # 保存会话
        file_path = os.path.join(SESSIONS_DIR, f"{st.session_state.session_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

# 加载所有的会话
def load_sessions():
    session_list = []
    # 加载 sessions 目录下的文件（名称即时间戳，倒序排列，最新的在最上面）
    if os.path.exists(SESSIONS_DIR):
        file_list = os.listdir(SESSIONS_DIR)
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

# 加载指定会话信息
def load_session(session_name):
    # 异常处理
    try:
        # 路径不要以 / 开头，否则在 Windows 上会被当成盘符根目录（如 D:\sessions）
        file_path = os.path.join(SESSIONS_DIR, f"{session_name}.json")
        if os.path.exists(file_path):
            # 读取会话数据
            with open(file_path, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
                st.session_state.messages = session_data.get("messages", [])
                st.session_state.nick_name = session_data.get("nickname", "宵宫")
                st.session_state.description = session_data.get("description", "一个活泼开朗的小女孩")
                st.session_state.session_id = session_data.get("session_id", session_name)
            return True
        st.error("会话文件不存在！")
        return False
    except Exception as e:
        print("加载会话失败：", e)
        st.error('加载会话失败！！！')
        return False

# 删除会话信息函数
def delete_session(session_name):
    # 异常处理
    try:
        file_path = os.path.join(SESSIONS_DIR, f"{session_name}.json")
        if os.path.exists(file_path):
            os.remove(file_path) # 删除文件
            # 如果删除的是当前会话，则需要更新消息列表
            if session_name == st.session_state.session_id:
                st.session_state.messages = []
                st.session_state.session_id = generate_session_id()
        return True
    except Exception as e:
        print("删除会话失败：", e)
        st.error('删除会话失败！！！')
        return False


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
    st.session_state.session_id = generate_session_id()

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
        # 1.保存当前会话（内部会判断，只有存在消息时才写文件）
        save_session()

        # 2.创建一个空的会话
        st.session_state.messages = []
        st.session_state.session_id = generate_session_id()
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
                if load_session(session):
                    st.rerun()
        with col2:
            # 删除会话消息
            if st.button("", width="stretch", icon="❌️", key=f"del_{session}"):
                if delete_session(session):
                    st.rerun()

    # Ai信息
    st.subheader("Ai信息")
    # 昵称输入框（改用 key 与 session_state 双向绑定，加载会话后能立刻刷新）
    st.text_input("昵称", placeholder="请输入昵称", key="nick_name")
    # 性格描述输入框
    st.text_area("请输入性格描述", placeholder="请输入性格描述", key="description")

# 输入框
prompt = st.chat_input("你好，我是纳兰宵宫，滴嘟滴嘟~")
if prompt: # 字符串会自动转换为布尔值，非空字符串为True
    with st.chat_message("user"):
        st.write(prompt)
    print("---------------> 调用ai大模型，提示词：", prompt) # 在控制台输出提示词

    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})
    save_session()  # 用户消息先落盘，即使后面接口异常也不会丢失

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
    save_session()  # 关键：把本轮对话写入会话文件
    st.rerun()  # 刷新页面，让会话历史里立即出现当前会话
