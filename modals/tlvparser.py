import marshaller.colmarshal
import marshaller.valmarshal
import modals
import modals.reader
import marshaller

class TLVParser:
    reader : modals.reader.Reader

    def __init__(self,reader):
        self.reader = reader

    def parse(self):
        data = self.reader.read_tlv()

        tlvunmarshaller = marshaller.valmarshal.TLVUnmarshaller(data)
        return tlvunmarshaller.tlv_unmarshal()


        