from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice','')
        if selected_choice_id.isdigit():
            choice = get_object_or_404(Choice, pk=selected_choice_id)
            choice.votes += 1
            choice.save()
    context = {'question': question}
    return render(request, 'polls/poll.html', context)
