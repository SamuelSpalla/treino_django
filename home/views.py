from django.shortcuts import render

from django.views import View


class Base(View):
    template_name = 'home/index.html'
    title = ''

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self):
        context = {
            'title': self.title,
            'headers': self.get_header(),
            'data': self.get_data(),
            'headers2': self.get_header_animals(),
            'data2': self.get_data_animals(),
            'exibir_tabela': self.get_condicional_table()
        }
        return context
    
    def get_header(self):
        return []
    
    def get_data(self):
        return []
    
    def get_header_animals(self):
        return []
    
    def get_data_animals(self):
       return []
    
    def get_condicional_table(self):
        return True
    

class Home(Base):
    title = 'Home'
    
    def get_header(self):
        return ['Nome', 'Idade', 'CPF']
    
    def get_data(self):
        data = [
            ['Samuel', 21, '123'],
            ['Deivid', 23, '213'],
            ['Lucas', 24, '321']
        ]
        return data
    
    def get_header_animals(self):
        return ['Nome', 'Idade', 'Raça']
    
    def get_data_animals(self):
        data2 = [
            ['Diana', 4, 'Pastor'],
            ['Rex', 2, 'Pitbull'],
            ['Apollo', 6, 'Labrador']
        ]
        return data2
    
    def get_condicional_table(self):
        return True
        
class Alternative(Base):
    title = 'Alternative'
    
    def get_header(self):
        return ['Nome', 'Idade', 'CPF']
    
    def get_data(self):
        data = [
            ['Pedro', 23, '123'],
            ['Thiago', 24, '213'],
            ['Alvaro', 24, '321']
        ]
        return data
    
    def get_header_animals(self):
        return ['Nome', 'Idade', 'Raça']
    
    def get_data_animals(self):
        data2 = [
            ['Diana', 4, 'Pastor'],
            ['Rex', 2, 'Pitbull'],
            ['Apollo', 6, 'Labrador']
        ]
        return data2
    
    def get_condicional_table(self):
        return False