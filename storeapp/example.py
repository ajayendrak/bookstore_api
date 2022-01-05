# premium_subscription = PremiumSubscription.objects.get(user = user)
# 		ending_date = premium_subscription.end_date
# 		today_date = datetime.today()
# 		if today_date > ending_date:
# 			if connected_users:
# 				connected_users = connected_users.last()
# 				if len(connected_users.friend.all())>=3:
# 					return Response({"message":"you can able to connect 3 people at a time.", "premium subscription": "false"})
# 				else:
# 					all_connected_users = connected_users.friend.all()
# 					if connect_user in all_connected_users:
# 						return Response({"message":f"you are already connected with {connect_user.first_name} {connect_user.last_name}"})
# 					connected_users.friend.add(connect_user)
# 					connected_users.save()
# 					return Response({"message":f"you are successfully connected with {connect_user.first_name} {connect_user.last_name}"})
# 			else:
# 				connected_users = ConnectedContact.objects.create(user = requested_user)
# 				connected_users.friend.add(connect_user)
# 				connected_users.save()
# 				return Response({"message":f"you are successfully connected with {connect_user.first_name} {connect_user.last_name}"})
# 		else:
# 			connected_users = ConnectedContact.objects.create(user = requested_user)
# 			connected_users.friend.add(connect_user)
# 			connected_users.save()
# 			return Response({"message":f"you are successfully connected with {connect_user.first_name} {connect_user.last_name}"})





# try:
# 				#############
# 				premium_subscription = PremiumSubscription.objects.filter(user = requested_user)
# 				if premium_subscription:
# 					premium_subscription = premium_subscription.last()
# 					ending_date = premium_subscription.end_date.strftime('%y-%m-%d')
# 					today_date = datetime.today().strftime('%y-%m-%d')
# 					if today_date > ending_date:
# 						request_obj = ContactRequest.objects.filter(user = requested_user)
# 						if request_obj:
# 							request_obj=request_obj.last()
# 							if request_obj.friend:
# 								request_sents = request_obj.friend.all()
# 								if len(request_sents) >= 10 :
# 									return Response({"error":"you can send only 10 request without premium subscription", "status" : False})
# 				else:
# 					request_obj = ContactRequest.objects.filter(user = requested_user).last()
# 					request_sents = request_obj.friend.all()
# 					if len(request_sents) >= 10 :
# 						return Response({"error":"you can send only 10 request without premium subscription", "status" : False})
# 					# return Response({"error":"you have to pay first", "status" : False})
				
# 				##############













# 				##############################################################
# 				premium_subscription = PremiumSubscription.objects.get(user = user)
# 				ending_date = premium_subscription.end_date
# 				today_date = datetime.today()
# 				if today_date > ending_date:
# 					if sent_requests < 10:
						
# 						if connected_users:
# 							if connected_users.last().friend:
# 								no_of_connections = len(connected_users.last().friend.all())
# 								if len(connected_users.last().friend.all())>=3:
# 									return Response({"message":"you can able to connect 3 people at a time.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections, "premium subscription": "false"})
# 							else:
# 								pass
# 				if requested_user == receiver_user:
# 					return Response({"message":"you can't send connection request to your self.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 				contact = ContactRequest.objects.filter(user = requested_user)
# 				if contact:
# 					contact = contact.last()
# 					contact_friends = contact.friend
# 					if contact_friends:
# 						all_contact_friends = contact_friends.all()
# 						if receiver_user in all_contact_friends:
# 							return Response({"message":"you have already sent connection request.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 						else:
# 							contact.friend.add(receiver_user)
# 							contact.save()
# 							if message:
# 								contact.message = message
# 								contact.save()
# 							return Response({"message":f"your request sent successfully to {receiver_user.first_name}", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 				else:
# 					contact = ContactRequest.objects.create(user = requested_user)
# 					contact.friend.add(receiver_user)
# 					contact.save()
# 					if message:
# 						contact.message = message
# 						contact.save()
# 					return Response({"message":f"your request sent successfully to {receiver_user.first_name}", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 			except Exception as e:
# 				print(e)
# 		else:
# 			return Response({"has_biodata":has_biodata, "has_photoes":has_photoes})
		










