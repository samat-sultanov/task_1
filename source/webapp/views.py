from django.shortcuts import render


def math_numbers(request):
    if request.method == 'GET':
        return render(request, 'user_input.html')
    else:
        context = {
            'first_num': request.POST.get('first_num'),
            'second_num': request.POST.get('second_num'),
            'user_math': request.POST.get('user_math')
        }
        num_one, num_two = int(context['first_num']), int(context['second_num'])
        if context['user_math'] is None:
            error_message = 'Error: select one of the options (add, subtract, multiply, divide)'
            math_output = ''
        elif context['user_math'] == '/' and num_two == 0:
            error_message = 'Error: you can not divide number by zero'
            math_output = ''
        elif context['user_math'] is not None:
            if context['user_math'] == '+':
                math_output = num_one + num_two
            elif context['user_math'] == '-':
                math_output = num_one - num_two
            elif context['user_math'] == '/' and num_two != 0:
                math_output = num_one / num_two
            elif context['user_math'] == '*':
                math_output = num_one * num_two
            error_message = ''

        context = {
            'first_num': request.POST.get('first_num'),
            'second_num': request.POST.get('second_num'),
            'user_math': request.POST.get('user_math'),
            'math_output': math_output,
            'error_message': error_message
        }

        return render(request, 'math_result.html', context)