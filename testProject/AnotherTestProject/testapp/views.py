from django.shortcuts import render_to_response


def test_chat(request):
    return render_to_response('test.html', {})
