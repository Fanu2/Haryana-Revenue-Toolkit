"""
Haryana Revenue Toolkit (HRTK)

Main Window.

Application shell.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
)

from hrtk.application.application_context import ApplicationContext
from hrtk.presentation.navigation import Navigator
from hrtk.presentation.statusbar import StatusBar
from hrtk.presentation.toolbar import MainToolbar
from hrtk.presentation.workspace import WorkspaceArea


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    WINDOW_TITLE = "Haryana Revenue Toolkit"
    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 900

    def __init__(self, context: ApplicationContext) -> None:
        super().__init__()

        self._context = context

        self._navigator: Navigator | None = None
        self._workspace: WorkspaceArea | None = None
        self._toolbar: MainToolbar | None = None
        self._status_bar: StatusBar | None = None

        self._initialize()

    @property
    def context(self) -> ApplicationContext:
        """Return the application context."""
        return self._context

    @property
    def navigator(self) -> Navigator:
        """Return the application navigator."""
        assert self._navigator is not None
        return self._navigator

    @property
    def workspace(self) -> WorkspaceArea:
        """Return the workspace area."""
        assert self._workspace is not None
        return self._workspace

    @property
    def toolbar(self) -> MainToolbar:
        """Return the main toolbar."""
        assert self._toolbar is not None
        return self._toolbar

    @property
    def status_bar(self) -> StatusBar:
        """Return the status bar."""
        assert self._status_bar is not None
        return self._status_bar

    def _initialize(self) -> None:
        """Initialize the application shell."""

        self.setWindowTitle(self.WINDOW_TITLE)
        self.resize(
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT,
        )

        self._build_menu_bar()
        self._build_toolbar()
        self._build_workspace()
        self._build_status_bar()

        self.context.logging.logger.info(
            "Main window initialized."
        )

    def _build_menu_bar(self) -> None:
        """Create the application menu."""

        menu_bar = self.menuBar()

        menu_bar.addMenu("&File")
        menu_bar.addMenu("&Revenue")
        menu_bar.addMenu("&GIS")
        menu_bar.addMenu("&Reports")
        menu_bar.addMenu("&Tools")
        menu_bar.addMenu("&Help")

    def _build_toolbar(self) -> None:
        """Create the application toolbar."""

        self._toolbar = MainToolbar()

        self.addToolBar(self._toolbar)

    def _build_workspace(self) -> None:
        """Create the application workspace."""

        splitter = QSplitter(
            Qt.Orientation.Horizontal
        )

        self._navigator = Navigator()

        self._workspace = WorkspaceArea(
            self.context
        )

        #
        # Navigator -> Workspace
        #
        self._navigator.page_requested.connect(
            self._change_page
        )

        splitter.addWidget(self._navigator)
        splitter.addWidget(self._workspace)

        splitter.setChildrenCollapsible(False)

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        splitter.setSizes([260, 1100])

        self.setCentralWidget(splitter)

    def _build_status_bar(self) -> None:
        """Create the application status bar."""

        self._status_bar = StatusBar()

        self.setStatusBar(self._status_bar)

    def _change_page(self, page: str) -> None:
        """
        Handle navigation requests.
        """

        self.context.logging.logger.info(
            "Navigator requested page: %s",
            page,
        )

        self.workspace.show_page(page)
    def __repr__(self) -> str:
        return (
            f"MainWindow("
            f"title={self.WINDOW_TITLE!r})"
        )