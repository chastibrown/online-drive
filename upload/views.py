from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy, reverse

from .forms import FileForm, RenameForm
from .models import File



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {
        'files': files
    })

# class FileListView(ListView):
#     model = File
#     template_name = 'class_file_list.html'
#     context_object_name = 'files'



def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {
        'form': form
    })


class RenameFileView(UpdateView):
    model = File
    form_class = RenameForm
    template_name = 'rename.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('file_list')


    

def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')




class UploadFileView(CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('class_file_list')
    template_name = 'upload_File.html'

