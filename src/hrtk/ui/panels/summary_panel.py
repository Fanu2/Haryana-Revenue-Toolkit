"""
Haryana Revenue Toolkit (HRTK)

Reusable Summary Panel.
"""

from __future__ import annotations

from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QFormLayout,
    QFrame,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class SummaryPanel(
    QFrame,
):
    """
    Generic summary panel used
    throughout HRTK.

    The panel displays a title and
    dynamically created rows.

    No business logic belongs here.
    """

    def __init__(
        self,
        title: str,
        parent: QWidget | None = None,
    ) -> None:

        super().__init__(
            parent,
        )

        self._title = QLabel(
            title,
        )

        self._rows: dict[
            str,
            QLabel,
        ] = {}

        self._layout = QVBoxLayout(
            self,
        )

        self._form = QFormLayout()

        self._configure()

        self._layout.addWidget(
            self._title,
        )

        self._layout.addLayout(
            self._form,
        )

        self._layout.addStretch()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def set_title(
        self,
        title: str,
    ) -> None:
        """
        Set the panel title.
        """

        self._title.setText(
            title,
        )

    def title(
        self,
    ) -> str:
        """
        Return the current title.
        """

        return self._title.text()

    def set_value(
        self,
        label: str,
        value: str,
    ) -> None:
        """
        Create or update a summary row.
        """

        if label not in self._rows:

            value_label = QLabel()

            value_label.setAlignment(
                Qt.AlignRight
                | Qt.AlignVCenter,
            )

            self._rows[label] = (
                value_label
            )

            self._form.addRow(
                QLabel(label),
                value_label,
            )

        self._rows[label].setText(
            value,
        )

    def value(
        self,
        label: str,
    ) -> str:
        """
        Return the displayed value
        for a row.
        """

        if label not in self._rows:

            return ""

        return self._rows[
            label
        ].text()

    def labels(
        self,
    ) -> list[str]:
        """
        Return all row labels.
        """

        return list(
            self._rows.keys(),
        )

    def clear(
        self,
    ) -> None:
        """
        Clear displayed values.
        """

        for value_label in (
            self._rows.values()
        ):

            value_label.clear()

    # ---------------------------------------------------------
    # Configuration
    # ---------------------------------------------------------

    def _configure(
        self,
    ) -> None:
        """
        Configure the panel appearance.
        """

        self.setFrameShape(
            QFrame.StyledPanel,
        )

        self.setFrameShadow(
            QFrame.Raised,
        )

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred,
        )

        self._layout.setContentsMargins(
            10,
            10,
            10,
            10,
        )

        self._layout.setSpacing(
            8,
        )

        self._form.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self._form.setHorizontalSpacing(
            20,
        )

        self._form.setVerticalSpacing(
            6,
        )

        self._title.setAlignment(
            Qt.AlignCenter,
        )

        font = self._title.font()

        font.setBold(
            True,
        )

        font.setPointSize(
            font.pointSize() + 1,
        )

        self._title.setFont(
            font,
        )

    # ---------------------------------------------------------
    # Private Helpers
    # ---------------------------------------------------------

    def _has_row(
        self,
        label: str,
    ) -> bool:
        """
        Return True if the row exists.
        """

        return (
            label in self._rows
        )
    
    def set_values(
        self,
        values: dict[str, str],
    ) -> None:
        """
        Update all displayed values.
        """

        for label, value in values.items():

            self.set_value(
                label,
                value,
            )

    def remove_row(
        self,
        label: str,
    ) -> None:
        """
        Remove a row from the panel.
        """

        if label not in self._rows:

            return

        value_label = self._rows.pop(
            label,
        )

        for row in range(
            self._form.rowCount(),
        ):

            item = self._form.itemAt(
                row,
                QFormLayout.LabelRole,
            )

            if item is None:

                continue

            widget = item.widget()

            if (
                isinstance(
                    widget,
                    QLabel,
                )
                and widget.text() == label
            ):

                label_widget = widget

                self._form.removeRow(
                    row,
                )

                label_widget.deleteLater()

                value_label.deleteLater()

                break

    def values(
        self,
    ) -> dict[str, str]:
        """
        Return all displayed values.
        """

        return {
            label: widget.text()
            for label, widget in self._rows.items()
        }