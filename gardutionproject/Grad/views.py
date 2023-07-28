from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        select_value = request.POST.get('option')
        input1_value = request.POST.get('input1')
        input2_value = request.POST.get('input2')

        # Perform any necessary operations or calculations with the input values
        if select_value == 'option1':
            # Convert input1_value to an integer and increment by 1
            output_value = "ahmed option1"
            
        elif select_value == 'option2':
            output_value = "ahmad option2"

        elif select_value == 'option3':
            output_value = "ahmad option3"

        elif select_value == 'option4':
            output_value = "ahmad option4"

        elif select_value == 'option5':
            output_value = "ahmad option5"

        elif select_value == 'option6':
            output_value = "ahmad option6"

        elif select_value == 'option7':
            output_value = "ahmad option7"

        elif select_value == 'option8':
            output_value = "ahmad option8"
    else:
        output_value = None

    context = {'output': output_value} # output_value will be prented on the screen 
    return render(request, 'myapp/home.html', context)
