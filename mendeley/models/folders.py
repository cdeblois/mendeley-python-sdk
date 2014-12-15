import arrow
from mendeley.models.documents import UserBaseDocument
from mendeley.models.common import Discipline, Photo, Location, Education, Employment
from mendeley.response import SessionResponseObject, LazyResponseObject


class Folder(SessionResponseObject):
    """
    A Mendeley profile.

    .. attribute:: id
    .. attribute:: name
    .. attribute:: created
    .. attribute:: modified
    .. attribute:: parent_id
    .. attribute:: group_id
    """
    content_type = 'application/vnd.mendeley-folder.1+json'

    @property
    def name(self):
        """
        """
        if 'name' in self.json:
            return self.json['name']
        else:
            return None

    @property
    def created(self):
        """
        """
        if 'created' in self.json:
            return arrow.get(self.json['created'])
        else:
            return None

    @property
    def modified(self):
        """
        """
        if 'modified' in self.json:
            return self.json['modified']
        else:
            return None

    @property
    def parent_id(self):
        """
        """
        if 'parent_id' in self.json:
            return self.json['parent_id']
        else:
            return None

    @property
    def group_id(self):
        """
        """
        if 'group_id' in self.json:
            return self.json['group_id']
        else:
            return None

    @property
    def documents(self):
        return self.session.folder_documents(self.id)
    
    @classmethod
    def fields(cls):
        return ['id', 'name', 'created', 'modified', 'parent_id', 'group_id']


class FolderDocument(LazyResponseObject, UserBaseDocument): 
    """
    A document of a Mendeley folder.
    .. attribute:: id
    """
    content_type = 'application/vnd.mendeley-document.1+json'

    def __init__(self, session, document_json):
        super(FolderDocument, self).__init__(session, document_json.get('id'), UserBaseDocument, lambda: self._load())

        self.document_json = document_json

    @property
    def joined(self):
        """
        an :class:`Arrow <arrow.arrow.Arrow>` object.
        """
        if 'joined' in self.document_json:
            return arrow.get(self.document_json['joined'])
        else:
            return None

    def _load(self):
        return self.session.documents.get(self.id)

