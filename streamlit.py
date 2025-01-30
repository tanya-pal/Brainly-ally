import streamlit as st
from datetime import datetime

# Function to format date
def format_date(date):
    return f"{date.hour:02d}:{date.minute:02d}"

# Streamlit app
def main():
    st.title("Mental Health Chatbot")

    st.markdown(
        """
        <style>
            .msger {
                max-width: 800px;
                margin: auto;
            }
            .msger-header {
                text-align: center;
                padding: 15px;
                background: #f9f9f9;
            }
            .msger-header-title {
                font-size: 24px;
                font-weight: bold;
            }
            .msger-chat {
                border: 1px solid #ccc;
                padding: 15px;
                max-height: 500px;
                overflow-y: scroll;
            }
            .msger-inputarea {
                display: flex;
                margin-top: 15px;
            }
            .msger-input {
                flex: 1;
                padding: 10px;
            }
            .msger-send-btn {
                padding: 10px;
                margin-left: 10px;
            }
            .msg {
                display: flex;
                margin-bottom: 20px;
            }
            .left-msg {
                justify-content: flex-start;
            }
            .right-msg {
                justify-content: flex-end;
            }
            .msg-img {
                width: 40px;
                height: 40px;
                background-size: cover;
                border-radius: 50%;
                margin-right: 10px;
            }
            .msg-bubble {
                flex: 1;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                background-color: #fff;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Initial message
    st.markdown(
        """
        <section class="msger">
            <header class="msger-header">
                <div class="msger-header-title">
                    <i class="fas fa-love"></i> BRAINY ALLY <i class="fas fa-love"></i>
                </div>
            </header>
            <main class="msger-chat">
                <div class="msg left-msg">
                    <div class="msg-img" style="background-image: url(static/img/mhcicon.png)"></div>
                    <div class="msg-bubble">
                        <div class="msg-info">
                            <div class="msg-info-name">MentlHealthBot</div>
                            <div class="msg-info-time"><time id="clock"></time></div>
                        </div>
                        <div class="msg-text">
                            Welcome to MentlHealthBot, a safe and supportive space where you can share your thoughts and feelings without fear of judgement.
                        </div>
                    </div>
                </div>
            </main>
            <form class="msger-inputarea">
                <input type="text" class="msger-input" id="textInput" placeholder="Enter your message...">
                <button type="submit" class="msger-send-btn">Send</button>
            </form>
        </section>
        <script>
            function updateTime() {
                var now = new Date();
                var hours = now.getHours();
                var minutes = now.getMinutes();
                var timeString = hours + ':' + minutes;
                document.getElementById('clock').textContent = timeString;
            }
            setInterval(updateTime, 1000);
        </script>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <script>
            const msgerForm = get(".msger-inputarea");
            const msgerInput = get(".msger-input");
            const msgerChat = get(".msger-chat");
            const BOT_IMG = "static/img/mhcicon.png";
            const PERSON_NAME = "You";
            const BOT_NAME = "Chat Bot";
            msgerForm.addEventListener("submit", event => {
                event.preventDefault();
                const msgText = msgerInput.value;
                if (!msgText) return;
                appendMessage(PERSON_NAME, msgText, "right");
                msgerInput.value = "";
                botResponse(msgText);
            });
            function appendMessage(name, text, side) {
                const msgHTML = `
                    <div class="msg ${side}-msg">
                        <div class="msg-img" style="background-image: url(static/img/person.png)"></div>
                        <div class="msg-bubble">
                            <div class="msg-info">
                                <div class="msg-info-name">${name}</div>
                                <div class="msg-info-time">${formatDate(new Date())}</div>
                            </div>
                            <div class="msg-text">${text}</div>
                        </div>
                    </div>
                `;
                msgerChat.insertAdjacentHTML("beforeend", msgHTML);
                msgerChat.scrollTop += 500;
            }
            function botResponse(rawText) {
                // Simulate bot response
                const msgText = "Bot response goes here.";
                appendMessage(BOT_NAME, msgText, "left");
            }
            function get(selector, root = document) {
                return root.querySelector(selector);
            }
            function formatDate(date) {
                const h = "0" + date.getHours();
                const m = "0" + date.getMinutes();
                return `${h.slice(-2)}:${m.slice(-2)}`;
            }
        </script>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
