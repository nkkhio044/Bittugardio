import gradio as gr

def sun_bot(user_input):
    return f"☠️ Sun style reply: {user_input[::-1]}"

demo = gr.Interface(fn=sun_bot, inputs="text", outputs="text", title="☠️ Sun Bot")

# Vercel ke liye server_name aur port fix karna zaroori hai
demo.launch(server_name="0.0.0.0", server_port=5000)
