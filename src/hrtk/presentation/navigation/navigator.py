"""
Navigator.
"""

from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
)


class Navigator(QTreeWidget):
    """
    Left navigation tree.
    """

    page_requested = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.setHeaderHidden(True)

        self._build_tree()

        self.itemClicked.connect(
            self._item_clicked
        )

    def _build_tree(self) -> None:

        dashboard = QTreeWidgetItem(["Dashboard"])

        revenue = QTreeWidgetItem(["Revenue"])
        revenue.addChild(QTreeWidgetItem(["Villages"]))
        revenue.addChild(QTreeWidgetItem(["Owners"]))
        revenue.addChild(QTreeWidgetItem(["Khewats"]))
        revenue.addChild(QTreeWidgetItem(["Khasras"]))
        revenue.addChild(QTreeWidgetItem(["Ownership"]))
        revenue.addChild(
            QTreeWidgetItem(
                ["Partition Workspace"]
            )
        )

        gis = QTreeWidgetItem(["GIS"])
        gis.addChild(QTreeWidgetItem(["Canvas"]))
        gis.addChild(QTreeWidgetItem(["Maps"]))

        reports = QTreeWidgetItem(["Reports"])

        settings = QTreeWidgetItem(["Settings"])

        self.addTopLevelItem(dashboard)
        self.addTopLevelItem(revenue)
        self.addTopLevelItem(gis)
        self.addTopLevelItem(reports)
        self.addTopLevelItem(settings)

        self.expandAll()
    
    
    def _item_clicked(
        self,
        item: QTreeWidgetItem,
        column: int,
    ) -> None:
        del column

        self.page_requested.emit(item.text(0))