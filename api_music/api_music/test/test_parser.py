# group_info = {
#     'month_listeners': values.get('month_listeners'),
#     'name': values.get('name')
# }
# group_id = self.env['groups'].create(group_info)
#
#
# def _get_artist(artist):
#     artist_info = {
#         'name': artist.get('name'),
#         'age': artist.get('age'),
#         'sex': artist.get('sex'),
#         'country': artist.get('country'),
#         'groups': [(6, 0, group_id.ids or False)]
#     }
#     artists_id = self.env['artists'].create(artist_info)
#
#     def _get_singles(single):
#         album_or_single_info = {
#             'album_and_single': 'single',
#             'artists': [(6, 0, artists_id.ids or False)],
#             'groups': [(6, 0, group_id.ids or False)]
#         }
#         single_id = self.env['albums.singles'].create(album_or_single_info)
#         single_info = {
#             'name': single.get('name'),
#             'duration': single.get('duration'),
#             'listeners': single.get('listeners'),
#             'author': [(6, 0, artists_id.ids or False)],
#             'albums_and_singles': [(4, single_id.id)],
#             'groups': [(6, 0, group_id.ids or False)]
#         }
#         self.env['songs'].create(single_info)
#
#     try:
#         for single in values['singles']['songs']['song']:
#             _get_singles(single)
#     except:
#         pass
#
#
# for artist in values['artists']['artist']:
#     _get_artist(artist)
#
# return values