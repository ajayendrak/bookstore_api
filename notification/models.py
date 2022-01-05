from django.db import models
from user.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class BookNotification(models.Model):
	title = models.CharField(max_length=512, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	notification = models.TextField(max_length=512)
	is_seen = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.title}"

	def save(self, *args, **kwargs):
		channel_layer = get_channel_layer()
		notification_obj = BookNotification.objects.last()
		data = 	{'notification': f"50% OFF Sale : {notification_obj.title}"}

		async_to_sync(channel_layer.group_send)(
			'chat_consumer_group', {
				'type' : 'send_notification',
				'value' : json.dumps(data)
			})
		super(BookNotification, self).save(*args,**kwargs)
