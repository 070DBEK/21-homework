from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskForm
from .models import Task
import logging
logger = logging.getLogger(__name__)


class TaskListView(generic.ListView):
    model = Task
    template_name = 'todo/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        if search:
            logger.debug(f"Search filter applied: {search}")
            queryset = queryset.filter(title__icontains=search)
        priority = self.request.GET.get('priority')

        if priority:
            logger.debug(f"Priority filter applied: {priority}")
            queryset = queryset.filter(priority=priority)

        status = self.request.GET.get('status')
        if status:
            logger.debug(f"Status filter applied: {status}")
            queryset = queryset.filter(status__iexact=status)

        order_by = self.request.GET.get('order_by')
        if order_by:
            logger.debug(f"Order by filter applied: {order_by}")
            if order_by in ['due_date', 'priority', 'status']:
                queryset = queryset.order_by(order_by)

        logger.debug(f"Final queryset: {queryset.query}")
        return queryset



class TaskFormView(generic.FormView):
    template_name = 'todo/form.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        pk = self.kwargs.get('pk')
        if pk:
            try:
                task = Task.objects.get(pk=pk)
                kwargs['instance'] = task
            except Task.DoesNotExist:
                logger.error(f"Task with pk={pk} does not exist.")
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'todo/detail.html'
    context_object_name = 'task'


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:list')
