import os
import requests
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis .env

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
MODEL = "tiiuae/falcon-7b-instruct"  # gratuit et léger

def query_huggingface(prompt):
    API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except:
            return "Désolé, une erreur s'est produite."
    return "Erreur API Hugging Face."

def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            answer = query_huggingface(question.question_text)
            question.answer_text = answer
            question.save()
            return redirect('index')
    else:
        form = QuestionForm()

    questions = Question.objects.order_by('-created_at')[:5]
    return render(request, 'qa/index.html', {'form': form, 'questions': questions})
