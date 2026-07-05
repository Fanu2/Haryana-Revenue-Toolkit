"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Toolbar.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)


class JamabandiToolbar(QWidget):
    """
    Toolbar used by the
    Jamabandi Workspace.
    """

    add_requested = Signal()

    edit_requested = Signal()

    delete_requested = Signal()

    refresh_requested = Signal()

    finalize_requested = Signal()

    reopen_requested = Signal()

    print_requested = Signal()

    export_requested = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

        #
        # Initial state
        #

        self.update_state(
            selected=False,
        )

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._add_button = QPushButton(
            "New",
        )

        self._edit_button = QPushButton(
            "Edit",
        )

        self._delete_button = QPushButton(
            "Delete",
        )

        self._refresh_button = QPushButton(
            "Refresh",
        )

        self._finalize_button = QPushButton(
            "Finalize",
        )

        self._reopen_button = QPushButton(
            "Reopen",
        )

        self._print_button = QPushButton(
            "Print",
        )

        self._export_button = QPushButton(
            "Export",
        )

        #
        # Future features
        #

        self._print_button.setEnabled(
            False,
        )

        self._export_button.setEnabled(
            False,
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QHBoxLayout()

        layout.addWidget(
            self._add_button,
        )

        layout.addWidget(
            self._edit_button,
        )

        layout.addWidget(
            self._delete_button,
        )

        layout.addSpacing(
            16,
        )

        layout.addWidget(
            self._refresh_button,
        )

        layout.addStretch()

        layout.addWidget(
            self._finalize_button,
        )

        layout.addWidget(
            self._reopen_button,
        )

        layout.addSpacing(
            16,
        )

        layout.addWidget(
            self._print_button,
        )

        layout.addWidget(
            self._export_button,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Signals
    # ---------------------------------------------------------

    def _connect_signals(
        self,
    ) -> None:

        self._add_button.clicked.connect(
            self.add_requested,
        )

        self._edit_button.clicked.connect(
            self.edit_requested,
        )

        self._delete_button.clicked.connect(
            self.delete_requested,
        )

        self._refresh_button.clicked.connect(
            self.refresh_requested,
        )

        self._finalize_button.clicked.connect(
            self.finalize_requested,
        )

        self._reopen_button.clicked.connect(
            self.reopen_requested,
        )

        self._print_button.clicked.connect(
            self.print_requested,
        )

        self._export_button.clicked.connect(
            self.export_requested,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def update_state(
        self,
        *,
        selected: bool,
        finalized: bool = False,
    ) -> None:
        """
        Update the toolbar according to the
        current workspace state.
        """

        #
        # Always available
        #

        self._add_button.setEnabled(
            True,
        )

        self._refresh_button.setEnabled(
            True,
        )

        #
        # No selection
        #

        if not selected:

            self._edit_button.setEnabled(
                False,
            )

            self._delete_button.setEnabled(
                False,
            )

            self._finalize_button.setEnabled(
                False,
            )

            self._reopen_button.setEnabled(
                False,
            )

            return

        #
        # Draft Jamabandi
        #

        if not finalized:

            self._edit_button.setEnabled(
                True,
            )

            self._delete_button.setEnabled(
                True,
            )

            self._finalize_button.setEnabled(
                True,
            )

            self._reopen_button.setEnabled(
                False,
            )

            return

        #
        # Finalized Jamabandi
        #

        self._edit_button.setEnabled(
            False,
        )

        self._delete_button.setEnabled(
            False,
        )

        self._finalize_button.setEnabled(
            False,
        )

        self._reopen_button.setEnabled(
            True,
        )