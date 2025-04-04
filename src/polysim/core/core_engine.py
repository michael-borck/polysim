import flet as ft
from polysim.core.game_state import GameState
from polysim.ui.ui_manager import UIManager
from polysim.core.event_manager import EventManager
from polysim.core.event import Event
from polysim.resource_loader import ResourceLoader

class CoreEngine:
    def __init__(self, page: ft.Page):
        self.page = page
        self.game_state = GameState()
        self.ui_manager = UIManager(self.page, self.game_state)
        self.event_manager = EventManager()
        self.setup()

    def setup(self):
        # Use path to configs folder
        loader = ResourceLoader('configs/business.json')
        self.decisions = loader.get_decisions()
        self.rules = loader.get_rules()
        self.events = loader.get_events()
        self.resources = loader.get_resources()
        self.themes = loader.get_themes()
        self.ui_manager.setup_ui()
        self.event_manager.register_listener("score_changed", self.ui_manager.update_score_display)
        self.page.update()

    def run(self):
        self.page.update()
