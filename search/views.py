from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from catalog.models import Author

class ESearchView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        context = {}
        question = request.GET.get('q')
        if question is not None:
            search_author = Author.objects.filter(last_name__icontains=question)
            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_author, 10)
            page = request.GET.get('page')
            try:
                context['author_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['author_lists'] = current_page.page(1)
            except EmptyPage:
                context['author_lists'] = current_page.page(current_page.num_pages)

        return render(request, template_name=self.template_name, context=context)