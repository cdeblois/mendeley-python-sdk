from mendeley.models.folders import Folder, FolderDocument
from mendeley.resources.base import ListResource


class Folders(ListResource):
    """
    Top-level resource for accessing files.  These can be:

    - folders for the logged-in user, if retrieved from a
      :func:`MendeleySession <mendeley.session.MendeleySession.folders>`.
    - folders attached to a :func:`CatalogDocument <mendeley.models.catalog.CatalogDocument.folders>`.
    - folders attached to a :func:`UserDocument <mendeley.models.documents.UserDocument.folders>`.
    - folders in a :func:`Group <mendeley.models.groups.Group.folders>`.
    """
    _url = '/folders'

    def __init__(self, session, document_id=None):
        self.session = session
        self.document_id = document_id

    def get(self, id):
        """
        Retrieves a folder by ID.

        :param id: the ID of the folder to get.
        :return: a :class:`File <mendeley.models.folders.Folder>`.
        """
        return super(Folders, self).get(id)

    def list(self, page_size=None, added_since=None, deleted_since=None):
        """
        Retrieves folders, as a paginated collection.

        :param page_size: the number of folders to return on each page.  Defaults to 20.
        :param added_since: if specified, only returns folders added after this timestamp.
        :param deleted_since: if specified, only returns the IDs of folder deleted after this timestamp.
        :return: a :class:`Page <mendeley.pagination.Page>` of :class:`Folders <mendeley.models.folders.Folder>`.
        """
        return super(Folders, self).list()

    def iter(self, page_size=None, added_since=None, deleted_since=None):
        """
        Retrieves folders, as an iterator.

        :param page_size: the number of folders to retrieve at a time.  Defaults to 20.
        :param added_since: if specified, only returns folders added after this timestamp.
        :param deleted_since: if specified, only returns the IDs of folders deleted after this timestamp.
        :return: an iterator of :class:`Folders <mendeley.models.folders.Folder>`.
        """
        return super(Folders, self).iter()

    @property
    def _session(self):
        return self.session

    def _obj_type(self, **kwargs):
        return Folder


class FolderDocuments(ListResource):
    """
    Resource for accessing documents of a folder.
    """
    def __init__(self, session, id):
        self.session = session
        self.id = id

    def list(self, page_size=None):
        """
        Retrieves documents of the folder, as a paginated collection.
        :param page_size: the number of documents to return on each page.  Defaults to 20.
        :return: a :class:`Page <mendeley.pagination.Page>` of
                 :class:`FolderDocuments <mendeley.models.folders.FolderDocument>`.
        """
        return super(FolderDocuments, self).list(page_size)

    def iter(self, page_size=None):
        """
        Retrieves documents of the folder, as an iterator.
        :param page_size: the number of documents to retrieve at a time.  Defaults to 20.
        :return: an iterator of :class:`FolderDocuments <mendeley.models.folders.FolderDocument>`.
        """
        return super(FolderDocuments, self).iter(page_size)

    @property
    def _session(self):
        return self.session

    def _obj_type(self, **kwargs):
        return FolderDocument

    @property
    def _url(self):
        return '/folders/%s/documents' % self.id
