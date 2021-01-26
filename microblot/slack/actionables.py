from dataclasses import dataclass
from typing import Optional

from slack_sdk import WebClient

from .modals import populate_post_modal


@dataclass
class SlackBase:
    pass


@dataclass
class SlackCommand(SlackBase):
    team_id: str  # TODO move to base class
    user_id: str  # TODO move to base class
    action: str  # TODO move to base class

    params: Optional[list[str]]

    token: str
    response_url: str
    trigger_id: str

    default_action: str = "action_help"

    @property
    def default_action(self):
        # TODO move to base class
        raise NotImplementedError

    def execute(self):
        # TODO move to base class
        method = getattr(self, f"action_{self.action}", self.default_action)
        return method()

    @property
    def post_id(self):
        return int(self.params)

    def action_new(self):
        """Open new post modal."""
        TEMP_SLACK_BOT_TOKEN = ""
        client = WebClient(token=TEMP_SLACK_BOT_TOKEN)
        response = client.views_open(
            trigger_id=self.trigger_id,
            view=populate_post_modal(modal_type="new_post"),
        )
        ok = response.get("ok", False)
        return ok

    def action_list(self):
        """List posts in UI, deets TBD."""
        ...  # TODO

    def action_edit(self):
        """Open edit post modal."""
        ...  # TODO

    def action_delete(self):
        """Delete post."""
        ...  # TODO

    def action_info(self):
        """Show blog info."""
        ...  # TODO

    def action_help(self):
        """Show Microblot commands."""
        ...  # TODO


@dataclass
class SlackInteraction(SlackBase):
    team_id: str  # TODO move to base class
    user_id: str  # TODO move to base class
    action: str  # TODO move to base class

    params: dict[str, str]

    default_action = None

    @property
    def default_action(self):
        # TODO move to base class
        raise NotImplementedError

    def execute(self):
        # TODO move to base class
        method = getattr(self, f"action_{self.action}", self.default_action)
        return method()

    def action_new(self):
        """Create new post."""
        ...  # TODO

    def action_edit(self):
        """Update existing post."""
        ...  # TODO

    def action_config_author(self):
        """Update author config."""
        ...  # TODO

    def action_config_blog(self):
        """Update blog config."""
        ...  # TODO
