"""
Haryana Revenue Toolkit (HRTK)

Partition Summary Panel.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QLabel,
)


class SummaryPanel(QGroupBox):
    """
    Displays live partition summary.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(
            "Summary",
            parent,
        )

        self._create_widgets()

        self._build_layout()

    # ---------------------------------------------------------
    # Widgets
    # ---------------------------------------------------------

    def _create_widgets(
        self,
    ) -> None:

        self._owners = QLabel("0")

        self._khasras = QLabel("0")

        self._total_area = QLabel("-")

        self._allocated = QLabel("-")

        self._remaining = QLabel("-")

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _build_layout(
        self,
    ) -> None:

        layout = QFormLayout()

        layout.addRow(
            "Owners",
            self._owners,
        )

        layout.addRow(
            "Khasras",
            self._khasras,
        )

        layout.addRow(
            "Total Area",
            self._total_area,
        )

        layout.addRow(
            "Allocated",
            self._allocated,
        )

        layout.addRow(
            "Remaining",
            self._remaining,
        )

        self.setLayout(
            layout,
        )

    # ---------------------------------------------------------
    # Public
    # ---------------------------------------------------------

    def update_summary(
        self,
        ownerships,
        khasras,
    ) -> None:
        """
        Refresh summary values.
        """

        self._owners.setText(
            str(
                len(
                    ownerships,
                )
            )
        )

        self._khasras.setText(
            str(
                len(
                    khasras,
                )
            )
        )

        #
        # Total Area
        #

        total_area = 0

        for khasra in khasras:

            if hasattr(
                khasra,
                "area",
            ):

                try:

                    total_area += float(
                        khasra.area
                    )

                except Exception:

                    pass

        if total_area:

            self._total_area.setText(
                str(
                    total_area
                )
            )

        else:

            self._total_area.setText(
                "-"
            )

        #
        # Allocation Engine
        #

        self._allocated.setText(
            "-"
        )

        self._remaining.setText(
            "-"
        )

    def clear(
        self,
    ) -> None:
        """
        Clear panel.
        """

        self._owners.setText("0")

        self._khasras.setText("0")

        self._total_area.setText("-")

        self._allocated.setText("-")

        self._remaining.setText("-")