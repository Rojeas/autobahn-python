# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class Yield(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsYield(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Yield()
        x.Init(buf, n + offset)
        return x

    # Yield
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Yield
    def Request(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Yield
    def Payload(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Yield
    def PayloadAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Yield
    def PayloadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Yield
    def EncAlgo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Yield
    def EncSerializer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Yield
    def EncKey(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Yield
    def EncKeyAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Yield
    def EncKeyLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def YieldStart(builder): builder.StartObject(5)
def YieldAddRequest(builder, request): builder.PrependUint64Slot(0, request, 0)
def YieldAddPayload(builder, payload): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(payload), 0)
def YieldStartPayloadVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def YieldAddEncAlgo(builder, encAlgo): builder.PrependUint8Slot(2, encAlgo, 0)
def YieldAddEncSerializer(builder, encSerializer): builder.PrependUint8Slot(3, encSerializer, 0)
def YieldAddEncKey(builder, encKey): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(encKey), 0)
def YieldStartEncKeyVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def YieldEnd(builder): return builder.EndObject()