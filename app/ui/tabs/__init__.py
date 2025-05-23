"""
Tab modules for Document QA Assistant UI.
"""

# Import all tabs to make them available from tabs package
from app.ui.tabs.unified_chat_tab import unified_chat_tab
from app.ui.tabs.documents_tab import documents_tab
from app.ui.tabs.logs_tab import logs_tab
from app.ui.tabs.settings_tab import settings_tab
from app.ui.tabs.status_tab import status_tab

# Keep these imports for backward compatibility
# These tabs can be removed or disabled in the main app
from app.ui.tabs.chat_tab import chat_tab
from app.ui.tabs.general_knowledge_tab import general_knowledge_tab