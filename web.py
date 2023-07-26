import streamlit as st
import functions as fc


todos = fc.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    fc.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my ToDo App")
st.write("This app was created to improve productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')