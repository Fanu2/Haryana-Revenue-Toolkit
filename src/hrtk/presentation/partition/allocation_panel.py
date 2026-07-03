"""
Haryana Revenue Toolkit (HRTK)

Allocation Panel.
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QButtonGroup,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)


class AllocationPanel(QWidget):
    """
    Allocation input panel used by the
    Partition Workbench.
    """

    allocate_requested = Signal()

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self._create_widgets()

        self._build_layout()

        self._connect_signals()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:
        """
        Create all panel widgets.
        """

        #
        # Selection
        #

        self._owner_value = QLabel(
            "---"
        )

        self._khasra_value = QLabel(
            "---"
        )

        self._remaining_area = QLabel(
            "0K-0M-0S"
        )

        #
        # Allocation Mode
        #

        self._entire_radio = QRadioButton(
            "Allocate Entire Khasra"
        )

        self._manual_radio = QRadioButton(
            "Manual Allocation"
        )

        self._manual_radio.setChecked(
            True
        )

        self._mode_group = QButtonGroup(
            self,
        )

        self._mode_group.addButton(
            self._entire_radio,
        )

        self._mode_group.addButton(
            self._manual_radio,
        )

        #
        # Area Entry
        #

        self._kanal_edit = QLineEdit()

        self._marla_edit = QLineEdit()

        self._sarsai_edit = QLineEdit()

        self._kanal_edit.setPlaceholderText(
            "Kanal"
        )

        self._marla_edit.setPlaceholderText(
            "Marla"
        )

        self._sarsai_edit.setPlaceholderText(
            "Sarsai"
        )

        #
        # Allocate Button
        #

        self._allocate_button = QPushButton(
            "Allocate"
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:
        """
        Build the Allocation Panel layout.
        """

        #
        # Selection Group
        #

        selection_group = QGroupBox(
            "Allocation"
        )

        selection_layout = QFormLayout()

        selection_layout.addRow(
            "Selected Owner",
            self._owner_value,
        )

        selection_layout.addRow(
            "Selected Khasra",
            self._khasra_value,
        )

        selection_layout.addRow(
            "Remaining Area",
            self._remaining_area,
        )

        selection_group.setLayout(
            selection_layout,
        )

        #
        # Allocation Mode
        #

        mode_group = QGroupBox(
            "Allocation Mode"
        )

        mode_layout = QVBoxLayout()

        mode_layout.addWidget(
            self._entire_radio,
        )

        mode_layout.addWidget(
            self._manual_radio,
        )

        mode_group.setLayout(
            mode_layout,
        )

        #
        # Area Entry
        #

        area_group = QGroupBox(
            "Allocation Area"
        )

        area_layout = QGridLayout()

        area_layout.addWidget(
            QLabel("Kanal"),
            0,
            0,
        )

        area_layout.addWidget(
            self._kanal_edit,
            0,
            1,
        )

        area_layout.addWidget(
            QLabel("Marla"),
            1,
            0,
        )

        area_layout.addWidget(
            self._marla_edit,
            1,
            1,
        )

        area_layout.addWidget(
            QLabel("Sarsai"),
            2,
            0,
        )

        area_layout.addWidget(
            self._sarsai_edit,
            2,
            1,
        )

        area_group.setLayout(
            area_layout,
        )

        #
        # Main Layout
        #

        layout = QVBoxLayout()

        layout.addWidget(
            selection_group,
        )

        layout.addWidget(
            mode_group,
        )

        layout.addWidget(
            area_group,
        )

        layout.addStretch()

        layout.addWidget(
            self._allocate_button,
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
        """
        Connect widget signals.
        """

        self._allocate_button.clicked.connect(
            self.allocate_requested.emit,
        )

        self._entire_radio.toggled.connect(
            self._update_mode,
        )

        self._update_mode()

    # ---------------------------------------------------------
    # Mode Handling
    # ---------------------------------------------------------

    def _update_mode(
        self,
    ) -> None:
        """
        Enable or disable manual area entry.
        """

        manual = self._manual_radio.isChecked()

        self._kanal_edit.setEnabled(
            manual,
        )

        self._marla_edit.setEnabled(
            manual,
        )

        self._sarsai_edit.setEnabled(
            manual,
        )

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_owner(
        self,
        owner: str,
    ) -> None:
        """
        Display selected owner.
        """

        self._owner_value.setText(
            owner,
        )

    def set_khasra(
        self,
        khasra: str,
    ) -> None:
        """
        Display selected Khasra.
        """

        self._khasra_value.setText(
            khasra,
        )

    def set_remaining_area(
        self,
        area: str,
    ) -> None:
        """
        Display remaining area.
        """

        self._remaining_area.setText(
            area,
        )

    def allocation_mode(
        self,
    ) -> str:
        """
        Return current allocation mode.
        """

        if self._entire_radio.isChecked():

            return "entire"

        return "manual"

    def allocated_area(
        self,
    ) -> tuple[int, int, int]:
        """
        Return entered area.
        """

        def value(
            widget: QLineEdit,
        ) -> int:

            text = widget.text().strip()

            if not text:

                return 0

            return int(text)

        return (
            value(
                self._kanal_edit,
            ),
            value(
                self._marla_edit,
            ),
            value(
                self._sarsai_edit,
            ),
        )

    def clear(
        self,
    ) -> None:
        """
        Reset panel.
        """

        self._owner_value.setText(
            "---",
        )

        self._khasra_value.setText(
            "---",
        )

        self._remaining_area.setText(
            "0K-0M-0S",
        )

        self._kanal_edit.clear()

        self._marla_edit.clear()

        self._sarsai_edit.clear()

        self._manual_radio.setChecked(
            True,
        )