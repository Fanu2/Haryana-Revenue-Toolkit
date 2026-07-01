"""
Haryana Revenue Toolkit (HRTK)

Khasra Dialog.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QSpinBox,
    QVBoxLayout,
)

from hrtk.domain.parcel import Parcel
from hrtk.domain.value_objects.area import Area
from hrtk.domain.value_objects.parcel_number import (
    ParcelNumber,
)


class KhasraDialog(QDialog):
    """
    Dialog for creating or editing a parcel.
    """

    def __init__(
        self,
        parent=None,
    ) -> None:

        super().__init__(parent)

        self.setWindowTitle(
            "Khasra"
        )

        self._build_ui()

    def _build_ui(self) -> None:

        layout = QVBoxLayout()

        form = QFormLayout()

        self._rectangle = QSpinBox()
        self._rectangle.setMaximum(9999)

        self._killa = QLineEdit()

        self._kanal = QSpinBox()
        self._kanal.setMaximum(999)

        self._marla = QSpinBox()
        self._marla.setMaximum(19)

        self._sarsai = QSpinBox()
        self._sarsai.setMaximum(8)

        self._remarks = QLineEdit()

        form.addRow(
            "Rectangle",
            self._rectangle,
        )

        form.addRow(
            "Killa",
            self._killa,
        )

        form.addRow(
            "Kanal",
            self._kanal,
        )

        form.addRow(
            "Marla",
            self._marla,
        )

        form.addRow(
            "Sarsai",
            self._sarsai,
        )

        form.addRow(
            "Remarks",
            self._remarks,
        )

        layout.addLayout(
            form,
        )

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok
            | QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(
            self.accept,
        )

        buttons.rejected.connect(
            self.reject,
        )

        layout.addWidget(
            buttons,
        )

        self.setLayout(
            layout,
        )

    def value(
        self,
    ) -> Parcel:
        """
        Return the parcel entered by the user.
        """

        return Parcel(
            number=ParcelNumber(
                rectangle=self._rectangle.value(),
                killa=self._killa.text().strip(),
            ),
            area=Area.from_kms(
                kanal=self._kanal.value(),
                marla=self._marla.value(),
                sarsai=self._sarsai.value(),
            ),
            remarks=self._remarks.text().strip(),
        )
    
    def set_parcel(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Populate the dialog from an existing parcel.
        """

        self._rectangle.setValue(
            parcel.number.rectangle,
        )

        self._killa.setText(
            parcel.number.killa,
        )

        self._kanal.setValue(
         parcel.area.kanal,
        )

        self._marla.setValue(
            parcel.area.marla,
        )

        self._sarsai.setValue(
            parcel.area.sarsai,
        )

        self._remarks.setText(
            parcel.remarks,
    )


    def update_parcel(
        self,
        parcel: Parcel,
    ) -> None:
        """
        Update an existing parcel from the dialog.
        """

        parcel.number = ParcelNumber(
            rectangle=self._rectangle.value(),
            killa=self._killa.text().strip(),
        )

        parcel.area = Area.from_kms(
            kanal=self._kanal.value(),
            marla=self._marla.value(),
            sarsai=self._sarsai.value(),
        )

        parcel.remarks = (
            self._remarks.text().strip()
        )
