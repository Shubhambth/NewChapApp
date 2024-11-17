from django.shortcuts import render , get_object_or_404 ,redirect
from .models import ChatGroup , GroupMessage
from django.contrib.auth.decorators import login_required
from .forms import ChatmessageCreateForm




def chat(request):
    chat_group  = get_object_or_404(ChatGroup,group_name="public-chat")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()

    if request.method == 'POST':
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message':message, 
                'user' : request.user,
            }
            return render(request,'pchat.html',context)
    return render(request,'chat.html' ,{'chat_messages': chat_messages , 'form':form})








