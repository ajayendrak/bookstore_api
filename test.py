


# lenght = (len(filtered_user))
#                 print(f'48--------------------{lenght}')
#                 user = 0 
#                 for user in range(0,lenght):
#                     print(f'51-----------------{filtered_user[user]}')
#                     has_biodata = check_user_details(filtered_user[user])
#                     has_photoes = check_user_photoes(filtered_user[user])
#                     print(f'36----------------{filtered_user[user]}--{has_biodata}')
#                     print(f'37----------------{filtered_user[user]}--{has_photoes}')
#                     if not has_biodata and not has_photoes:
#                         filtered_user.remove((filtered_user[user]))
#                     # else:
                        
#                     user = user + 1
#                 print()


# class UnMatchAPIView(APIView): 
# 	permission_classes = [IsAuthenticated]

# 	def post(self, request):
# 		logged_user = request.user
# 		unmatch_user_id = request.data.get('user_id')
# 		reason = request.data.get('reason')
# 		if reason:
# 			pass
# 		else:
# 			reason = ""

# 		unmatch_user = User.objects.get(pk = unmatch_user_id)

# 		logged_user_connection = ConnectedContact.objects.filter(user = logged_user).all()
# 		if logged_user_connection:
# 			for connection in logged_user_connection:
# 				if unmatch_user in connection.friend.all():
# 					connection.delete()

# 		unmatch_user_connection = ConnectedContact.objects.filter(user = unmatch_user).all()
# 		if unmatch_user_connection:
# 			for connection in unmatch_user_connection:
# 				if logged_user in connection.friend.all():
# 					connection.delete()

# 		unmatch_object = UnMatchUser.objects.create(unmatched_by = logged_user, unmatched_user = unmatch_user, unmatch_reason = reason)
# 		unmatch_object.save()






# class UnMatchUser(models.Model):
#     unmatched_user = models.ManyToManyField(User, related_name='unmatched_user',null = True, blank = True)
#     unmatched_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unmatched_by', limit_choices_to={'is_active': 'True'})
#     reason = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
#     updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)

#     class Meta:
#         ordering = ["id"]

#     def __str__(self):
#         return str(self.id)




# path('unmatch', UnMatchAPIView.as_view(), name = "unmatch"),










# class CompatibaleProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserPreferenceSerilizer
#     pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

#     def post(self, request):
#         user = self.request.user
#         user_biodata = BioData.objects.filter(user = user)
#         if user_biodata:
#             user_biodata = user_biodata.last()
#         if request.data:
#             compatible_users = fetch_compatible_users(user, user_biodata, request)
#             page = self.paginate_queryset(compatible_users)
#             if page is not None:
#                 compatible_user_prefrence = UserPreferenceSerilizer(page, many=True).data
#                 return self.get_paginated_response(compatible_user_prefrence)

#             compatible_user_prefrence = UserPreferenceSerilizer(compatible_users, many=True).data
#             return Response(compatible_user_prefrence)
#         else:
#             user_gender = user.gender
#             user_preferences = User.objects.filter(~Q(gender = user_gender)).order_by('id')
#             filtered_user = calculate_general_user_prefrence(user_preferences, user, user_biodata)
#             page = self.paginate_queryset(filtered_user)
#             if page is not None:
#                 user_genral_prefrence = UserPreferenceSerilizer(page, many=True).data
#                 return self.get_paginated_response(user_genral_prefrence)
#             user_genral_prefrence = UserPreferenceSerilizer(filtered_user, many = True).data
#             return Response(user_genral_prefrence)

#     @property
#     def paginator(self):
#         """
#         The paginator instance associated with the view, or `None`.
#         """
#         if not hasattr(self, '_paginator'):
#             if self.pagination_class is None:
#                 self._paginator = None
#             else:
#                 self._paginator = self.pagination_class()
#         return self._paginator

#     def paginate_queryset(self, queryset):
#         """
#         Return a single page of results, or `None` if pagination is disabled.
#         """
#         if self.paginator is None:
#             return None
#         return self.paginator.paginate_queryset(queryset, self.request, view=self)

#     def get_paginated_response(self, data):
#         """
#         Return a paginated style `Response` object for the given output data.
#         """
#         assert self.paginator is not None
#         return self.paginator.get_paginated_response(data)