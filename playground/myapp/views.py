from django.shortcuts import render
from openai import OpenAI

client = OpenAI()

history = []

def playground_view(request):
    output_text = ""
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        global history
        history.append({"role": "user", "content": input_text})
        response = client.responses.create(
            model="gpt-4o",
            input=history,
        )
        history += [{"role": element.role, "content": element.content} for element in response.output]
        output_text = response.output_text

    return render(request, 'playground.html', {'output_text': output_text})