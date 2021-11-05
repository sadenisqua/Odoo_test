import xmltodict

from odoo import models, fields, api

import base64


class UploadFileWizzard(models.TransientModel):
    _name = 'upload.file.wizzard'
    # _inherit = ['upload.file']

    import_xml = fields.Binary()
    import_xml_name = fields.Char()

    def _parse_artist(self, values):
        artist_info = {
            'name': values.get('name'),
            'month_listeners': values.get('month_listeners'),
            'age': values.get('age'),
            'sex': values.get('sex'),
            'country': values.get('country')
        }

        artist_id = self.env['artists'].create(artist_info)

        def _parse_single(single_values):

            album_or_single_info = {
                'album_and_single': 'single',
                'artists': [(6, 0, artist_id.ids or False)]
            }
            single_id = self.env['albums.singles'].create(album_or_single_info)

            members = []
            string = ()

            try:
                for member in single['members']['member']:
                    members.append(member['name'])
                    string = ''.join(str(f'{x} ') for x in members)
            except:
                try:
                    members.append(single['members']['member']['name'])
                    string = ''.join(str(members)).replace("['", "").replace("']", "")
                except:
                    string = ''

            single_info = {
                'name': single_values.get('name'),
                'duration': single_values.get('duration'),
                'listeners': single_values.get('listeners'),
                'author': [(6, 0, artist_id.ids or False)],
                'albums_and_singles': [(4, single_id.id)],
                'member': string
            }
            self.env['songs'].create(single_info)

        try:
            for single in values['singles']['songs']['song']:
                _parse_single(single)
        except:
            pass

        def _parse_album(album_values):
            album_or_single_info = {
                'album_and_single': album_values.get('name'),
                'artists': [(6, 0, artist_id.ids or False)]
            }
            album_id = self.env['albums.singles'].create(album_or_single_info)

            def _parse_album_songs(album_songs):
                album_songs_info = {
                    'name': album_songs.get('name'),
                    'duration': album_songs.get('duration'),
                    'listeners': album_songs.get('listeners'),
                    'author': [(6, 0, artist_id.ids or False)],
                    'albums_and_singles': [(6, 0, album_id.ids or False)]
                }
                self.env['songs'].create(album_songs_info)

            for album_songs in album['songs']['song']:
                _parse_album_songs(album_songs)

        try:
            for album in values['albums']['album']:
                _parse_album(album)
        except:
            pass
        return values

    def _parse_group(self, group):
        group_info = {
            'month_listeners': group.get('month_listeners'),
            'name': group.get('name')
        }
        group_id = self.env['groups'].create(group_info)
        for artist in group['artists']['artist']:
            self._parse_group_artist(artist, group_id, group)
        return group

    def _parse_group_artist(self, artist, group_id, group):
        artist_info = {
            'name': artist.get('name'),
            'age': artist.get('age'),
            'sex': artist.get('sex'),
            'country': artist.get('country'),
            'groups': [(6, 0, group_id.ids or False)]
        }
        artists_id = self.env['artists'].create(artist_info)
        try:
            for single in group['singles']['songs']['song']:
                self._parse_group_singles(single, artists_id, group_id)
        except:
            pass
        # if isinstance(group['albums']['album'], dict):
        #     album = group['albums']['album']['name']
        #     self._parse_group_albums(album, artists_id, group_id)
        members = {}
        string = ()
        try:
            for album in group['albums']['album']:
                self._parse_group_albums(album, artists_id, group_id)
        except:
            try:
                self._parse_group_albums(group(group['albums']['album']), artists_id, group_id)
            except:
                pass

    def _parse_group_singles(self, single, artist_id, group_id):

        update_song = self.env['songs'].search(
            [('name', '=', single.get('name')),
             ('duration', '=', single.get('duration'))
             ])
        if not update_song:
            album_or_single_info = {
                'album_and_single': 'single',
                'artists': [(6, 0, artist_id.ids or False)],
                'groups': [(6, 0, group_id.ids or False)]
            }
            single_id = self.env['albums.singles'].create(album_or_single_info)
            single_info = {
                'name': single.get('name'),
                'duration': single.get('duration'),
                'listeners': single.get('listeners'),
                'author': [(6, 0, artist_id.ids or False)],
                'albums_and_singles': [(4, single_id.id)],
                'groups': [(6, 0, group_id.ids or False)]
            }
            self.env['songs'].create(single_info)

        if update_song:
            update_song.write({
                'author': [(4, artist_id.id)]
            })
            update_single = self.env['albums.singles'].search([
                ('songs', '=', update_song.ids)])
            update_single.write({
                'artists': [(4, artist_id.id)]
            })

    def _parse_group_albums(self, album, artists_id, group_id):
        update_album = self.env['albums.singles'].search([
            'album_and_single', '=', album.get('name')
        ])
        if not update_album:
            album_or_single_info = {
                'album_and_single': album.get('name'),
                'artists': [(6, 0, artists_id.ids or False)],
                'groups': [(6, 0, group_id.ids or False)]
            }
            album_id = self.env['albums.singles'].create(album_or_single_info)
        if update_album:
            update_album.write({
                'artists': [(4, artists_id.id)]
            })

    #     for songs in album['songs']['song']:
    #         self._parse_groups_albums_songs(songs, artists_id, group_id, album_id, album)
    #
    # def _parse_groups_albums_songs(self, songs, artists_id, group_id, album_id, album):
    #     update_song = self.env['songs'].search(
    #         [('name', '=', songs.get('name')),
    #          ('duration', '=', songs.get('duration'))
    #          ])
    #     if not update_song:
    #         album_songs_info = {
    #             'name': songs.get('name'),
    #             'duration': songs.get('duration'),
    #             'listeners': songs.get('listeners'),
    #             'author': [(6, 0, artists_id.ids or False)],
    #             'albums_and_singles': [(6, 0, album_id.ids or False)],
    #             'groups': [(6, 0, group_id.ids or False)]
    #         }
    #         self.env['songs'].crate(album_songs_info)
    #     if update_song:
    #         update_song.write({
    #             'author': [(4, artists_id.id)]
    #         })
    #         update_album = self.env['albums.singles'].search([
    #             ('album_and_single', album.get('name'))
    #         ])
    #         update_album.write({
    #             'artists': [(4, artists_id)]
    #         })

    def upload_file_xml(self):
        data_dict = f'{base64.b64decode(self.import_xml).decode()}'
        data_dict = xmltodict.parse(data_dict)

        """"
        Artists info create
        """
        for artist in data_dict['music']['Artists']['artist']:
            self._parse_artist(artist)

        """
        Groups info create
        """
        for group in data_dict['music']['Groups']['group']:
            self._parse_group(group)
