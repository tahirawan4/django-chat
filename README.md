
Chat
____

Chat is a simple Django app to conduct Web-socket based chat.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "channels" and "chat" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
        'channels',
    ]

2. Include the chat URLconf in your project urls.py like this::

    url(r'^chat/', include('chat.urls')),

3. Add Following to your settings File

	CHANNEL_LAYERS = {
    	'default': {
        	'BACKEND': 'asgiref.inmemory.ChannelLayer',
        	'ROUTING': 'chat.routing.channel_routing',
    	},
	}


4. Start the development server and visit http://127.0.0.1:8000/chat/page


6. Dependencies

	bootstrap
	jquery
	pip install asgi-redis
	pip install channels==0.17.3
	pip install daphne==0.15.0

7. You can Include this module in any of your page just by writing following

	{% include 'chat_module.html' %}
