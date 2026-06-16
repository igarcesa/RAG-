from graph import app_graph

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    result = app_graph.invoke({"question": question})

    print("\nAnswer:")
    print(result["answer"])