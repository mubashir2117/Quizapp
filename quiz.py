import streamlit as st
import random

st.set_page_config(page_title="Python Quiz", page_icon="🧠")
st.title("🧠 Python Quiz App")
st.write("Answer these Python questions and test your knowledge!")

quiz = [
    {"question": "What is the output of 3 + 2 * 2?", "options": ["5", "7", "10", "6"], "answer": "7"},
    {"question": "Which keyword is used to create a function?", "options": ["func", "def", "function", "lambda"], "answer": "def"},
    {"question": "Which data type is immutable?", "options": ["List", "Tuple", "Dictionary", "Set"], "answer": "Tuple"},
    {"question": "How do you start a comment in Python?", "options": ["//", "#", "/*", "<!--"], "answer": "#"},
    {"question": "What does len() do?", "options": ["Adds numbers", "Prints output", "Returns length", "None"], "answer": "Returns length"},
    {"question": "Valid variable name?", "options": ["1st_name", "first-name", "_first_name", "first name"], "answer": "_first_name"},
    {"question": "Correct way to create a list?", "options": ["{1,2,3}", "[1,2,3]", "(1,2,3)", "<1,2,3>"], "answer": "[1,2,3]"},
    {"question": "Operator for exponentiation?", "options": ["^", "**", "//", "%"], "answer": "**"},
    {"question": "Module for random numbers?", "options": ["math", "random", "time", "os"], "answer": "random"},
    {"question": "'Hello' * 3 outputs?", "options": ["HelloHelloHello", "Error", "Hello3", "3Hello"], "answer": "HelloHelloHello"},
    {"question": "Add item to list?", "options": ["add()", "append()", "insert()", "push()"], "answer": "append()"},
    {"question": "Python loop keyword?", "options": ["repeat", "while", "foreach", "loop"], "answer": "while"},
    {"question": "Handle exceptions with?", "options": ["try-catch", "try-except", "error-handling", "exception block"], "answer": "try-except"},
    {"question": "Syntax to define a class?", "options": ["class MyClass():", "define class MyClass:", "MyClass = class:", "class: MyClass"], "answer": "class MyClass():"},
    {"question": "Install packages with?", "options": ["pip install", "python get", "py install", "import install"], "answer": "pip install"},
    {"question": "Which of the following is not a keyword?", "options": ["if", "while", "goto", "return"], "answer": "goto"},
    {"question": "What is the output of bool(0)?", "options": ["True", "False", "0", "None"], "answer": "False"},
    {"question": "Which of the following is used to get input from user?", "options": ["cin", "input()", "get()", "read()"], "answer": "input()"},
    {"question": "What does 'break' do in a loop?", "options": ["Skips to next", "Ends loop", "Restarts loop", "None"], "answer": "Ends loop"},
    {"question": "How do you import a module?", "options": ["include module", "use module", "import module", "module()"], "answer": "import module"},
    {"question": "Which of these is a mutable data type?", "options": ["str", "tuple", "list", "int"], "answer": "list"},
    {"question": "Which operator is used for division that returns whole number?", "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "Which function converts string to integer?", "options": ["int()", "str()", "float()", "eval()"], "answer": "int()"},
    {"question": "What is the output of 5 % 2?", "options": ["2.5", "2", "1", "0"], "answer": "1"},
    {"question": "Which data type stores true or false?", "options": ["int", "bool", "str", "char"], "answer": "bool"},
    {"question": "Which statement is used to skip iteration in loop?", "options": ["pass", "continue", "break", "exit"], "answer": "continue"},
    {"question": "What is the default return type of input()?", "options": ["int", "str", "float", "bool"], "answer": "str"},
    {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<list>", "list", "ListType"], "answer": "<class 'list'>"},
    {"question": "What symbol is used for comments?", "options": ["#", "//", "/* */", "--"], "answer": "#"},
    {"question": "What is a lambda function?", "options": ["A named function", "A class", "An anonymous function", "A module"], "answer": "An anonymous function"},
    {"question": "Which function gives max of list?", "options": ["high()", "max()", "maximum()", "top()"], "answer": "max()"},
    {"question": "Which file extension is for Python?", "options": [".py", ".java", ".cpp", ".js"], "answer": ".py"},
    {"question": "Which statement handles exceptions?", "options": ["if", "try", "except", "try-except"], "answer": "try-except"},
    {"question": "What is the output of 4 ** 2?", "options": ["6", "8", "16", "10"], "answer": "16"},
    {"question": "Which of these is not a data type?", "options": ["int", "str", "bool", "real"], "answer": "real"},
    {"question": "What is the result of 10 // 3?", "options": ["3", "3.33", "4", "Error"], "answer": "3"},
    {"question": "How to define a tuple?", "options": ["[1,2]", "{1,2}", "(1,2)", "<1,2>"], "answer": "(1,2)"},
    {"question": "Which function shows output?", "options": ["write()", "echo()", "display()", "print()"], "answer": "print()"},
    {"question": "How to install streamlit?", "options": ["pip install streamlit", "install streamlit", "pip get streamlit", "py install streamlit"], "answer": "pip install streamlit"},
    {"question": "Which of these is a logical operator?", "options": ["=", "and", "&", "+"], "answer": "and"},
    {"question": "Which function returns list length?", "options": ["length()", "count()", "len()", "size()"], "answer": "len()"}
]

# Initialize session state
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(quiz, 40)
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False

# Current question
q = st.session_state.questions[st.session_state.q_index]

# Display question
st.subheader(f"Q{st.session_state.q_index + 1}: {q['question']}")
user_answer = st.radio("Select your answer:", q["options"], key=f"q{st.session_state.q_index}")

# Horizontal buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Submit", key="submit_btn") and not st.session_state.answered:
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer was: {q['answer']}")
        st.session_state.answered = True

with col2:
    if st.session_state.answered and st.button("➡️ Next", key="next_btn"):
        st.session_state.q_index += 1
        st.session_state.answered = False

        if st.session_state.q_index >= len(st.session_state.questions):
            st.balloons()
            st.subheader("🎉 Quiz Completed!")
            score = st.session_state.score
            total = len(st.session_state.questions)
            st.write(f"**Your Score: {score} / {total}**")

            if score == total:
                st.success("🏆 Perfect Score! You're a Python Pro!")
            elif score >= total // 2:
                st.info("👍 Good job! Keep going.")
            else:
                st.warning("💡 Keep practicing. You’ll improve!")

            if st.button("🔄 Restart Quiz"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        else:
            st.rerun()