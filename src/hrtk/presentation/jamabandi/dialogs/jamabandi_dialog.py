"""
Haryana Revenue Toolkit (HRTK)

Jamabandi Dialog.
"""

from __future__ import annotations

from uuid import uuid4

from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)

from hrtk.domain.jamabandi import (
    Jamabandi,
)


class JamabandiDialog(
    QDialog,
):
    """
    Dialog used to create or edit
    a Jamabandi.
    """

    def __init__(
        self,
        village_id,
        jamabandi: Jamabandi | None = None,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._village_id = village_id

        self._jamabandi = jamabandi

        self.setWindowTitle(
            "Jamabandi"
        )

        self.resize(
            500,
            320,
        )

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

        if jamabandi is not None:

            self._load_data()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._year_edit = QLineEdit()

        self._mutation_edit = QLineEdit()

        self._remarks_edit = QTextEdit()

        self._active_check = QCheckBox(
            "Active"
        )

        self._finalized_check = QCheckBox(
            "Finalized"
        )

        self._active_check.setChecked(
            True,
        )

        self._buttons = (
            QDialogButtonBox(
                QDialogButtonBox.Ok
                |
                QDialogButtonBox.Cancel
            )
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        form = QFormLayout()

        form.addRow(
            "Year",
            self._year_edit,
        )

        form.addRow(
            "Mutation No.",
            self._mutation_edit,
        )

        form.addRow(
            "Remarks",
            self._remarks_edit,
        )

        status = QHBoxLayout()

        status.addWidget(
            self._active_check,
        )

        status.addWidget(
            self._finalized_check,
        )

        status.addStretch()

        layout = QVBoxLayout()

        layout.addLayout(
            form,
        )

        layout.addLayout(
            status,
        )

        layout.addWidget(
            self._buttons,
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

        self._buttons.accepted.connect(
            self._accept,
        )

        self._buttons.rejected.connect(
            self.reject,
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def _load_data(
        self,
    ) -> None:

        self._year_edit.setText(
            self._jamabandi.year,
        )

        self._mutation_edit.setText(
            self._jamabandi.mutation_no,
        )

        self._remarks_edit.setPlainText(
            self._jamabandi.remarks,
        )

        self._active_check.setChecked(
            self._jamabandi.active,
        )

        self._finalized_check.setChecked(
            self._jamabandi.finalized,
        )

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    def _accept(
        self,
    ) -> None:

        year = (
            self._year_edit.text()
            .strip()
        )

        if not year:

            QMessageBox.warning(
                self,
                "Validation",
                "Year is required.",
            )

            return

        self.accept()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def jamabandi(
        self,
    ) -> Jamabandi:
        """
        Return the edited
        Jamabandi.
        """

        if self._jamabandi is None:

            entity_id = uuid4()

        else:

            entity_id = (
                self._jamabandi.id
            )

        return Jamabandi(

            id=entity_id,

            village_id=self._village_id,

            year=self._year_edit.text().strip(),

            mutation_no=(
                self._mutation_edit.text()
                .strip()
            ),

            remarks=(
                self._remarks_edit
                .toPlainText()
                .strip()
            ),

            active=(
                self._active_check
                .isChecked()
            ),

            finalized=(
                self._finalized_check
                .isChecked()
            ),
        )