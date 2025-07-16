from abc import ABC, abstractmethod


class IDocumentFormat(ABC):
    @abstractmethod
    def get_format(self) -> str:
        pass

class Excel(IDocumentFormat):
    def get_format(self) -> str:
        return 'xlsx'

class CSV(IDocumentFormat):
    def get_format(self) -> str:
        return 'csv'

class DocumentFactory:
    @staticmethod
    def create_document(format: str) -> IDocumentFormat:
        if format == 'xlsx':
            return Excel()
        elif format == 'csv':
            return CSV()
        else:
            raise ValueError("Unsupported document format")


excel_doc = DocumentFactory.create_document('xlsx')
print(excel_doc)
csv_doc = DocumentFactory.create_document('csv')
print(csv_doc)
pdf_doc = DocumentFactory.create_document('pdf')
print(pdf_doc)

