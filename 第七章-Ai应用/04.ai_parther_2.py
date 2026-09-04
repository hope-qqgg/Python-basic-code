# 添加会话记忆功能
import streamlit as st
import os
from openai import OpenAI

print("---------------> 重新执行此文件，渲染展示此页面")

# 设置页面的配置项
st.set_page_config(
    page_title="ai智能伴侣",
    page_icon="🥰",
    # 页面布局
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("ai智能伴侣")

# logo
st.logo("./resources/微信图片_20260715222041_52_58.jpg")

# 系统提示词
system_prompt = "你是一名可爱的Ai助理，你的名字叫宵宫，请你用温柔的语气回答用户问题,可以适当的使用颜文字"

# 初始化聊天消息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 展示聊天消息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 创建与Ai大模型交互的客户端对象（DEEPSEEK_API_KEY环境变量的名字，值是API_KEY）
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

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
            {"role": "system", "content": system_prompt},
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
    response_message = st.empty() # 创建一个空的元素来显示AI的回复
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.write(full_response)
    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})
