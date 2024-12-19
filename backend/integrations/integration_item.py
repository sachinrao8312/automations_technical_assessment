from datetime import datetime
from typing import Optional, List


class IntegrationItem:
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[str] = None,
        directory: bool = False,
        parent_path_or_name: Optional[str] = None,
        parent_id: Optional[str] = None,
        name: Optional[str] = None,
        creation_time: Optional[datetime] = None,
        last_modified_time: Optional[datetime] = None,
        url: Optional[str] = None,
        children: Optional[List[str]] = None,
        mime_type: Optional[str] = None,
        delta: Optional[str] = None,
        drive_id: Optional[str] = None,
        visibility: Optional[bool] = True,
    ):
        self.id = id
        self.type = type
        self.directory = directory
        self.parent_path_or_name = parent_path_or_name
        self.parent_id = parent_id
        self.name = name
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.url = url
        self.children = children or []
        self.mime_type = mime_type
        self.delta = delta
        self.drive_id = drive_id
        self.visibility = visibility

    def __repr__(self):
        return f"<IntegrationItem(id={self.id}, type={self.type}, name={self.name})>"

    def __str__(self):
        return f"IntegrationItem: {self.name} (ID: {self.id}, Type: {self.type})"

    # New Methods
    def to_dict(self):
        """Convert the object to a dictionary."""
        return {
            "id": self.id,
            "type": self.type,
            "directory": self.directory,
            "parent_path_or_name": self.parent_path_or_name,
            "parent_id": self.parent_id,
            "name": self.name,
            "creation_time": self.creation_time.isoformat() if self.creation_time else None,
            "last_modified_time": self.last_modified_time.isoformat() if self.last_modified_time else None,
            "url": self.url,
            "children": self.children,
            "mime_type": self.mime_type,
            "delta": self.delta,
            "drive_id": self.drive_id,
            "visibility": self.visibility,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create an IntegrationItem instance from a dictionary."""
        return cls(
            id=data.get("id"),
            type=data.get("type"),
            directory=data.get("directory", False),
            parent_path_or_name=data.get("parent_path_or_name"),
            parent_id=data.get("parent_id"),
            name=data.get("name"),
            creation_time=datetime.fromisoformat(data["creation_time"]) if data.get("creation_time") else None,
            last_modified_time=datetime.fromisoformat(data["last_modified_time"]) if data.get("last_modified_time") else None,
            url=data.get("url"),
            children=data.get("children", []),
            mime_type=data.get("mime_type"),
            delta=data.get("delta"),
            drive_id=data.get("drive_id"),
            visibility=data.get("visibility", True),
        )

    def add_child(self, child_id: str):
        """Add a child ID to the children list."""
        if child_id not in self.children:
            self.children.append(child_id)

    def remove_child(self, child_id: str):
        """Remove a child ID from the children list."""
        if child_id in self.children:
            self.children.remove(child_id)

    def is_visible(self):
        """Check if the item is visible."""
        return self.visibility

    def update_last_modified_time(self):
        """Update the last modified time to the current time."""
        self.last_modified_time = datetime.now()

    def set_visibility(self, visibility: bool):
        """Set the visibility of the item."""
        self.visibility = visibility
