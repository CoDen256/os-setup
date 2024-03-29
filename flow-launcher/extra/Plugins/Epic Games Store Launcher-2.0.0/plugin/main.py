import webbrowser
from difflib import SequenceMatcher as sm
from flox import Flox, ICON_WARNING
from flox.string_matcher import string_matcher

import egs


class EpicGamesStoreLauncher(Flox):

    def query(self, query):
        try:
            games = egs.get_games()
            for game in games:
                match_data = string_matcher(query, game.display_name)
                score = match_data.score if match_data else 0
                show_on_empty_query = self.settings.get(
                    'show_on_empty_query', True)
                if not game.b_is_incomplete_install:
                    self.add_item(
                        title=game.display_name,
                        subtitle=str(game.full_exe_path()),
                        icon=str(game.full_exe_path()),
                        method=self.launch,
                        parameters=[game.catalog_namespace,
                                    game.catalog_item_id, game.app_name],
                        score=int(score)
                    )
        except (FileNotFoundError):
            self.add_item(
                title='Unable to locate Epic Games Launcher',
                icon=ICON_WARNING
            )

    def context_menu(self, data):
        pass

    def launch(self, namespace, catalog_id, app_name):
        uri = f'com.epicgames.launcher://apps/{namespace}%3A{catalog_id}%3A{app_name}?action=launch&silent=true'
        webbrowser.open(uri)


if __name__ == "__main__":
    EpicGamesStoreLauncher()
