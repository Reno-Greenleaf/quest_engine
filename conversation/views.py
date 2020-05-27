from django.shortcuts import render
from django.views import View


class ExchangeEditor(View):
	def get(self, request):
		return render(request, 'conversation/exchange-editor.html')