# 	def post(self, request, user_id):
# 		message = request.data['message']
# 		requested_user = request.user
# 		print(f'29---------------------------{requested_user}')
# 		no_of_connections = 0
# 		receiver_user = User.objects.get(pk = user_id)
# 		has_biodata = check_user_details(requested_user)
# 		has_photoes = check_user_photoes(requested_user)
# 		if has_biodata and has_photoes:
# 			try:
# 				#############
# 				premium_subscription = PremiumSubscription.objects.filter(user = requested_user)
# 				if premium_subscription:
# 					print(f'39----------------')
# 					premium_subscription = premium_subscription.last()
# 					ending_date = premium_subscription.end_date.strftime('%y-%m-%d')
# 					today_date = datetime.today().strftime('%y-%m-%d')
# 					if today_date > ending_date:
# 						print(f'43----------------')
# 						request_obj = ContactRequest.objects.filter(user = requested_user)
# 						if request_obj:
# 							request_obj=request_obj.last()
# 							print(f'46-------------{request_obj}')
# 							print(f'47-------------{request_obj.friend}')
# 							print(f'46-------------{request_obj.friend.all()}')
# 							if request_obj.friend:
# 								request_sents = request_obj.friend.all()
# 								if len(request_sents) >= 10 :
# 									return Response({"error":"you can send only 10 request without premium subscription", "status" : False})
# 				else:
# 					print(f'54----------------')
# 					request_obj = ContactRequest.objects.filter(user = requested_user).last()
# 					print(f'56----------------')
# 					if request_obj.friend:

# 						request_sents = request_obj.friend.all()
# 						if len(request_sents) >= 10 :
# 							print(f'63----------------')
# 							return Response({"error":"you can send only 10 request without premium subscription", "status" : False})
# 					# return Response({"error":"you have to pay first", "status" : False})
				
# 				##############



# 				connected_users = ConnectedContact.objects.filter(user = requested_user)
# 				if connected_users:
# 					if connected_users.last().friend:
# 						no_of_connections = len(connected_users.last().friend.all())
# 						print(f'75----------------')
# 						if len(connected_users.last().friend.all())>=3:
# 							return Response({"message":"you can able to connect 3 people at a time.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 					else:
# 						pass
# 				if requested_user == receiver_user:
# 					print(f'81----------------')
# 					return Response({"message":"you can't send connection request to your self.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 				contact = ContactRequest.objects.filter(user = requested_user)
# 				if contact:
# 					contact = contact.last()
# 					contact_friends = contact.friend
# 					print(f'87----------------')
# 					if contact_friends:
# 						all_contact_friends = contact_friends.all()
# 						if receiver_user in all_contact_friends:
# 							print(f'91----------------')
# 							return Response({"message":"you have already sent connection request.", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 						else:
# 							contact.friend.add(receiver_user)
# 							contact.save()
# 							print(f'96----------------')
# 							if message:
# 								contact.message = message
# 								contact.save()
# 								print(f'99----------------')
# 							return Response({"message":f"your request sent successfully to {receiver_user.first_name}", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 				else:
# 					contact = ContactRequest.objects.create(user = requested_user)
# 					contact.friend.add(receiver_user)
# 					contact.save()
# 					if message:
# 						print(f'106----------------')
# 						contact.message = message
# 						contact.save()
# 					return Response({"message":f"your request sent successfully to {receiver_user.first_name}", "has_biodata":has_biodata, "has_photoes":has_photoes, "no_of_connections":no_of_connections})
# 			except Exception as e:
# 				print(f'85----------------{e}')
# 				return Response({"error":"something went wrong."})
# 		else:
# 			return Response({"has_biodata":has_biodata, "has_photoes":has_photoes})
		
