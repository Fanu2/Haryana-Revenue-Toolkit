"""
Haryana Revenue Toolkit (HRTK)

Application.

Responsible for bootstrapping and running the desktop application.
"""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from hrtk.application.application_context import ApplicationContext


class Application:
    """
    Main HRTK application.

    Responsibilities
    ----------------
    * Create QApplication.
    * Create ApplicationContext.
    * Create the main window.
    * Start the Qt event loop.
    """

    def __init__(self) -> None:
        self._qt_app = QApplication(sys.argv)

        self._context = ApplicationContext()

        self._main_window = None

        self._context.logging.logger.info(
            "Application initialized."
        )

    @property
    def qt_app(self) -> QApplication:
        """Return the Qt application instance."""
        return self._qt_app

    @property
    def context(self) -> ApplicationContext:
        """Return the application context."""
        return self._context

    @property
    def main_window(self):
        """Return the main window."""
        return self._main_window

    def set_main_window(self, window) -> None:
        """
        Register the application's main window.
        """
        self._main_window = window

    def run(self) -> int:
        """
        Start the application.
        """
        if self._main_window is None:
            raise RuntimeError(
                "Main window has not been assigned."
            )

        self._main_window.show()

        self._context.logging.logger.info(
            "Application started."
        )

        exit_code = self._qt_app.exec()

        self.shutdown()

        return exit_code

    def shutdown(self) -> None:
        """
        Shutdown the application gracefully.
        """
        self._context.logging.logger.info(
            "Application shutting down."
        )

        self._context.shutdown()

    def __repr__(self) -> str:
        return (
            f"Application("
            f"workspace={self.context.workspace.root!s})"
        )